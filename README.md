# MDStudyRag

This is MDStudyRag, a project developed by me, to take advantage of the fact that I do my notes in markdown (MD). The aim is to have an assistant program that will take the markdown, do any necessary pre-processing, then eventually use to RAG the Gemini model.

# How to use

1. Clone or download the repository.
2. Install [`uv`](https://docs.astral.sh/uv/), the Python package and project manager.
3. Copy the `.env.sample` file, and rename the copy to `.env`. 
4. Acquire a Gemini API key, and be sure to set it in the `.env` file.
5. Run `uv sync` to install the dependencies and set up the virtual environment.
6. Run `uv run main.py` to run the cli program.

## Getting your API Key

[Get your API Key Here](https://aistudio.google.com/app/apikey)
