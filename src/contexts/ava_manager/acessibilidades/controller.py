import pandas as pd
import typer
from pandas import DataFrame
from rich.progress import track

from src.contexts.ava_manager.acessibilidades.service import AcessibilidadeService
from src.util import logger


class AcessibilidadeController:
    def __init__(self):
        self.service = AcessibilidadeService()

    def make_acess(self) -> DataFrame:
        acess = self.service.yaml_load()

        manager = {"name": [], "externalId": [], "accessibilityTypeId": []}

        for element in track(
            acess,
            description="[cyan]Exorcizando Acessibilidades...[/cyan]",
            complete_style="bright_green",
            finished_style="bold green",
        ):
            manager["name"].append(element.nome)
            manager["externalId"].append(element.manager_content.externo_id)
            manager["accessibilityTypeId"].append(element.manager_content.tipo)

        logger.sucesso("Acessibilidade Exorcizado!")
        return pd.DataFrame(manager)
