import os
import requests
import mimetypes
from datetime import datetime
from urllib.parse import urljoin, unquote
from Domains.utils.replace_str import replaceWithUnderscore


def download_images(soup, url, base_folder) -> list:
    img_tags = soup.find_all("img", src=True)
    img_urls = [urljoin(url, img['src']) for img in img_tags]

    image_folder = os.path.join(base_folder, "images")
    os.makedirs(image_folder, exist_ok=True)

    downloaded_files = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for index, img_url in enumerate(img_urls):
        decoded_url = unquote(img_url)
        if "_next/image" in decoded_url:
            print(f"[+] Image Next.js optimisée détectée : {decoded_url}")

        try:
            response = requests.get(decoded_url, stream=True, timeout=10, headers=headers)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            extension = mimetypes.guess_extension(content_type.split(";")[0]) or ".jpg"

            filename = f"image_{index+1}{extension}"
            filepath = os.path.join(image_folder, filename)

            with open(filepath, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            downloaded_files.append(filepath)
            print(f"[✔] Image téléchargée: {filepath}")
        except Exception as e:
            print(f"[!] Erreur lors du téléchargement de {decoded_url}: {e}")

    return downloaded_files
