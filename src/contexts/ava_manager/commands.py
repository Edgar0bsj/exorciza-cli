from pathlib import Path

import typer

from src.contexts.ava_manager.pessoas.controller import PessoaController
from src.util import logger

app = typer.Typer()
pessoa_contr = PessoaController()


def ava_manager(
    person: bool | None = typer.Option(None, "--person", "-p"),
    xlsx_file: Path = typer.Option(  # noqa: B008
        ...,
        "--file",
        "-f",
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
    ),
):
    try:
        if person:
            # EM DESENVOLVIMENTO
            # person_df = pessoa_contr.make_person(xlsx_file)
            return

        # EM DESENVOLVIMENTO
    except:
        ...
        # EM DESENVOLVIMENTO
