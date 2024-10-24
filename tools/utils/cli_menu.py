"""This will hold the implementation of the CLI menu."""

import pyinputplus as pyip

from typing import override, Dict
from tools.utils.base_menu import BaseMenu
from tools.chroma.chroma import ChromaClient
from tools.gemini.geminiClient import GeminiClient



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
        return super().query_llm()

    @override
    def upload_document(self) -> None:
        return super().upload_document()

    @override
    def view_documents(self) -> None:
        print(self.chroma_client.get_all_collection_names())
        return super().view_documents()

    @override
    def update_document(self) -> None:
        return super().update_document()

    @override
    def delete_document(self) -> None:
        return super().delete_document()

    @override
    def clear_database(self) -> None:
        return super().clear_database()

    @override
    def exit_program(self) -> None:
        super().exit_program()