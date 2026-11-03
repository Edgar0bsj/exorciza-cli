from pathlib import Path

import typer
from pydantic import ValidationError

from src.contexts.ava_manager.acessibilidades.controller import AcessibilidadeController
from src.err.exception_errs import ExtractionYmlError
from src.util import logger

app = typer.Typer()


acessibilidade_contr = AcessibilidadeController()


def ava_manager(
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
    """
    Comando ava-manager: responsável por lidar com a burocracia
    de dados da plataforma manager do AVA, garantindo que a planilha
    passe pelo exorcismo antes de entrar no sistema.
    """
    try:
        # Acessibilidades
        logger.aviso("Iniciando Acessibilidade")
        acessibilidades_df = acessibilidade_contr.make_acess()

        # Modalidades de ensino
        # (EM DESENVOLVIMENTO)

        dir = Path("ava-manager")
        dir.mkdir(parents=True, exist_ok=True)

        acessibilidades_df.to_csv(
            dir / "accessibility.unig_producao.csv",
            sep=";",
            encoding="utf-8",
            index=False,
        )

    except ValidationError as err:
        msg = {}
        erros = err.errors()
        for e in erros:
            msg[e["msg"]] = e["loc"]
        for k, v in msg.items():
            logger.erro(f"{k} | {v}")

    except ExtractionYmlError as err:
        logger.erro(err.detail)
