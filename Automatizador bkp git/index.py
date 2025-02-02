from datetime import datetime
import sys
import subprocess
import os
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
    if len(sys.argv) != 3:
        print("Uso: python script.py <caminho_da_pasta> <mensagem_de_commit>")
    else:
        folder_path = sys.argv[1]
        commit_message = sys.argv[2]
        git_push(folder_path, commit_message)

# Comparar data atual com o ultimo check
def verificar_ultimocheck():
    if verificar_dia_atual > ultima_data:
        print("OI")  #codigo bkp
    elif verificar_dia_atual == ultima_data:
        print("OI") #verificar se vai haver atualizações no dia, estimar tempo para bkp