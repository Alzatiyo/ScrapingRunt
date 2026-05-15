import json
import os
import sys

def get_base_path():
    # Cuando corre como ejecutable
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    # Cuando corre como script
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_PATH = get_base_path()
CONFIG_PATH = os.path.join(BASE_PATH, "config.json")

# Verificar si existe el config
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"No se encontró config.json en: {CONFIG_PATH}")

# Cargar configuración
with open(CONFIG_PATH, "r", encoding="utf-8-sig") as f:
    config = json.load(f)

# Variables
ANTICAPTCHA_KEY = config.get("ANTICAPTCHA_KEY")
TIPO_DOC = config.get("TIPO_DOC")
URL = config.get("URL")

DB_CONFIG = config.get("DB_CONFIG", {})
HEADERS = config.get("HEADERS", {})