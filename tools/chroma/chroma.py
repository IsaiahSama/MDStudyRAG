import chromadb
from chromadb.errors import InvalidCollectionException
from typing import List
from time import sleep
from tqdm import tqdm

class ChromaClient:
    client: chromadb.ClientAPI
    db: chromadb.Collection
    
    def __init__(self, client: chromadb.ClientAPI | None=None, root="./", path="chroma") -> None:
        if client is None:
            client = chromadb.PersistentClient(path=root+path)
            
        self.client: chromadb.ClientAPI = client
        self.db = None
        
    def get_or_create_collection(self, collection_name: str, embedding_function) -> None:
        self.db = self.client.get_or_create_collection(name=collection_name, embedding_function=embedding_function)

    def add_items_to_collection(self, items: List[str]) -> None:
        """Adds the items to the collection initialized using the get_or_create_collection method

        Args:
            items (List[str]): The list of string items to add to the collection.

        Raises:
            InvalidCollectionException: Error raised if self.db is not initialized or not a chromadb.Collection
        """
        
        if not self.db or not isinstance(self.db, chromadb.Collection): 
            raise InvalidCollectionException("Collection not initialized")
        
        initial_size = self.db.count()
        
        for i, d in tqdm(enumerate(items), total=len(items), desc="Adding items to collection"):
            self.db.add( 
                documents=d,
                ids=str(i + initial_size))
            sleep(0.5)
            
    def get_db(self, collection_name: str) -> chromadb.Collection:
        """Gets a collection by it's name.

        Args:
            collection_name (str): The name of the collection to get from the chroma db

        Returns:
            chromadb.Collection: The returned collection
        """
        return self.client.get_collection(name=collection_name)
    
    def get_current_db(self) -> chromadb.Collection:
        """Gets the collection using the current initialized db value.

        Raises:
            InvalidCollectionException: Error raised when self.db is not initialized or not a chromadb.Collection

        Returns:
            chromadb.Collection: The collection from the client.
        """
        if not self.db or not isinstance(self.db, chromadb.Collection): 
            raise InvalidCollectionException("Collection not initialized")

        return self.client.get_collection(name=self.db.name)