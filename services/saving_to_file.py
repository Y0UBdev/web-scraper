import os
from datetime import datetime
from utils.replace_str import replaceWithUnderscore
from utils.compress_folder import compress_folder

def save_to_file(data: dict, base_folder: str):
    os.makedirs(base_folder, exist_ok=True)

    with open(os.path.join(base_folder, "meta.txt"), "w", encoding="utf-8") as f:
        f.write(f"URL: {data['URL']}\n")
        f.write(f"Titre: {data['Titre']}\n")
        f.write(f"Description: {data['Description']}\n")
        f.write(f"Nombre de liens: {len(data['Liens'])}\n")
        f.write(f"Nombre d'images: {len(data['Images'])}\n")

    with open(os.path.join(base_folder, "texte.txt"), "w", encoding="utf-8") as f:
        f.write(data["Texte"])

    with open(os.path.join(base_folder, "liens.txt"), "w", encoding="utf-8") as f:
        for link in data["Liens"]:
            f.write(link + "\n")

    with open(os.path.join(base_folder, "images.txt"), "w", encoding="utf-8") as f:
        for path in data["Images"]:
            f.write(path + "\n")

    print(f"[✔] Données sauvegardées dans le dossier: {base_folder}")
    
    
