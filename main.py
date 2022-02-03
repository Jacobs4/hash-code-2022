from os import listdir
from os.path import isfile, join

from custom_parser import parse_dataset, Customer
from cost_function import naive_cost_function

if __name__ == '__main__':
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

    customer_1 = Customer(id=0, likes=["a", "b"], dislikes=["c"])
    customer_2 = Customer(id=1, likes=["a", "c"], dislikes=[])
    customer_3 = Customer(id=2, likes=["b"], dislikes=["c"])
    customers = [customer_1, customer_2, customer_3]

    pizza = ["a", "b"]
    print(naive_cost_function(pizza, customers))
