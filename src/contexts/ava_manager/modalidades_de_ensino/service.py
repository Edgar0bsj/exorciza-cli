from pathlib import Path

import yaml

from src.contexts.ava_manager.modalidades_de_ensino.dto import (
    ModalidadesEnsinoDTO,
    ModalidadesEnsinoType,
)


class ModalidadesDeEnsinoService:
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
        self.PARANS_YML = Path("config/ava_manager_ctx/modalidades_de_ensino.yml")

    def yaml_load(self) -> list[ModalidadesEnsinoDTO]:
        config_path = self.BASE_DIR / self.PARANS_YML

        _buffer = []
        _arquivo_yml: dict | None = None

        with open(config_path, "r", encoding="utf-8") as arquivo:
            config = yaml.safe_load(arquivo)
            _arquivo_yml = config

        for k, v in _arquivo_yml.items():
            mod_ens_type = ModalidadesEnsinoType(**v)
            mod_ens = ModalidadesEnsinoDTO(nome=str(k), mod_ens_content=mod_ens_type)
            _buffer.append(mod_ens)

        return _buffer
