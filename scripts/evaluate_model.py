
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from models.abstract_generator import AbstractGenerator
from utils.metrics import compute_rouge, compute_bleu
from utils.logger import get_logger
from config import Config
import torch

logger = get_logger("evaluate")

def evaluate():
    logger.info("Loading processed data...")
    df = pd.read_csv(os.path.join(Config.PROCESSED_DATA, "processed.csv"))
    sample_size = min(50, len(df))
    sample_df = df.sample(n=sample_size, random_state=Config.RANDOM_SEED)


    model_obj = AbstractGenerator()
    model_obj.model.load_state_dict(torch.load(Config.CHECKPOINT_PATH, map_location=Config.DEVICE))
    model_obj.model.eval()

    logger.info("Generating abstracts for evaluation...")
    predictions = []
    references = sample_df['cleaned_abstract'].tolist()

    for _, row in sample_df.iterrows():
        text = row['cleaned_title'] + " " + row['keywords']
        pred = model_obj.generate(text)
        predictions.append(pred)

    rouge = compute_rouge(predictions, references)
    bleu = compute_bleu(predictions, references)

    logger.info(f"ROUGE-1: {rouge['rouge1']:.4f}")
    logger.info(f"ROUGE-L: {rouge['rougeL']:.4f}")
    logger.info(f"BLEU: {bleu:.2f}")

if __name__ == "__main__":
    evaluate()
