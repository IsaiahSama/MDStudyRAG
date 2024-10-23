"""This file will be used for testing the functionality of the ChromaClient"""

from chroma.chroma import ChromaClient, InvalidCollectionException
from gemini.embedding import GeminiEmbeddingFunction
from os import remove, path, rmdir

chroma_path = "test_chroma"
client = ChromaClient(path=chroma_path)

client.get_or_create_collection("test", GeminiEmbeddingFunction)

client.add_items_to_collection(["This is something about cars", "Something about Pineapples", "Something about squares"])

car_passages = client.query_collection("cars", n_results=2)

assert car_passages[0] == "This is something about cars"

fruit_passages = client.query_collection("apple", n_results=2)

assert fruit_passages[0] == "Something about Pineapples"

client.delete_collection("test")

final_path = path.join(chroma_path, "chroma.sqlite3")
if path.exists(final_path):
    remove(final_path)
    rmdir(chroma_path)