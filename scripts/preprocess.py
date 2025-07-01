

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from utils.helpers import clean_text
from config import Config
from utils.logger import get_logger


logger = get_logger("preprocess")

def preprocess_data(input_path, output_path):
    logger.info(f"Loading raw data from: {input_path}")
    df = pd.read_csv(input_path)

    logger.info("Cleaning abstracts and titles...")
    df['cleaned_title'] = df['title'].apply(clean_text)
    df['cleaned_abstract'] = df['abstract'].apply(clean_text)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    logger.info(f"Processed data saved to: {output_path}")

if __name__ == "__main__":
    raw_file = os.path.join(Config.RAW_DATA, "sample_raw.csv")
    processed_file = os.path.join(Config.PROCESSED_DATA, "processed.csv")
    preprocess_data(raw_file, processed_file)
