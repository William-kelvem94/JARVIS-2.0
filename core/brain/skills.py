# core/brain/skills.py

def invoke_skill(skill_name):
    """Invoca a skill baseada no nome ou endpoint"""
    from core.config.loader import load_skills_endpoints
    skills = load_skills_endpoints()

    if skill_name in skills:
        return f"Executando skill: {skills[skill_name]}"
    return "Skill não encontrada!"
