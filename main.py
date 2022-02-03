from os import listdir
from os.path import isfile, join

from code import parse_dataset

DATASETS_PATH = "input-data/"
DATASETS = [DATASETS_PATH + f for f in listdir(DATASETS_PATH) if isfile(join(DATASETS_PATH, f))]

# sanity check
for i, dataset in enumerate(DATASETS[:3]):
    customers = parse_dataset(dataset)
    print(f"DATASET #{i}")
    print("-" * 40)
    for customer in customers:
        print(customer)
    print("-" * 40)
