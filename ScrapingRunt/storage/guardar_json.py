import json
from datetime import datetime

def guardar_json(todos_resultados):

    nombre = f"runt_resultados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(nombre, "w", encoding="utf-8") as f:
        json.dump(todos_resultados, f, ensure_ascii=False, indent=2)

    print(f"\n  JSON guardado: {nombre}")

    return nombre