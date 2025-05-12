# src/paraphrase.py

import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: Falta la variable OPENAI_API_KEY en el archivo .env")
    sys.exit(1)

# Inicializar cliente moderno
client = OpenAI(api_key=api_key)

def paraphrase_file(path: str):
    if not os.path.isfile(path):
        print(f"El archivo '{path}' no existe.")
        sys.exit(1)

    with open(path, 'r', encoding='utf-8') as file:
        texto = file.read()

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente que parafrasea textos en español."},
                {"role": "user", "content": f"Parafrasea el siguiente texto:\n\n{texto}"}
            ],
            temperature=0.7,
            max_tokens=500
        )

        parafraseado = response.choices[0].message.content.strip()
        print("\nTexto parafraseado:\n")
        print(parafraseado)

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python src/paraphrase.py <input.txt>')
        sys.exit(1)
    paraphrase_file(sys.argv[1])
