"""This will launch the CLI version of the tool."""

from pathlib import Path
from typing import Annotated

import typer
from pyinputplus import inputYesNo

from tools import CliMenu

app = typer.Typer(help="Study your markdown notes with Gemini. Run with no command for the interactive menu.")

Yes = Annotated[bool, typer.Option("--yes", "-y", help="Skip the confirmation prompt.")]


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """The entry point"""
    if ctx.invoked_subcommand:
        return

    menu = CliMenu()

    clear_screen = inputYesNo("Hey there! Would you like me to clear the screen after menu use? (y/n) [Will prompt each time]\n:", postValidateApplyFunc=lambda x: x == 'yes')

    # The while loop!
    while True:
        # Display the menu!

        menu.display_menu()
        print("---")
        if clear_screen:
            input("Press enter to clear screen.")
            typer.clear()


@app.command()
def query(
    collection: Annotated[str | None, typer.Argument(help="Collection to query.")] = None,
    question: Annotated[str | None, typer.Argument(help="What to ask.")] = None,
    level: Annotated[int | None, typer.Option(min=1, max=3, help="1 = Basic, 2 = Intermediate, 3 = Advanced.")] = None,
    save: Annotated[bool | None, typer.Option("--save/--no-save", help="Save the response to ./result.txt.")] = None,
):
    """Ask the LLM a question about a collection."""
    CliMenu().query_llm(collection, question, level, save)


@app.command()
def upload(
    path: Annotated[Path | None, typer.Argument(exists=True, dir_okay=False, help="Markdown file to upload.")] = None,
    title: Annotated[str | None, typer.Option(help="Title for the collection.")] = None,
    yes: Yes = False,
):
    """Upload a markdown document as a new collection."""
    CliMenu().upload_document(str(path) if path else None, title, yes)


@app.command("list")
def list_collections():
    """List all collections."""
    CliMenu().view_documents()


@app.command()
def delete(
    collection: Annotated[str | None, typer.Argument(help="Collection to delete.")] = None,
    yes: Yes = False,
):
    """Delete a collection."""
    CliMenu().delete_document(collection, yes)


@app.command()
def clear(yes: Yes = False):
    """Delete ALL collections."""
    CliMenu().clear_database(yes)


if __name__ == "__main__":
    app()
