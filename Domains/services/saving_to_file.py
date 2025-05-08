import os
from datetime import datetime
from Domains.utils.replace_str import replaceWithUnderscore
from Domains.utils.compress_folder import compress_folder

import json

def save_to_file(data: dict, base_folder: str, format_type: str = "txt"):
    os.makedirs(base_folder, exist_ok=True)

    with open(os.path.join(base_folder, "meta.txt"), "w", encoding="utf-8") as f:
        f.write(f"URL: {data['URL']}\n")
        f.write(f"Titre: {data['Titre']}\n")
        f.write(f"Description: {data['Description']}\n")
        f.write(f"Nombre de liens: {len(data['Liens'])}\n")
        f.write(f"Nombre d'images: {len(data['Images'])}\n")

    if format_type == "json":
        with open(os.path.join(base_folder, "texte.json"), "w", encoding="utf-8") as f:
            json.dump({"texte": data["Texte"]}, f, indent=4, ensure_ascii=False)
    else:
        with open(os.path.join(base_folder, "texte.txt"), "w", encoding="utf-8") as f:
            f.write(data["Texte"])

    with open(os.path.join(base_folder, "liens.txt"), "w", encoding="utf-8") as f:
        for link in data["Liens"]:
            f.write(link + "\n")

    with open(os.path.join(base_folder, "images.txt"), "w", encoding="utf-8") as f:
        for path in data["Images"]:
            f.write(path + "\n")

    print(f"[✔] Données sauvegardées dans le dossier: {base_folder}")

