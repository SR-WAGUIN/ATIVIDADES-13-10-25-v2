import os

# === Diretórios base ===
base_dir = "projeto_filmes"
dirs = [
    f"{base_dir}/data",
    f"{base_dir}/src",
    f"{base_dir}/full_version",
]

# Cria os diretórios
for d in dirs:
    os.makedirs(d, exist_ok=True)

# === Conteúdo dos arquivos ===
arquivos = {
    f"{base_dir}/data/filmes.csv": """Ano,Título
1982,TRON
1983,WarGames
1995,Hackers
1999,Pirates of Silicon Valley
2010,The Social Network
2013,Jobs
2014,The Imitation Game
2014,Ex Machina
2016,Snowden
2018,Ready Player One
""",

    f"{base_dir}/src/avaliacao.py": """import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENTRADA = os.path.join(BASE_DIR, "data", "filmes.csv")
SAIDA = os.path.join(BASE_DIR, "data", "filmes_avaliacao.csv")

def avaliar_filmes():
    filmes = []

    with open(ENTRADA, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filmes.append(row)

    for filme in filmes:
        while True:
            try:
                nota = float(input(f"Digite a nota (0 a 10) para '{filme['Título']}': "))
                if 0 <= nota <= 10:
                    filme["Nota"] = nota
                    break
                else:
                    print("⚠️  A nota deve estar entre 0 e 10.")
            except ValueError:
                print("⚠️  Digite um número válido.")

    with open(SAIDA, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["Ano", "Título", "Nota"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filmes)

    print(f"\\n✅ Arquivo '{SAIDA}' criado com sucesso!")

if __name__ == "__main__":
    avaliar_filmes()
""",

    f"{base_dir}/src/indicacao.py": """import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENTRADA = os.path.join(BASE_DIR, "data", "filmes_avaliacao.csv")
SAIDA = os.path.join(BASE_DIR, "data", "filmes_indicacao.csv")

def gerar_indicacoes():
    filmes = []

    with open(ENTRADA, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Nota"] = float(row["Nota"])
            filmes.append(row)

    filmes_ordenados = sorted(filmes, key=lambda x: (-x["Nota"], x["Título"]))
    top5 = filmes_ordenados[:5]

    with open(SAIDA, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["Ano", "Título", "Nota"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(top5)

    print(f"✅ Arquivo '{SAIDA}' criado com sucesso!")

if __name__ == "__main__":
    gerar_indicacoes()
""",

    f"{base_dir}/src/top_filmes.py": """import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENTRADA = os.path.join(BASE_DIR, "data", "filmes_indicacao.csv")

def mostrar_top_filmes():
    filmes = []

    with open(ENTRADA, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Nota"] = float(row["Nota"])
            filmes.append(row)

    filmes.sort(key=lambda x: x["Nota"], reverse=True)

    print("\\n🎥 TOP FILMES RECOMENDADOS 🎥")
    print("-" * 45)
    for filme in filmes:
        print(f"{filme['Título']} ({filme['Ano']}) — Nota: {filme['Nota']}")
    print("-" * 45)

if __name__ == "__main__":
    mostrar_top_filmes()
""",

    f"{base_dir}/full_version/main.py": """import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

FILMES = os.path.join(DATA_DIR, "filmes.csv")
AVALIACAO = os.path.join(DATA_DIR, "filmes_avaliacao.csv")
INDICACAO = os.path.join(DATA_DIR, "filmes_indicacao.csv")

def avaliar_filmes():
    filmes = []
    with open(FILMES, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filmes.append(row)

    for filme in filmes:
        while True:
            try:
                nota = float(input(f"Digite a nota (0 a 10) para '{filme['Título']}': "))
                if 0 <= nota <= 10:
                    filme["Nota"] = nota
                    break
                else:
                    print("⚠️  A nota deve estar entre 0 e 10.")
            except ValueError:
                print("⚠️  Digite um número válido.")

    with open(AVALIACAO, "w", newline='', encoding="utf-8") as csvfile:
        fieldnames = ["Ano", "Título", "Nota"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filmes)

def gerar_indicacoes():
    filmes = []
    with open(AVALIACAO, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Nota"] = float(row["Nota"])
            filmes.append(row)

    top5 = sorted(filmes, key=lambda x: (-x["Nota"], x["Título"]))[:5]

    with open(INDICACAO, "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Ano", "Título", "Nota"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(top5)

def mostrar_top_filmes():
    filmes = []
    with open(INDICACAO, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Nota"] = float(row["Nota"])
            filmes.append(row)

    filmes.sort(key=lambda x: x["Nota"], reverse=True)

    print("\\n🎥 TOP FILMES RECOMENDADOS 🎥")
    print("-" * 45)
    for filme in filmes:
        print(f"{filme['Título']} ({filme['Ano']}) — Nota: {filme['Nota']}")
    print("-" * 45)

if __name__ == "__main__":
    print("=== Sistema de Avaliação de Filmes ===")
    avaliar_filmes()
    gerar_indicacoes()
    mostrar_top_filmes()
""",

    f"{base_dir}/run_all.py": """import os
import subprocess

BASE_DIR = os.path.dirname(__file__)
FULL_DIR = os.path.join(BASE_DIR, "full_version")

print("🎬 Executando o sistema completo de avaliação de filmes...\\n")

main_script = os.path.join(FULL_DIR, "main.py")
subprocess.run(["python", main_script])

print("\\n✅ Processo completo finalizado!")
"""
}

# Cria todos os arquivos
for path, content in arquivos.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Projeto criado com sucesso na pasta 'projeto_filmes'!")


