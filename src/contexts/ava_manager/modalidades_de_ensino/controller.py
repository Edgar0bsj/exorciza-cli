import pandas as pd
from pandas import DataFrame
from rich.progress import track

from src.contexts.ava_manager.modalidades_de_ensino.service import (
    ModalidadesDeEnsinoService,
)
from src.util import logger


class ModalidadesDeEnsinoController:
    def __init__(self):
        self.service = ModalidadesDeEnsinoService()

    def make_mod(self) -> DataFrame:
        mod_ens_list = self.service.yaml_load()

        manager = {"name": [], "externalId": [], "teachingModalityTypeId": []}

        for element in track(
            mod_ens_list,
            description="[cyan]Exorcizando Modalidade...[/cyan]",
            complete_style="bright_green",
            finished_style="bold green",
        ):
            manager["name"].append(element.nome)
            manager["externalId"].append(element.mod_ens_content.externo_id)
            manager["teachingModalityTypeId"].append(
                element.mod_ens_content.teachingModality
            )

        logger.sucesso("Modalidades de ensino Exorcizado!")
        return pd.DataFrame(manager)
