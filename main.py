import os
from datetime import datetime
from Domains.controller.WebScraper   import WebScraper
from Domains.services.extract_data   import extract_data
from Domains.services.saving_to_file import save_to_file
from Domains.utils.replace_str       import replaceWithUnderscore
from Domains.utils.compress_folder   import compress_folder


def ask_folder_name() -> str:
    while True:
        folder_name = input("Nom du dossier de sauvegarde (titre ou mot-clé) : ").strip()
        folder_name = replaceWithUnderscore(folder_name)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_path = os.path.join("uploads", f"{folder_name}_{timestamp}")

        if os.path.exists(full_path):
            choix = input(f"[!] Le dossier '{full_path}' existe déjà. Écraser ? (o/n) : ").lower()
            if choix == 'o':
                return full_path
            else:
                print("Veuillez entrer un autre nom.")
        else:
            return full_path


if __name__ == "__main__":
    url = input("Entrez l'URL à scrapper : ").strip()
    lang = input("Langue souhaitée (ex: fr, en, de) [défaut site] : ").strip()

    scraper = WebScraper(url, lang)

    if scraper.validate_url() and scraper.fetch_page():
        base_folder = ask_folder_name()
        result = extract_data(scraper.get_soup(), scraper.get_url(), base_folder)
        save_to_file(result, base_folder)
    else:
        print("URL invalide ou page inaccessible.")