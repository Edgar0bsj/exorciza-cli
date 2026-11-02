import re

import pandas as pd


# ================================================
# CPF
# ================================================
def cpf(valor) -> str | None:

    if pd.isna(valor) or not str(valor).strip():
        return None

    try:
        if isinstance(valor, (float, int)):
            val_str = f"{int(valor)}"
        else:
            val_str = str(valor).strip()
        val_str = val_str.removesuffix(".0")

        apenas_digitos = re.sub(r"\D", "", val_str)

        if not apenas_digitos:
            return None

        cpf_padronizado = apenas_digitos.zfill(11)

        if len(cpf_padronizado) != 11:
            return None

        return cpf_padronizado

    except (ValueError, TypeError):
        return None


# ================================================
# NOME
# ================================================
def nome(valor) -> str | None:
    if pd.isna(valor) or not str(valor).strip():
        return None

    try:
        nome_str = str(valor).strip()

        nome_limpo = re.sub(r"[^a-zA-ZÀ-ÿ\s\'\.]", "", nome_str)

        nome_limpo = re.sub(r"\s+", " ", nome_limpo)

        if not nome_limpo:
            return None

        minusculas = {"de", "da", "do", "dos", "das", "e", "del", "dela"}

        palavras = nome_limpo.lower().split()
        palavras_formatadas = []

        for i, palavra in enumerate(palavras):
            if i > 0 and palavra in minusculas:
                palavras_formatadas.append(palavra)
            else:
                palavras_formatadas.append(palavra.capitalize())

        return " ".join(palavras_formatadas)

    except (ValueError, TypeError):
        return None
