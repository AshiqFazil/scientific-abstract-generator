
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import torch
from torch.utils.data import DataLoader, Dataset
from torch.optim import AdamW
from transformers import get_linear_schedule_with_warmup


from config import Config
from models.abstract_generator import AbstractGenerator
from utils.logger import get_logger
import pandas as pd
from tqdm import tqdm

logger = get_logger("train")

class AbstractDataset(Dataset):
    def __init__(self, df, tokenizer):
        self.inputs = df['cleaned_title'] + " " + df['keywords']
        self.targets = df['cleaned_abstract']
        self.tokenizer = tokenizer

    def __len__(self): return len(self.inputs)

    def __getitem__(self, idx):
        source = self.tokenizer(
            self.inputs.iloc[idx],
            max_length=Config.MAX_INPUT_LENGTH,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )
        target = self.tokenizer(
            self.targets.iloc[idx],
            max_length=Config.MAX_TARGET_LENGTH,
            truncation=True,
            padding="max_length",
            return_tensors="pt"
        )
        return {
            "input_ids": source["input_ids"].squeeze(),
            "attention_mask": source["attention_mask"].squeeze(),
            "labels": target["input_ids"].squeeze()
        }

def train():
    logger.info("Loading processed data...")
    df = pd.read_csv(os.path.join(Config.PROCESSED_DATA, "processed.csv"))

    logger.info("Preparing dataset & dataloader...")
    model_obj = AbstractGenerator()
    dataset = AbstractDataset(df, model_obj.tokenizer)
    dataloader = DataLoader(dataset, batch_size=Config.BATCH_SIZE, shuffle=True)

    optimizer = AdamW(model_obj.model.parameters(), lr=Config.LEARNING_RATE)
    total_steps = len(dataloader) * Config.EPOCHS
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    model_obj.model.train()
    logger.info("Starting training...")

    for epoch in range(Config.EPOCHS):
        total_loss = 0
        loop = tqdm(dataloader, desc=f"Epoch {epoch+1}/{Config.EPOCHS}")
        for batch in loop:
            input_ids = batch["input_ids"].to(Config.DEVICE)
            attention_mask = batch["attention_mask"].to(Config.DEVICE)
            labels = batch["labels"].to(Config.DEVICE)

            outputs = model_obj.model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                labels=labels
            )

            loss = outputs.loss
            total_loss += loss.item()

            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()

            loop.set_postfix(loss=loss.item())

        avg_loss = total_loss / len(dataloader)
        logger.info(f"Epoch {epoch+1}: Average Loss = {avg_loss:.4f}")

    os.makedirs(Config.MODEL_DIR, exist_ok=True)
    torch.save(model_obj.model.state_dict(), Config.CHECKPOINT_PATH)
    logger.info(f"Training finished. Model saved to: {Config.CHECKPOINT_PATH}")

if __name__ == "__main__":
    train()
