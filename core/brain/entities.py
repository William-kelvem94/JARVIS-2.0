# core/brain/entities.py

def load_entities(language):
    """Carrega as entidades globais para o idioma"""
    # Usando o loader que já fizemos anteriormente
    from core.config.loader import load_entities
    return load_entities(language)
