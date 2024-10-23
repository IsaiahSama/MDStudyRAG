"""This file will be used for testing the functionality of the ChromaClient"""

from chroma.chroma import ChromaClient, InvalidCollectionException
from gemini.embedding import GeminiEmbeddingFunction

client = ChromaClient(path=".")

client.get_or_create_collection("test", GeminiEmbeddingFunction)

client.add_items_to_collection(["This is something about cars", "Something about Pineapples", "Something about squares"])

car_passages = client.query_collection("cars", n_results=2)

print(car_passages)

square_passages = client.query_collection("apple", n_results=2)

print(square_passages)