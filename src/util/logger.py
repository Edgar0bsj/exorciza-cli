import typer


def info(mensagem: str):
    typer.secho(f"[INFO] {mensagem}", fg=typer.colors.BLUE)


def sucesso(mensagem: str):
    typer.secho(f"[SUCESSO] {mensagem}", fg=typer.colors.GREEN)


def aviso(mensagem: str):
    typer.secho(f"[AVISO] {mensagem}", fg=typer.colors.YELLOW)


def erro(mensagem: str):
    typer.secho(f"[ERRO] {mensagem}", fg=typer.colors.RED, err=True)
