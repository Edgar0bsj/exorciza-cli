import typer

from src.contexts.ava_manager.commands import ava_manager
from src.core.version.version import version

app = typer.Typer(
    name="exorciza",
    help="Ferramenta de automação e integração de dados.",
    epilog="Se funcionou de primeira, não mexe. Não olhe fixamente. Não faça barulho. Apenas aceite o milagre",
)


# =============================================
# VERSION
# =============================================
@app.callback(invoke_without_command=True)
def main(
    version_flag: bool = typer.Option(None, "--version", "-v"),
):
    if version_flag:
        version()


# =============================================
# ADD COMMANDS
# =============================================
app.command(name="ava-manager")(ava_manager)

# =============================================
# START
# =============================================
if __name__ == "__main__":
    app()
