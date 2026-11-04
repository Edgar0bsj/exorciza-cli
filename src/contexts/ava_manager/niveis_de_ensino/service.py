from pathlib import Path

import yaml

from src.contexts.ava_manager.niveis_de_ensino.dto import (
    NivelEnsinoContent,
    NivelEnsinoDTO,
)


class NiveisDeEnsinoService:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        self.PARANS_YML = Path("config/ava_manager_ctx/niveis_de_ensino.yml")

    def yaml_load(self) -> list[NivelEnsinoDTO]:
        config_path = self.BASE_DIR / self.PARANS_YML

        _buffer = []
        _arquivo_yml: dict | None = None

        with open(config_path, "r", encoding="utf-8") as arquivo:
            config = yaml.safe_load(arquivo)
            _arquivo_yml = config

        for k, v in _arquivo_yml.items():
            nvl_content = NivelEnsinoContent(**v)
            nlv_ensino = NivelEnsinoDTO(nome=str(k), nvl_ens_content=nvl_content)
            _buffer.append(nlv_ensino)

        return _buffer
