import json
from pathlib import Path

def load_config(path=None):
    cfg_path = Path(path or (Path(__file__).resolve().parents[2] / 'config' / 'config.json'))
    if not cfg_path.exists():
        return {}
    with open(cfg_path, 'r', encoding='utf-8') as f:
        return json.load(f)
