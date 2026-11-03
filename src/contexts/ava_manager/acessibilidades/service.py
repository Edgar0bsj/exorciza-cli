from pathlib import Path

import yaml

from src.contexts.ava_manager.acessibilidades.dto import AcessibilidadeDTO, AcessType


class AcessibilidadeService:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        self.PARANS_YML = Path("config/ava_manager_ctx/acessibilidade.yml")

    def yaml_load(self) -> list[AcessibilidadeDTO]:
        config_path = self.BASE_DIR / self.PARANS_YML

        _buffer = []
        _arquivo_yml: dict | None = None

        with open(config_path, "r", encoding="utf-8") as arquivo:
            config = yaml.safe_load(arquivo)
            _arquivo_yml = config

        for k, v in _arquivo_yml.items():
            acess_type = AcessType(**v)
            acess_dto = AcessibilidadeDTO(nome=str(k), manager_content=acess_type)
            _buffer.append(acess_dto)

        return _buffer
