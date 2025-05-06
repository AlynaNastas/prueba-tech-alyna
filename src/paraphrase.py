# src/paraphrase.py
import sys
import openai


def paraphrase_file(path: str):
    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python src/paraphrase.py <input.txt>')
        sys.exit(1)
    paraphrase_file(sys.argv[1])
