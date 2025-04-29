# core/brain/brain.py

from core.config.loader import load_entities, load_resolvers, load_skills_endpoints
from core.config.settings import DEFAULT_LANGUAGE
import random

class JarvisBrain:
    def __init__(self, language=DEFAULT_LANGUAGE):
        self.language = language
        self.entities = load_entities(language)
        self.resolvers = load_resolvers(language)
        self.skills = load_skills_endpoints()

    def process_input(self, user_input):
        """Processa a entrada do usuário e retorna a resposta do Jarvis"""
        # Primeiro, tentamos encontrar uma resposta nos resolvers globais (como negações, afirmações)
        response = self.resolve_input(user_input)
        
        # Se não encontramos, tentamos identificar entidades específicas no comando
        if not response:
            response = self.match_entities(user_input)
        
        # Se não encontrou nada, tenta buscar uma skill personalizada
        if not response:
            response = self.invoke_skill(user_input)
        
        # Se ainda assim não tiver resposta, retorna uma resposta genérica
        if not response:
            response = self.get_default_response()

        return response

    def resolve_input(self, user_input):
        """Resolve negações, afirmações e respostas genéricas."""
        for resolver_name, resolver in self.resolvers.items():
            for pattern, response in resolver.items():
                if pattern.lower() in user_input.lower():
                    return random.choice(response)  # Resposta aleatória se tiver múltiplas respostas

        return None

    def match_entities(self, user_input):
        """Tenta identificar as entidades no comando e responder"""
        for entity_name, entity_data in self.entities.items():
            for entity in entity_data:
                if entity['value'].lower() in user_input.lower():
                    return f"Entidade '{entity_name}' identificada: {entity['value']}."
        
        return None

    def invoke_skill(self, user_input):
        """Tenta invocar uma skill com base na entrada do usuário"""
        for skill_name, skill_endpoint in self.skills.items():
            if skill_name.lower() in user_input.lower():
                return self.execute_skill(skill_endpoint)
        
        return None

    def execute_skill(self, skill_endpoint):
        """Executa uma skill externa via seu endpoint"""
        # Aqui você poderia fazer chamadas HTTP ou invocar funções específicas para a skill
        return f"Executando skill: {skill_endpoint}"

    def get_default_response(self):
        """Retorna uma resposta padrão quando não há correspondência"""
        return "Desculpe, não entendi. Pode reformular?"

