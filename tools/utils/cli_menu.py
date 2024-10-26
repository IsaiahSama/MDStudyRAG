"""This will hold the implementation of the CLI menu."""

import pyinputplus as pyip

from os.path import exists
from typing import List, override, Dict
# My imports!

try:
    from tools import BaseMenu, loader, ChromaClient, GeminiClient, GeminiEmbeddingFunction, md_to_json
except ImportError:
    from tools.utils.base_menu import BaseMenu
    from tools.utils import loader
    from tools.chroma.chroma import ChromaClient
    from tools.gemini.geminiClient import GeminiClient
    from tools.gemini.embedding import GeminiEmbeddingFunction
    from tools.md_to_json import md_to_json


class CliMenu(BaseMenu):
    """The CLI version of the menu"""
    
    def __init__(self) -> None:
        super().__init__()
        
        # Setup the clients
        self.chroma_client = ChromaClient()
        self.gemini_client = GeminiClient()
        
        # Add the options to the menu
        self.setup_menu()
        
    def setup_menu(self) -> None:
        self.menu_options = self.base_menu_options
        mappings = {
            "QUERY LLM": self.query_llm,
            "UPLOAD DOCUMENT": self.upload_document,
            "VIEW DOCUMENTS": self.view_documents,
            "UPDATE DOCUMENT": self.update_document,
            "DELETE DOCUMENT": self.delete_document,
            "CLEAR DATABASE": self.clear_database,
            "EXIT PROGRAM": self.exit_program
        }
        
        for key, value in mappings.items():
            self.menu_options[key]["function"] = value
        
    @override
    def display_menu(self) -> None:
        action = pyip.inputMenu(list(self.menu_options.keys()), "What would you like to do currently?\n", numbered=True)
        self.menu_options[action]["function"]()
    
    @override
    def query_llm(self) -> str:
        
        # Ask the user what collection they want to query
        print("Which collection would you like to query?")
        if not (collection := self.select_a_document()):
            return
        
        # Get the collection
        
        self.chroma_client.get_or_create_collection(collection, GeminiEmbeddingFunction, collection)
        
        # Ask the user for their query
        print(f"Understood. What would you like to ask about {collection}")
        query = pyip.inputStr()
        
        # Get the level for the query
        print("What level of detail do you want for your response?")
        prompt_level = pyip.inputChoice(["1", "2", "3"], prompt="Enter the level of detail you want for your response.\n(1 = Basic, 2 = Intermediate, 3 = Advanced)\n:", postValidateApplyFunc=lambda x: int(x))
        
        # Get the relevant context!
        passages = self.chroma_client.query_collection(query, n_results=5)
        context = ""
        if not passages:
            if prompt_level == 1:
                print("Couldn't find relevant context, so will use basic prompt.")
            else:
                print("Couldn't find relevant context")
                return
        else:
            context = ' '.join([f"PARTIALCONTEXT\n{passage}\nENDPARTIALCONTEXT\n" for passage in passages])
        
        # Prepare the prompt
        prompt = self.gemini_client.make_prompt(query, context, prompt_level)
        
        print("Prompt: ", prompt)
        
        # Return the response
        
        loadable = loader.Loadable(self.gemini_client.prompt_model, prompt)
        spinner = loader.LoadingSpinner()
        
        result = spinner.start("Asking your LLM!", loadable)
        
        print(f"\nYour Question: {query}\nModel Response:\n {result}\n")

    @override
    def upload_document(self) -> None:
        def validate_path(path: str) -> bool:
            if exists(path) and path.split(".")[-1] == "md":
                return path
            raise ValueError("Invalid path. Please enter a valid path to a markdown file.")
        
        doc_path = pyip.inputCustom(validate_path, "Enter the path to the document you would like to upload.\n:")
        
        title = pyip.inputStr("Fantastic! What should we title this collection? The title should reflect the nature of the content.\n:")
        
        # Helper function to use for displaying a loading screen!
        def format_and_prepare_document(doc_path: str) -> str:
            alpaca_json = md_to_json.md_to_alpaca_json(doc_path)
            stringified_alpaca_json = md_to_json.stringify_alpaca_json(alpaca_json)
            return stringified_alpaca_json
        
        ellipse = loader.LoadingSpinner()
        formatter = loader.Loadable(format_and_prepare_document, doc_path)
        
        stringified_alpaca_json = ellipse.start("Formatting and preparing the document!", formatter)
        
        # Then, we can upload the alpaca json, after confirming the user wants to proceed.
        proceed = pyip.inputYesNo("Are you sure you want to upload this document?\n:", postValidateApplyFunc=lambda x: x == 'yes')
        if not proceed: 
            print("Returning to menu!")
            return 
        
        self.chroma_client.get_or_create_collection(title.lower().replace(" ", "_"), GeminiEmbeddingFunction, title)
        self.chroma_client.add_items_to_collection(stringified_alpaca_json)
        
        print("Document uploaded!")

    @override
    def view_documents(self) -> List[str]:
        collections = self.chroma_client.get_all_collection_names()
        
        if collections:
            print("Listing names of collections.\n---")
            print(*self.chroma_client.get_all_collection_names(), sep="\n")
            print("---")
        
        return collections
        
    def select_a_document(self) -> str:
        collections = self.view_documents()
        if not (collections):
            print("No collections found. Please add a collection and try again.")
            return ""

        collection_name = pyip.inputMenu(collections, "Which collection would you like to perform actions on?\n", numbered=True, blank=True)
        return collection_name

    @override
    def update_document(self) -> None:
        collection_name = self.select_a_document()
        if not collection_name: return
        return super().update_document()

    @override
    def delete_document(self) -> None:
        collection_name = self.select_a_document()
        if not collection_name: return
        confirm = pyip.inputYesNo("Are you sure you want to delete this document?\n:", postValidateApplyFunc=lambda x: x == 'yes')
        
        if not confirm: 
            print("Aborting")
            return 
        
        self.chroma_client.delete_collection(collection_name)
        print("Collection deleted!")

    @override
    def clear_database(self) -> None:
        collections = self.view_documents()
        if not collections:
            print("No collections to delete.")
            return
        
        print("Clearing the databse means deleting ALL of the following records:")
        confirm = pyip.inputYesNo("Are you sure you want to clear the database?\n:", postValidateApplyFunc=lambda x: x == 'yes')
        
        if confirm:
            ellipse_loader = loader.LoadingEllipse()
            loadable = loader.Loadable(self.chroma_client.delete_all_collections)
            ellipse_loader.start("Clearing the database!", loadable)
            self.view_documents()
        else:
            print("Aborting")

    @override
    def exit_program(self) -> None:
        super().exit_program()