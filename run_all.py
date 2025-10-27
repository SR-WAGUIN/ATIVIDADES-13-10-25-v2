import os
import subprocess

BASE_DIR = os.path.dirname(__file__)
FULL_DIR = os.path.join(BASE_DIR, "full_version")

print("🎬 Executando o sistema completo de avaliação de filmes...\n")

main_script = os.path.join(FULL_DIR, "main.py")
subprocess.run(["python", main_script])

print("\n✅ Processo completo finalizado!")
