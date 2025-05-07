
from Domains.services.download_images import download_images
from bs4 import Comment


def extract_data(soup, url, base_folder) -> dict:
    if not soup:
        print("[Erreur] La page n'a pas été chargée.")
        return {}

    images = download_images(soup, url, base_folder)

    all_text = extract_all_text(soup)

    data = {
        "URL": url,
        "Titre": soup.title.string.strip() if soup.title else "Aucun titre",
        "Description": get_meta_description(soup),
        "Liens": [a['href'] for a in soup.find_all('a', href=True)],
        "Images": images,
        "Texte": all_text 
    }

    return data


def extract_all_text(soup) -> str:
    for tag in soup(['script', 'style', 'head', 'meta', 'noscript', 'footer', 'header', 'link', 'nav']):
        tag.decompose()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    lines = []

    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']):
        text = element.get_text(strip=True)
        if not text:
            continue

        tag = element.name
        if tag.startswith('h'):
            level = int(tag[1])
            prefix = "#" * level  
            lines.append(f"\n{prefix} {text}\n")
        elif tag == 'li':
            lines.append(f"- {text}")
        else:  # p, etc.
            lines.append(text)

    return "\n".join(lines)


def get_meta_description(soup) -> str:
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        return meta["content"].strip()
    return "Aucune description"