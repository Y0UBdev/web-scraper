# Web Scraper

A web scraping tool that extracts data from web pages. Can be used via command line or REST API.

## Features

- Extract page title and meta description
- Extract all text content (headings, paragraphs, list items)
- Extract all links from the page
- Download all images from the page
- Support for custom language headers
- Export data to text files
- Compress results to ZIP

## Installation

### CLI

```bash
pip install -r Domains/requirements.txt
```

### API

```bash
pip install -r Domains/requirements.txt
pip install -r API/requirements.txt
```

## Usage

### Command Line Interface

```bash
python main.py
```

Enter the URL to scrape and optionally specify a language (e.g., `fr`, `en`, `de`).

The scraped data will be saved in the `uploads/` folder with the following structure:
```
uploads/<folder_name>/
    texte.txt
    liens.txt
    images.txt
    meta.txt
    images/
```

### REST API

Start the Flask server:

```bash
python API/app.py
```

The API will be available at `http://localhost:5000`.

#### Endpoints

**POST /api/scrape**

Scrape a web page.

Parameters (form-data):
- `url` (required): URL of the page to scrape
- `lang` (optional): Language code (e.g., `fr`, `en`)
- `name` (optional): Custom folder name for the output
- `format` (optional): Output format (`txt`, default: `txt`)

Response:
```json
{
    "message": "Scraping terminé",
    "zip_file": "path/to/output.zip"
}
```

Example with curl:
```bash
curl -X POST http://localhost:5000/api/scrape \
    -F "url=https://example.com" \
    -F "lang=en" \
    -F "name=my_scraped_data"
```

## Project Structure

```
web-scraper/
    main.py                 # CLI entry point
    Domains/
        controller/
            WebScraper.py   # Core scraper class
        services/
            extract_data.py     # Data extraction logic
            download_images.py  # Image downloading
            saving_to_file.py   # File writing
        utils/
            replace_str.py      # String utilities
            compress_folder.py  # ZIP compression
        requirements.txt
    API/
        app.py              # Flask application
        routes/
            scraper.py      # API endpoints
        requirements.txt
```

## Requirements

- Python 3.8+
- beautifulsoup4
- requests
- flask (for API)
