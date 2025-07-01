
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from generate import AbstractGeneratorService

from utils.logger import get_logger

logger = get_logger("web_app")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

app = Flask(__name__,
            template_folder=os.path.join(ROOT_DIR, "templates"),
            static_folder=os.path.join(ROOT_DIR, "static"))

CORS(app)

generator_service = AbstractGeneratorService()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    title = data.get("title", "")
    keywords = data.get("keywords", "")
    domain = data.get("domain", "general")

    if not title or not keywords:
        logger.warning("Missing required fields.")
        return jsonify({"error": "Missing title or keywords"}), 400

    abstract = generator_service.generate_abstract(title, keywords, domain)
    logger.info("Abstract generated successfully.")
    return jsonify({"abstract": abstract})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
