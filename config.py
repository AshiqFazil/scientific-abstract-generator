
import os

class Config:
    DATA_DIR = "data/"
    RAW_DATA = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA = os.path.join(DATA_DIR, "processed")
    MODEL_DIR = "models/"
    CHECKPOINT_PATH = os.path.join(MODEL_DIR, "abstract_gen_checkpoint.pt")
    LOG_DIR = "logs/"

   
    PRETRAINED_MODEL = "t5-small"
    MAX_INPUT_LENGTH = 512
    MAX_TARGET_LENGTH = 150
    BATCH_SIZE = 8
    EPOCHS = 5
    LEARNING_RATE = 5e-5

   
    RANDOM_SEED = 42
    DEVICE = "cuda" if os.environ.get("CUDA_AVAILABLE") == "true" else "cpu"
