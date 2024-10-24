# MDStudyRag

This is MDStudyRag, a project developed by me, to take advantage of the fact that I do my notes in markdown (MD). The aim is to have an assistant program that will take the markdown, do any necessary pre-processing, then eventually use to RAG the Gemini model.

# How to use

1. Clone or download the repository.
2. Create a virtual environment (preferably), then run `pip install -r requirements.txt` to download the dependencies.
3. Copy the .env.sample file, and rename the copy to `.env`. 
4. Acquire a Gemini API key, and be sure to seet it in the `.env` file.
5. Run `python main.py` to launch the application.