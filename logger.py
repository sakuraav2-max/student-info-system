import logging
from pathlib import Path

def get_logger(name=__name__):
    logs_dir = Path(__file__).resolve().parents[2] / 'logs'
    logs_dir.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(logs_dir / 'app.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
    return logger
