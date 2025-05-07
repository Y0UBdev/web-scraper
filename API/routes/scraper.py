import os
from flask import Blueprint, request, jsonify, send_file
from datetime import datetime

from API.utils.folder_name import generate_folder_name
from Domains.controller.WebScraper import WebScraper
from Domains.services.extract_data import extract_data
from Domains.services.saving_to_file import save_to_file
from Domains.utils.compress_folder import compress_folder

scrape_bp = Blueprint("scrape", __name__)


@scrape_bp.route("/scrape", methods=["POST"])
def scrape():
    
    url = request.form.get("url")
    print(request.form)
    lang = request.form.get("lang", "").strip()
    custom_name = request.form.get("name", "").strip()

    if not url:
        return jsonify({"error": "L'URL est manquante."}), 400

    scraper = WebScraper(url, lang)

    if not scraper.validate_url() or not scraper.fetch_page():
        return jsonify({"error": "URL invalide ou inaccessible."}), 400

    base_folder = generate_folder_name(custom_name)
    os.makedirs(base_folder, exist_ok=True)

    result = extract_data(scraper.get_soup(), scraper.get_url(), base_folder)
    save_to_file(result, base_folder)
    zip_path = compress_folder(base_folder)

    return jsonify({
        "message": "Scraping terminé",
        "zip_file": zip_path
    }), 200
