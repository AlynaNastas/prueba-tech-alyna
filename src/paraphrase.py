# src/paraphrase.py

import sys
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def paraphrase_file(path: str):
    try:
        if not os.path.isfile(path):
            print(f"El archivo '{path}' no existe.")
            sys.exit(1)

        with open(path, 'r', encoding='utf-8') as file:
            texto = file.read()

        response = openai.completions.create(
            model="gpt-4o-mini",
            prompt=f"Parafrasea el siguiente texto:\n\n{texto}",
            temperature=0.7,
            max_tokens=500
        )

        parafraseado = response['choices'][0]['text'].strip()

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
