# Process:

# Do all Imports!

# Read in context from md file.
## Do any necessary pre-processing.
## Chunk using langchain text_splitter.

# Store all chunks by calling page_content, into a list.

# Next is Embedding
# Make use of models/embedding-001 for embedding, then return the embedding as a vector.

# Can then create the chroma db, to go over each element in the vectors, and store in the db.

# Can then query the db for similar documents, and return the top n results.

# Can then create the prompt, and get the appropriate context.

#  Can then make a request to the model, and interpret the response

# OVerall Steps for consumption:

# 1. Provide the Question
# 2. Search chroma db for relevant documents.
# 3. Convert top n results to a single string to play the role of context.
# 4. Create the prompt with the context, question, and expected format for response.
# 5. Call the model, and get the response.