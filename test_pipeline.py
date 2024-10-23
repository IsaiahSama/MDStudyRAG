from tools import md_to_json, ChromaClient, GeminiEmbeddingFunction, GeminiClient
from typing import List, Dict

import pandas as pd


"""This file will test the process from start to finish!"""

# First, we'll select a markdown file!

md_file: str = "./tools/md_to_json/small_sample.md"

# Then, we turn this! Into Alpaca Json

alpaca_json: List[Dict[str, Dict[str, str]]] = md_to_json.md_to_alpaca_json(md_file)

stringified_alpaca_json: List[str] = md_to_json.stringify_alpaca_json(alpaca_json)

# Now, we make embeddings!

chroma_client: ChromaClient = ChromaClient()

chroma_client.delete_collection("testing")
chroma_client.get_or_create_collection("testing", GeminiEmbeddingFunction, "Database Management Systems Course Information")

chroma_client.add_items_to_collection(stringified_alpaca_json)

query = "Give me information about Traditional File Systems"

passages: List[str] = chroma_client.query_collection(query, n_results=3)

context_passage = ' '.join(passages)

gemini_client = GeminiClient()

prompt = gemini_client.make_prompt(query, context_passage)

response = gemini_client.prompt_model(prompt)

print(response)
