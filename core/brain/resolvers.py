# core/brain/resolvers.py

def load_resolvers():
    """Carrega resolvers básicos como afirmações e negações"""
    return {
        "affirmation": {
            "yes": ["Sim", "Claro", "Com certeza", "Está certo!"],
            "okay": ["Ok", "Beleza", "Combinado"],
        },
        "denial": {
            "no": ["Não", "De jeito nenhum", "Nem pensar", "Não mesmo"],
            "not": ["Isso não vai acontecer", "De forma alguma"],
        },
    }
