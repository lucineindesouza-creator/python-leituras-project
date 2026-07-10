"""
Projeto: Biblioteca Pessoal
Autor: Lucinei Neris
Versão: 1.0.0
Data de criação: 10/07/2026
Descrição: Sistema para gerenciamento de livros lidos, com funcionalidades de análise, gráficos e visualização de dados.
"""

# Instalação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Instala o pacote watermark para exibir informações do autor e do ambiente de execução no Jupiter Notebook

#!pip install -q -U watermark

#%reload_ext watermark

#%watermark -a "Lucinei Neris" -d

#%watermark -v -p numpy,pandas,matplotlib,seaborn


# Criação do DataFrame com os registros de leituras de 2023
registros_2023 = pd.DataFrame({ 
    "Ano": [
        2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023
    ],

    "Mês": [
        "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
        "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ],

    "Título": [
        "Eu venci a depressão", "Esperança além da crise", "Como vencer suas guerras pela fé",
        "Orixás, caboclos e guias. Deuses ou demônios?", "A luz do presidiário", "A cabana",
        "A volta ao mundo em 80 dias", "O segredo da última escolha", "O caçador de pipas",
        "O caçador de corruptos", "Os segredos do Pai Nosso"
    ],

    "Autor": [
        "Dra. Eunice Higuchi", "Mark Finley", "Edir Macedo", "Edir Macedo", "Edir Macedo", "William P. Young",
        "Júlio Verne", "Andy Andrews", "Khaled Hosseini", "Augusto Cury", "Augusto Cury"
    ],

    "Status": [
        "Lido", "Lido", "Lido", "Lido", "Lido", "Lido",
        "Lido", "Lido", "Lido", "Lido", "Lido"
    ],

    "Resenha": [
        "Sim", "Sim", "Sim", "Sim", "Sim", "Sim",
        "Sim", "Sim","Sim", "Sim", "Sim"
    ],

    "Páginas": [
        136, 80, 264, 200, 160, 240, 272,
        248, 365, 240, 112
    ]
})

print("\nRegistros de leituras em 2023:")

print(registros_2023)

#Criação do DataFrame com os registros de leituras de 2024
registros_2024 = pd.DataFrame({ 
    "Ano": [
        2024, 2024, 2024, 2024, 2024, 2024,
        2024, 2024, 2024, 2024, 2024, 2024
    ],
    "Mês": [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro","Dezembro"
    ],
    "Título": [
        "Fronteira", "O código Da Vinci", "Capitães de Areia", "Eu lhes darei um coração novo",
        "A Graça plena de Deus", "A corrente da vida", "O meu cálice transborda", "Confiando em Deus todo dia",
        "Importa Renascer", "Êxodo", "Levítico", "Números"
    ],
    "Autor": [
        "Robinson Pereira", "Dan Brown", "Jorge Amado", "Glênio Fonseca Paranaguá", "Antonio Abuchaim",
        "Walcir Carrasco", "Glênio Fonseca Paranaguá", "Charles Spurgeon", "Antonio Abuchaim",
        "Bíblia Sagrada", "Bíblia Sagrada", "Bíblia Sagrada"
    ],
    "Status": [
        "Lido", "Lido", "Lido", "Lido", "Lido", "Lido",
        "Lido", "Lido", "Lido", "Lido", "Lido", "Lido"
    ],
    "Resenha": [
        "Sim", "Sim", "Sim", "Sim", "Sim", "Sim",
        "Sim", "Sim", "Sim", "Sim", "Sim", "Sim"
    ],
    "Páginas": [
        250, 312, 283, 64, 80, 96, 96, 112, 80, 100, 75, 95
    ]
})

print("\nRegistros de leituras em 2024:")

print(registros_2024)

# Criação do DataFrame com os registros de leituras de 2025
registros_2025 = pd.DataFrame({
    "Ano": [
        2025, 2025, 2025, 2025, 2025, 2025,
        2025, 2025, 2025, 2025, 2025, 2025
    ],
    "Mês": [
        "Janeiro",  "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ],
    "Título": [
        "Deuteronômio", "Josué", "Os mistérios da fé", "Os quatro compromissos", "Nossa união com Cristo", 
        "A salvação de A a Z. A Sã doutrina.", "Barro em suas mãos", "Uma prova do Céu", "Os perigos do lado bom da alma",
        "Em cima do ringue", "Os propósitos da Encarnação", "Ódio sustenido"
    ],
    "Autor": [
        "Bíblia Sagrada", "Bíblia Sagrada", "Edir Macedo", "Don Miguel Ruiz", "David Kuykendall", "Glênio Fonseca Paranaguá", 
        "Antonio Abuchaim", "Dr. Eben Alexander III", "Dong Yu Lang", "Henrique Felix", "G. Campbell Morgan", "Nelson de Oliveira"
    ],
    "Status": [
        "Lido", "Lido", "Lido", "Lido", "Lido", "Lido", "Lido", "Lido", "Lido", "Lido", "Lido", "Lido"
    ],
    "Resenha": [
        "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Sim"
    ],
    "Páginas": [
        85, 65, 80, 112, 208, 96, 144, 186, 94, 82, 64, 88
    ]
})

print("\nRegistros de leituras em 2025:")
print(registros_2025)

# Concatenando os DataFrames de 2023, 2024 e 2025 em um único DataFrame
df_registros = pd.concat([registros_2023, registros_2024, registros_2025], ignore_index=True)

print("\nDataFrame completo com os registros de leituras de 2023, 2024 e 2025:")
print(df_registros)

# Exibe as primeiras 10 linhas do DataFrame
print(df_registros.head(10))  

#Exibe as últimas 10 linhas do DataFrame
print(df_registros.tail(10))

# Seleciona apenas a coluna "Título" do DataFrame
print("\nColuna 'Título' do DataFrame:")
print(df_registros["Título"])

# Seleciona apenas as colunas "Título" e "Páginas" do DataFrame
print("\nColunas 'Título' e 'Páginas' do DataFrame:")
print(df_registros[["Título", "Páginas"]])

# Seleciona apenas as linhas onde o autor é "Edir Macedo"
print("\nRegistros onde o autor é 'Edir Macedo':")
print(df_registros[df_registros["Autor"] == "Edir Macedo"])

# Usando .loc para selecionar linhas e colunas específicas
print("\nUsando .loc para selecionar linhas e colunas específicas:")
print(df_registros.loc[df_registros["Autor"] == "Edir Macedo", ["Título", "Páginas", "Ano"]])

# Filtra os registros onde o número de páginas é maior que 200
print("\nRegistros onde o número de páginas é maior que 200:")
print(df_registros[df_registros["Páginas"] > 200])

# Soma o total de páginas lidas em 2023
total_paginas_2023 = df_registros[df_registros["Ano"] == 2023]["Páginas"].sum()
print(f"\nTotal de páginas lidas em 2023: {total_paginas_2023}")

# Soma o total de páginas lidas em 2024
total_paginas_2024 = df_registros[df_registros["Ano"] == 2024]["Páginas"].sum()
print(f"Total de páginas lidas em 2024: {total_paginas_2024}")

# Soma o total de páginas lidas em 2025
total_paginas_2025 = df_registros[df_registros["Ano"] == 2025]["Páginas"].sum()
print(f"Total de páginas lidas em 2025: {total_paginas_2025}")  

# Soma o total de páginas lidas em todos os anos
total_paginas = df_registros["Páginas"].sum()
print(f"Total de páginas lidas em todos os anos: {total_paginas}")

#Soma o total de livros lidos em todos os anos
total_livros = df_registros.shape[0]
print(f"Total de livros lidos em todos os anos: {total_livros}")

#Vericando se há valores nulos no DataFrame
print("\nVerificando se há valores nulos no DataFrame:")
print(df_registros.isnull().sum())

# Verificando se há valores duplicados no DataFrame
print("\nVerificando se há valores duplicados no DataFrame:")
print(df_registros.duplicated().sum())

# Verificando o número de linhas e colunas
print("\nNúmeros de linhas e colunas:")
print(df_registros.shape)

# Verificando as informações gerais do DataFrame
print("\nInformações gerais do DataFrame:")
df_registros.info()

# Verificando as estatísticas descritivas do DataFrame
print("\nEstatísticas descritivas do DataFrame:")
print(df_registros.describe())

# Agrupando os registros por ano e total de livros lidos por ano
total_livros_por_ano = df_registros.groupby("Ano")["Título"].count()
print("\nTotal de livros lidos por ano:")
print(total_livros_por_ano)

# Tipo de dados da variável total_livros_por_ano
print("\nTipo de dados da variável total_livros_por_ano:")
print(type(total_livros_por_ano))

# Gráfico de barras do total de livros lidos por ano
plt.figure(figsize=(10, 6))
sns.barplot(x=total_livros_por_ano.index, y=total_livros_por_ano.values, palette="viridis")
plt.title("Total de livros lidos por ano")
plt.xlabel("Ano")
plt.ylabel("Total de livros lidos")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.savefig("graficos/total_livros_por_ano.png")
plt.show()

# Contagem de registros por autor com mais de um livro lido
contagem_livros = df_registros.groupby("Autor").size()
contagem_livros = contagem_livros[contagem_livros > 1]
print("\nContagem de registros por autor com mais de um livro lido:")
print(contagem_livros)

# Gráfico de pizza da contagem de registros por autor
plt.figure(figsize=(10, 6))
contagem_livros.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis')
plt.title("Contagem de registros por autor")
plt.ylabel("")
plt.tight_layout()
plt.savefig("graficos/contagem_registros_por_autor.png")
plt.show()
