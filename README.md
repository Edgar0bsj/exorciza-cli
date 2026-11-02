<div align="center">

# EXORCIZA CLI

Este projeto nasceu de uma dor visceral, quase bíblica: a triste realidade do **pobre coitado do programador** que, em pleno século XXI, ainda é forçado a abrir, tratar, formatar e tentar entender planilhas infinitas (_ó, céus, a crueldade corporativa não tem limites!_).

Para evitar que mentes brilhantes definhem clicando em células do Excel ou corrigindo nomes e CPFs manualmente, criamos este ecossistema de **feitiços, simpatias e mandingas tecnológicas**.

O objetivo aqui é simples: **automação cirúrgica, limpeza de dados sem dor de cabeça e zero paciência para processos manuais.**

**Aviso Importante do Departamento de Defesa da Saúde Mental:**
Usar este projeto pode causar efeitos colaterais graves, como: terminar a demanda da semana em 4 segundos, ter tempo de sobra para tomar café sem culpa e a perigosa ilusão de que o setor administrativo aprendeu a usar o Excel. Use com moderação. Se a gerência descobrir o quanto isso facilita sua vida, eles vão te mandar tratar um arquivo .csv de 2GB via bloco de notas. Você foi avisado.

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge" /> <img src="https://img.shields.io/badge/Windows-017AD7?style=for-the-badge" /> <img src="https://img.shields.io/badge/Linux-E34F26?style=for-the-badge&logo=linux&logoColor=black" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />

[Instalação](#instalação) · [Docker](#docker-opcional) · [Configurações](#configurações) · [Comandos](#comandos) · [Desenvolverdor](#desenvolverdor) · [Licença](#licença)

</div>

## Instalação

Recomendação, Use a versão Python 3.12

Clone o repositório:

```bash
git clone https://github.com/Edgar0bsj/exorciza-cli.git
```

```bash
cd exorciza-cli
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

- Recomendo fortemente utilizar o **Python 3.12** para executar o projeto.
- py --list
- py -3.12 -m -venv venv
- venv/Scripts/activate

Instale as dependências e o projeto:

```bash
pip install -r requirements.txt

pip install -e .
```

Após a instalação, o comando `exorciza` estará disponível no terminal.

## Docker (Opcional)

Se você é do tipo que tem pavor de sujar seu próprio sistema operacional ou só quer evitar o clássico _"funciona na minha máquina"_, parabéns: eu já fiz o trabalho pesado. Deixei um `Dockerfile` tinindo, baseado num Ubuntu raiz, pronto para rodar sem explodir seu computador (em tese :/).

Para invocar essa obra-prima, execute o script no seu terminal:

1. **Buildando a imagens meu nobre:**

   ```bash
   docker build -t [nome-da-imagem] .

   ```

2. **Iniciando o container:**

   ```bash
   docker run -it --name [nome-do-container] [nome-da-imagem]

   ```

**Um aviso rápido**: o container vai inicializar do lado de fora do ambiente virtual. Não entre em pânico. É só ativar a venv e voilà: todos os comandos e feitiços tecnológicos do exorciza estarão no seu controle.

## Configurações

A pasta src/config é o centro de comando das configurações do projeto. Nela ficam os arquivos responsáveis por definir os parâmetros de cada entidade.
**_Atenção, recruta_**: não altere a estrutura dos arquivos ou da pasta. A missão é ajustar apenas os valores das configurações.

## Comandos

### **ava-manager** [_Contexto_]

Integrado ao ecossistema do ava manager, este comando assume a responsabilidade de traduzir e mapear a planilha-base oficial. É o ritual de passagem obrigatório para que os dados entrem no sistema sem corromper a matriz.

**Colunas obrigatórias:**

- `acessibilidade`
- `nome`
- `cpf`
- `login`
- `senha`
- `tags`
- `ativo`

```bash
exorciza ava-manager [options]
```

options

- **--file | -f** : caminho/arquivo.xlsx (Obrigatório)

## Desenvolverdor

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Edgar0bsj" title="Perfil do colaborador no GitHub">
        <img src="https://avatars.githubusercontent.com/u/180589510?v=4" width="100" alt="Foto do colaborador no GitHub"/><br>
        <sub>
          <b>Edgar Junior</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [`LICENSE`](./LICENSE) para mais informações.
