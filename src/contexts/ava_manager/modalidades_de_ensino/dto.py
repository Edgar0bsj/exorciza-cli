from pydantic import BaseModel, field_validator

from src.err.exception_errs import ExtractionYmlError


class ModalidadesEnsinoType(BaseModel):
    externo_id: str
    teachingModality: str

    @field_validator("externo_id", mode="before")
    @classmethod
    def setter_externo_id(cls, v):
        externo_id_limpo = str(v).strip()
        if not externo_id_limpo:
            raise ExtractionYmlError(f"Externo_id inválido ou vazio: {v}")
        return externo_id_limpo

    @field_validator("teachingModality", mode="before")
    @classmethod
    def setter_tipo(cls, v):
        teachingModality_limpo = str(v).strip()
        if not teachingModality_limpo:
            raise ExtractionYmlError(f"TeachingModality inválido ou vazio: {v}")
        return teachingModality_limpo


class ModalidadesEnsinoDTO(BaseModel):
    nome: str
    mod_ens_content: ModalidadesEnsinoType

    @field_validator("nome", mode="before")
    @classmethod
    def setter_nome(cls, v):
        nome_limpo = str(v).strip().lower()
        if not nome_limpo:
            raise ExtractionYmlError(f"Nome inválido ou vazio: {v}")
        return nome_limpo
