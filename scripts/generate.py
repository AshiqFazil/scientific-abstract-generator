
import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import torch
from models.abstract_generator import AbstractGenerator
from config import Config
from utils.logger import get_logger

logger = get_logger("generate")

def clean_input(title, keywords, domain):
    
    title_clean = " ".join(dict.fromkeys(title.strip().split()))
    keywords_list = [kw.strip() for kw in keywords.split(",")]
    keywords_unique = list(dict.fromkeys(keywords_list))
    keywords_str = ", ".join(keywords_unique)
    domain_clean = domain.strip() or "general"

    # Build clean prompt
    return f"{title_clean}. Keywords: {keywords_str}. Domain: {domain_clean}"

def remove_repetitions(text):
    
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', text)

def polish(text):
    
    text = text.strip()
    if text and not text.endswith('.'):
        text += '.'
    return text[0].upper() + text[1:] if text else text

class AbstractGeneratorService:
    def __init__(self):
        self.model_obj = AbstractGenerator()
        if os.path.exists(Config.CHECKPOINT_PATH):
            self.model_obj.model.load_state_dict(torch.load(Config.CHECKPOINT_PATH, map_location=Config.DEVICE))
            self.model_obj.model.eval()
            logger.info("Model loaded successfully for generation.")
        else:
            logger.error(f"Checkpoint not found at {Config.CHECKPOINT_PATH}")
            raise FileNotFoundError("Model checkpoint missing!")

    def generate_abstract(self, title, keywords, domain="general"):
        
        input_text = clean_input(title, keywords, domain)
        logger.info(f"Cleaned input for generation: {input_text}")

        raw_abstract = self.model_obj.generate(input_text)
        logger.info(f"Raw generated abstract: {raw_abstract}")

        clean_abstract = remove_repetitions(raw_abstract)
        polished_abstract = polish(clean_abstract)

        logger.info(f"Polished abstract: {polished_abstract}")
        return polished_abstract

def interactive_generate():
    service = AbstractGeneratorService()
    logger.info("Interactive generation started.")

    while True:
        title = input("\nEnter Title (or 'exit' to quit): ").strip()
        if title.lower() == "exit":
            break
        keywords = input("Enter Keywords (comma-separated): ").strip()
        domain = input("Enter Domain (optional): ").strip() or "general"

        abstract = service.generate_abstract(title, keywords, domain)
        print("\n🔹 Generated Abstract:\n", abstract)

if __name__ == "__main__":
    interactive_generate()
