
from flask import Flask
from API.routes.scraper import scrape_bp

app = Flask(__name__)
app.register_blueprint(scrape_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
