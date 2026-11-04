import pandas as pd
from pandas import DataFrame
from rich.progress import track

from src.contexts.ava_manager.niveis_de_ensino.service import NiveisDeEnsinoService
from src.util import logger


class NiveisDeEnsinoController:
    def __init__(self):
        self.service = NiveisDeEnsinoService()

    def make_nlv_ensino(self) -> DataFrame:
        acess = self.service.yaml_load()

        manager = {"name": [], "externalId": [], "educationLevelTypeId": []}

        for element in track(
            acess,
            description="[cyan]Exorcizando Nivel de Ensino...[/cyan]",
            complete_style="bright_green",
            finished_style="bold green",
        ):
            manager["name"].append(element.nome)
            manager["externalId"].append(element.nvl_ens_content.externo_id)
            manager["educationLevelTypeId"].append(
                element.nvl_ens_content.tipo_nivel_de_ensino
            )

        logger.sucesso("Nivel de Ensino Exorcizado!")
        return pd.DataFrame(manager)
