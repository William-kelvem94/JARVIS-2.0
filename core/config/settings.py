# core/config/settings.py

import os

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminhos importantes
DATA_DIR = os.path.join(BASE_DIR, "data")
CONFIG_DIR = os.path.join(BASE_DIR, "config")

# Configurações de idiomas
LANGS_FILE = os.path.join(BASE_DIR, "langs.json")

# Configurações de skills (habilidades)
SKILLS_ENDPOINTS_FILE = os.path.join(BASE_DIR, "skills-endpoints.json")

# Diretórios de modelos
MODELS_DIR = os.path.join(DATA_DIR, "models")
WAKE_WORD_MODELS_DIR = os.path.join(MODELS_DIR, "audio", "wake_word")
TTS_MODELS_DIR = os.path.join(MODELS_DIR, "audio", "tts")
ASR_MODELS_DIR = os.path.join(MODELS_DIR, "audio", "asr")

# Configurações adicionais
DEFAULT_LANGUAGE = "pt"

# Debug
DEBUG = True

# Definir o serviço de voz padrão (pode ser 'google-cloud', 'watson', etc.)
VOICE_SERVICE = "google-cloud"
