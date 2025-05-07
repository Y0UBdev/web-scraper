import re

def replaceWithUnderscore(text: str) -> str:
    text = text.replace(" ", "_")
    return re.sub(r'[^\w\-]', '_', text)