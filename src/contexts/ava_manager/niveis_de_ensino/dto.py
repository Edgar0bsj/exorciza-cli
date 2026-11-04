from pydantic import BaseModel, field_validator

from src.err.exception_errs import ExtractionYmlError


class NivelEnsinoContent(BaseModel):
    externo_id: str
    tipo_nivel_de_ensino: str

    @field_validator("externo_id", mode="before")
    @classmethod
    def setter_externo_id(cls, v):
        externo_id_limpo = str(v).strip()
        if not externo_id_limpo:
            raise ExtractionYmlError(f"Externo_id inválido ou vazio: {v}")
        return externo_id_limpo

    @field_validator("tipo_nivel_de_ensino", mode="before")
    @classmethod
    def setter_tipo(cls, v):
        tipo_limpo = str(v).strip()
        if not tipo_limpo:
            raise ExtractionYmlError(f"Tipo inválido ou vazio: {v}")
        return tipo_limpo


class NivelEnsinoDTO(BaseModel):
    nome: str
    nvl_ens_content: NivelEnsinoContent

    @field_validator("nome", mode="before")
    @classmethod
    def setter_nome(cls, v):
        nome_limpo = str(v).strip().lower()
        if not nome_limpo:
            raise ExtractionYmlError(f"Nome inválido ou vazio: {v}")
        return nome_limpo
