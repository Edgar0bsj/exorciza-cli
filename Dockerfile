FROM ubuntu

RUN mkdir /app
WORKDIR /app

COPY . .

RUN apt update && apt upgrade -y

# Instala as dependências básicas
RUN apt install software-properties-common -y

# Repositório com as versões do Python
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt update

# Instalação do Python 3.12, venv e pip
RUN apt install python3.12 python3.12-venv python3-full -y

# Cria o ambiente virtual
RUN python3.12 -m venv /app/venv

# Atualiza o pip dentro da venv
RUN /app/venv/bin/pip install --upgrade pip

# Instala o pacote local em modo editável (-e .) durante o build
RUN /app/venv/bin/pip install -e .

# Comando padrão para iniciar a sua aplicação 
CMD ["/app/venv/bin/python", "-m", "src.main"]