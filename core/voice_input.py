# core/voice_input.py

from core.config.settings import VOICE_SERVICE
from core.config.loader import load_voice_config

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.config = load_voice_config(VOICE_SERVICE)  # Carrega a configuração do serviço de voz
        self.client = speech.SpeechClient()

    def listen(self):
        """Escuta o áudio do usuário e retorna o texto reconhecido"""
        with self.microphone as source:
            print("Escutando...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            # Reconhecimento de fala usando o serviço de voz configurado
            audio_content = audio.get_wav_data()
            response = self.client.recognize(config=self.config, audio={'content': audio_content})
            
            if response.results:
                user_input = response.results[0].alternatives[0].transcript
                print(f"Você disse: {user_input}")
                return user_input
            return None
        except Exception as e:
            print(f"Erro no reconhecimento de fala: {e}")
            return None
