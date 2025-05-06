# project/src/utils.py

def clean_data(row: dict) -> dict:
    # Limpia campos, elimina espacios, etc.
    return {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}

def validate_row(row: dict) -> bool:
    # Validación básica de datos
    return all(v is not None and v != '' for v in row.values())
