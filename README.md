# MDStudyRag

This is MDStudyRag, a project developed by me, to take advantage of the fact that I do my notes in markdown (MD). The aim is to have an assistant program that will take the markdown, do any necessary pre-processing, then eventually use to RAG the Gemini model.

# How to use

1. Clone or download the repository.
2. Install [`uv`](https://docs.astral.sh/uv/), the Python package and project manager.
3. Copy the `.env.sample` file, and rename the copy to `.env`. 
4. Acquire a Gemini API key, and be sure to set it in the `.env` file.
5. Run `uv sync` to install the dependencies and set up the virtual environment.
6. Run `uv run main.py` to run the cli program.

## Commands

Running `uv run main.py` with no command opens the interactive menu. You can also run a single action directly. Anything you leave out will be prompted for.

```
uv run main.py query <collection> "<question>" --level 2 --save
uv run main.py upload notes.md --title "Caribbean Frontiers" -y
uv run main.py list
uv run main.py delete <collection> -y
uv run main.py clear -y
```

`--level` is 1 (Basic), 2 (Intermediate) or 3 (Advanced). `-y` skips the confirmation prompt. Run `uv run main.py <command> --help` for details.

## Getting your API Key

[Get your API Key Here](https://aistudio.google.com/app/apikey)
