import os
import sys
import subprocess
from datetime import datetime

ultima_data = "2025-02-02"

# Obtém a data e hora atual ( testado ok)
def verificar_dia_atual():
    data = datetime.now()
    # Formata a data atual no formato desejado (ex: YYYY-MM-DD)
    data_atual = data.strftime("%d-%m-%Y")
    return data_atual



def git_push(folder_path, commit_message):
    try:
        # Mudar para o diretório da pasta especificada
        os.chdir(folder_path)

        # Adicionar todas as alterações ao repositório Git
        subprocess.run(["git", "add", "."], check=True)

        # Fazer commit das alterações com a mensagem especificada
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Fazer push das alterações para o repositório remoto
        subprocess.run(["git", "push"], check=True)

        print("Upload para o Git concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    # Defina o caminho da pasta e a mensagem de commit diretamente no código
    folder_path = "D:\Projetos\Projeto teste"
    commit_message = verificar_dia_atual()
    
    git_push(folder_path, commit_message)
