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
        
    def get_or_create_collection(self, collection_name: str, embedding_function:chromadb.EmbeddingFunction) -> None:
        """Gets or creates a collection with the given name and embedding function

        Args:
            collection_name (str): _description_
            embedding_function (chromadb.EmbeddingFunction): _description_
        """
        self.db = self.client.get_or_create_collection(name=collection_name, embedding_function=embedding_function())
        return None

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
                documents=[d],
                ids=[str(i + initial_size)]
            )
            sleep(0.5)
            
        return None
    
    def query_collection(self, query: str, n_results:int = 5) -> List[str]:
        """Queries the collection and returns the resulting documents.

        Args:
            query (str): The query to execute
            n_results (int, optional): The number of top results to return. Defaults to 5.

        Returns:
            List[str]: The resulting documents contained as a list of strings
        """
        
        if not self.db or not isinstance(self.db, chromadb.Collection): 
            raise InvalidCollectionException("Collection not initialized")
        
        passages = self.db.query(
            query_texts=query, 
            n_results=n_results
        )['documents'][0]
        
        return passages