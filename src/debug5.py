# src/debug5.py

import json

def load_items(path):
    with open(path) as f:
        data = json.load(f)
    return data["items_list"]

def mean(nums):
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
