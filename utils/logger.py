
import logging
import os

def get_logger(name: str):
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(f"logs/{name}.log", mode='a')
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger
