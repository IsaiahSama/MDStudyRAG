from tools import md_to_json, ChromaClient, GeminiEmbeddingFunction, GeminiClient
from typing import List, Dict

"""This file will test the process from start to finish!"""

# First, we'll select a markdown file!

md_file: str = "./caribbean_frontiers.md"

# Then, we turn this! Into Alpaca Json

alpaca_json: List[Dict[str, Dict[str, str]]] = md_to_json.md_to_alpaca_json(md_file)

stringified_alpaca_json: List[str] = md_to_json.stringify_alpaca_json(alpaca_json)

# Now, we make embeddings!

chroma_client: ChromaClient = ChromaClient()

# try:
#     chroma_client.delete_collection("testing")
# except: 
#     pass

chroma_client.get_or_create_collection("testing", GeminiEmbeddingFunction, "Caribbean Frontiers")

# And store them in the database!

chroma_client.add_items_to_collection(stringified_alpaca_json)

# Prepare the query!!!!!!!

query = "Can you tell me what is Jonathan's role as a member of the team, and tell me a bit about him along with his weapon of choice? Also, is he an explorer, leader, warrior or guardian?"
print("Query: ", query)

# Get the relevant passaages from the database

passages: List[str] = chroma_client.query_collection(query, n_results=3)

print("Relevant Passages based on query: ", passages)

context_passage = ' '.join(passages)

gemini_client = GeminiClient()

# Creat the prompt!
prompt = gemini_client.make_prompt(query, context_passage, 3)

print("The prompt: ", prompt)

# Fireeeeee

response = gemini_client.prompt_model(prompt)

print("Gemini Response: ", response)
