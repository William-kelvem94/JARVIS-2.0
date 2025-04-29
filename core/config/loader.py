# core/config/loader.py

def load_voice_config(service_name="google-cloud"):
    """Carrega as configurações de voz para o serviço especificado."""
    file_path = f"core/config/voice/{service_name}.sample.json"
    return load_json(file_path)
