import os
from datetime import datetime
from Domains.utils.replace_str import replaceWithUnderscore

def generate_folder_name(name: str) -> str:
    name = replaceWithUnderscore(name if name else "scrape")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = os.path.join("Temp", f"{name}_{timestamp}")
    return folder
