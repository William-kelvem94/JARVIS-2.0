import os
import json
import subprocess
import sys

# Caminhos dos arquivos de configuração
google_cloud_path = r"C:\Users\willi\Documents\PROJETOS\JARVIS 2.0\core\config\voice\google-cloud.sample.json"
amazon_path = r"C:\Users\willi\Documents\PROJETOS\JARVIS 2.0\core\config\voice\amazon.sample.json"

# Função para alterar o idioma nos arquivos JSON
def update_json_language(file_path, language_code):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Alterando o idioma para o pt-BR
        if 'voice_language_code' in data:
            data['voice_language_code'] = language_code
        elif 'language_code' in data:
            data['language_code'] = language_code

        # Salvando as alterações no arquivo
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print(f"Arquivo {file_path} atualizado para o idioma {language_code}.")
    except Exception as e:
        print(f"Erro ao atualizar o arquivo {file_path}: {e}")

# Função para reiniciar a aplicação
def restart_application():
    print("Reiniciando a aplicação...")
    
    # Usando subprocess para reiniciar a aplicação (supondo que seja via comando)
    # Substitua o comando abaixo pelo que for necessário para reiniciar a aplicação.
    try:
        # Se você estiver usando Docker, pode usar docker-compose
        subprocess.run(["docker-compose", "down"], check=True)
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        print("Aplicação reiniciada com sucesso.")
    except Exception as e:
        print(f"Erro ao reiniciar a aplicação: {e}")

# Função principal que irá modificar os arquivos e reiniciar a aplicação
def main():
    # Atualizando arquivos Google Cloud e Amazon Polly
    update_json_language(google_cloud_path, 'pt-BR')
    update_json_language(amazon_path, 'pt-BR')

    # Reiniciando a aplicação
    restart_application()

if __name__ == "__main__":
    main()
