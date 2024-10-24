"""This file will contain the generic mennu options for the application."""

from abc import ABCMeta, abstractmethod
from typing import Dict

class BaseMenu(metaclass=ABCMeta):
    """An abstract class with the definition for methods that any menu system used by the app should support.
    
    Methods to be implemented:
    
    display_menu(self)
    
    query_llm(self)
    
    upload_document(self)
    
    view_documents(self)
    
    update_document(self)
    
    delete_document(self)
    
    clear_database(self)
    
    exit_program(self)
    
    """
    
    base_menu_options: Dict[str, Dict[str, str]] = {
        "QUERY LLM": {
            "description": "Query the LLM",
            "function": None
        },
        "UPLOAD DOCUMENT": {
            "description": "Upload a document",
            "function": None
        },
        "VIEW DOCUMENTS": {
            "description": "View documents",
            "function": None
        },
        "UPDATE DOCUMENT": {
            "description": "Update a document",
            "function": None
        },
        "DELETE DOCUMENT": {
            "description": "Delete a document",
            "function": None
        },
        "CLEAR DATABASE": {
            "description": "Clear the database",
            "function": None
        },
        "EXIT PROGRAM": {
            "description": "Exit the program",
            "function": None
        }
    }
    
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def display_menu(self) -> None:
        pass
    
    @abstractmethod
    def query_llm(self) -> str:
        pass
    
    @abstractmethod
    def upload_document(self) -> None:
        pass
    
    @abstractmethod
    def view_documents(self) -> None:
        pass
    
    @abstractmethod
    def update_document(self) -> None:
        pass
    
    @abstractmethod
    def delete_document(self) -> None:
        pass
    
    @abstractmethod
    def clear_database(self) -> None:
        pass
    
    @abstractmethod
    def exit_program(self) -> None:
        raise SystemExit
    