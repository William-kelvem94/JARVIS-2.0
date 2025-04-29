# core/voice.py

import pyttsx3
from core.config.loader import load_voice_config

class VoiceOutput:
    def __init__(self, service_name="google-cloud"):
        self.engine = pyttsx3.init()
        self.tts_config = load_voice_config(service_name)  # Carrega a configuração de TTS
        # Aqui você pode adicionar mais lógica se necessário para usar o TTS de um serviço específico

    def speak(self, text):
        """Faz o Jarvis falar o texto"""
        print(f"Jarvis diz: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
