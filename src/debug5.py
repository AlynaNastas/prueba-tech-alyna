# src/debug5.py

import json

def load_items(path):
    with open(path) as f:
        data = json.load(f)
    return data["items_list"]

def mean(nums):
    if len(nums) == 0:  # Comprobamos que la lista no esté vacía, para que no dividamos entre cero.
        print("Error: La lista está vacía") # Mostramos el error por consola.
        sys.exit(1) # Empleamos el código estándar de error para la salida de la función.
    total = sum(nums)
    return total / len(nums)


def scale(values):
    m = mean(values)
    return [v * m for v in values]

def top_n(values, n):
    vals = sorted(values, reverse=False)
    return vals[n]

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    n = int(sys.argv[2])
    items = load_items(path)
    scaled = scale(items)
    result = top_n(scaled, n)
    print(json.dumps({"result": result}))
