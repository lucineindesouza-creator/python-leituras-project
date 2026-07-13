# python-leituras-project
Sistema desenvolvido em Python para registrar, organizar e analisar livros lidos ao longo dos anos utilizando a biblioteca Pandas.

# Biblioteca Pessoal

Sistema desenvolvido em Python para registrar, organizar e analisar livros lidos ao longo dos anos utilizando a biblioteca Pandas.

# Objetivos

- Registrar livros lidos por ano.
- Organizar os dados em DataFrames.
- Realizar consultas e filtros.
- Gerar estatísticas de leitura.
- Produzir gráficos para visualização dos dados.

# Tecnologias utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn


# Funcionalidades

- Cadastro de livros por ano.
- Organização dos dados em DataFrames.
- Concatenação de vários anos em uma única base.
- Consulta por autor.
- Consulta por título.
- Soma de páginas lidas.
- Contagem de livros por ano.
- Verificação de valores nulos e duplicados.
- Estatísticas descritivas.
- Gráfico de barras com livros lidos por ano.
- Gráfico de pizza da distribuição por autor.

# Estrutura do projeto

```
python-leituras-project/
├── graficos/
    ├──contagem_registros_por_autor.png
    ├──total_livros_por_ano.png
│
├── leituras.py
├── requirements.txt
├── LICENSE
├── README.md
├── README.txt
├── .gitignore
```

# Instalação

Clone o repositório:

```bash
git clone https://github.com/lucineindesouza-creator/python-leituras-project.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python leituras.py
```

# Melhorias futuras

- Desenvolver uma interface gráfica utilizando **Tkinter** ou **CustomTkinter**.
- Implementar um formulário para entrada de dados, permitindo ao usuário cadastrar novos livros, autores, anos, meses, 
quantidade de páginas, status de leitura e resenhas diretamente pelo sistema, sem a necessidade de editar o código-fonte.
- Realizar leitura automática dos registros a partir de arquivos Excel (.xlsx) e CSV.
- Integrar um banco de dados SQLite para armazenamento permanente dos registros de leitura.
- Criar dashboards interativos utilizando Plotly para análise das leituras.
- Exportar relatórios e estatísticas em formato PDF.
- Desenvolver estatísticas avançadas, como páginas lidas por mês, média de páginas por livro, autores mais lidos, evolução anual das 
leituras e metas de leitura.
- Adicionar funcionalidades de edição, exclusão e pesquisa de registros por título, autor, ano ou status de leitura.

# Autor

**Lucinei Neris**

Estudante de Ciência de Dados, com foco em Python, análise de dados, automação e desenvolvimento de projetos para portfólio no GitHub.

# Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
