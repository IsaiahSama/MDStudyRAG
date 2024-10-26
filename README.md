# MDStudyRag

This is MDStudyRag, a project developed by me, to take advantage of the fact that I do my notes in markdown (MD). The aim is to have an assistant program that will take the markdown, do any necessary pre-processing, then eventually use to RAG the Gemini model.

# How to use

1. Clone or download the repository.
2. Create a virtual environment (preferably), then run `pip install -r requirements.txt` to download the dependencies.
3. Copy the .env.sample file, and rename the copy to `.env`. 
4. Acquire a Gemini API key, and be sure to seet it in the `.env` file.
5. Run `python main.py` to run the cli program.

## Getting your API Key

[Get your API Key Here](https://aistudio.google.com/app/apikey)

## ToDO (DONE)

~~Currently, I have not yet developed the CLI nor GUI interface to make it dynamic, but I am currently working on it.  However, if you want to test it, you can check the `test_pipeline.py` file, change the `md_file` variable, to point to the markdown file, change the `query` to reflect the question you want to ask, and then run `python test_pipeline.py`!~~

~~Later, I'll add licensing as well for open source reasons. I'm expecting to get the CLI and GUI with Tkinter finished in about a week, so look forward to it.~~

The CLI is now complete, so you can run the main.py file :D