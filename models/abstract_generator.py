
from transformers import T5Tokenizer, T5ForConditionalGeneration
from config import Config

class AbstractGenerator:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained(Config.PRETRAINED_MODEL)
        self.model = T5ForConditionalGeneration.from_pretrained(Config.PRETRAINED_MODEL)
        self.model.to(Config.DEVICE)

    def encode(self, text, max_length=Config.MAX_INPUT_LENGTH):
        return self.tokenizer(
            text, truncation=True, padding="max_length", max_length=max_length, return_tensors="pt"
        )

    def generate(self, input_text, max_length=Config.MAX_TARGET_LENGTH):
        inputs = self.encode(input_text)
        inputs = {k: v.to(Config.DEVICE) for k, v in inputs.items()}
        summary_ids = self.model.generate(**inputs, max_length=max_length, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
