from pathlib import Path

import typer
from pydantic import ValidationError

from src.contexts.ava_manager.acessibilidades.controller import AcessibilidadeController
from src.contexts.ava_manager.modalidades_de_ensino.controller import (
    ModalidadesDeEnsinoController,
)
from src.contexts.ava_manager.niveis_de_ensino.controller import (
    NiveisDeEnsinoController,
)
from src.err.exception_errs import ExtractionYmlError
from src.util import logger

app = typer.Typer()


acessibilidade_contr = AcessibilidadeController()
mod_ensino_contr = ModalidadesDeEnsinoController()
nivel_ensino_contr = NiveisDeEnsinoController()


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
        logger.aviso("> Iniciando Acessibilidade")
        acessibilidades_df = acessibilidade_contr.make_acess()

        # Modalidades de ensino
        logger.aviso("> Iniciando Modalidade de Ensino")
        modalidades_de_ensino_df = mod_ensino_contr.make_mod()

        # Nivel de Ensino
        logger.aviso("> Iniciando Nivel de Ensino")
        nivel_de_ensino_df = nivel_ensino_contr.make_nlv_ensino()

        dir = Path("ava-manager")
        dir.mkdir(parents=True, exist_ok=True)

        # ACESSIBILIDADE EXPORT
        logger.aviso("Exportando Acessibilidade")
        acessibilidades_df.to_csv(
            dir / "accessibility.unig_producao.csv",
            sep=";",
            encoding="utf-8",
            index=False,
        )

        # MODALIDADE DE ENSINO EXPORT
        logger.aviso("Exportando Modalidade de Ensino")
        modalidades_de_ensino_df.to_csv(
            dir / "teaching-modality.unig_producao.csv",
            sep=";",
            encoding="utf-8",
            index=False,
        )

        # NIVEL DE ENSINO EXPORT
        logger.aviso("Exportando Nivel de Ensino")
        nivel_de_ensino_df.to_csv(
            dir / "education-level.unig_producao.csv",
            sep=";",
            encoding="utf-8",
            index=False,
        )

        logger.sucesso("Exorcismo Feito com Sucesso !")

    except ValidationError as err:
        msg = {}
        erros = err.errors()
        for e in erros:
            msg[e["msg"]] = e["loc"]
        for k, v in msg.items():
            logger.erro(f"{k} | {v}")

    except ExtractionYmlError as err:
        logger.erro(err.detail)
