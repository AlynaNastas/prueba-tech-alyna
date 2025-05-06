# project/src/main.py

import csv
from api_client import ApiClient
from utils import clean_data, validate_row

def main(path):
    client = ApiClient()
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clean = clean_data(row)
            if validate_row(clean):
                client.post_data(clean)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Uso: python main.py <data.csv>')
        sys.exit(1)
    main(sys.argv[1])
