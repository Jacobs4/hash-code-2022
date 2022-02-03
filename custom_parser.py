from dataclasses import dataclass, field
from typing import List


@dataclass
class Customer:
    id: int
    likes: List[str] = field(default_factory=list)
    dislikes: List[str] = field(default_factory=list)


def parse_dataset(dataset_path: str) -> List[Customer]:
    """Parses a dataset into a list of handy Customer objects.

    Args:
        dataset_path: relative path to the dataset file.

    Returns:
        List of Customer objects.

    """
    with open(dataset_path, "r") as f:
        customers: List[Customer] = list()
        # skips the first line since we don't really need to know how many customers there are
        lines = f.readlines()[1::]
        # the even indexed lines are ingredients that a customer likes and the odd ones contain those he dislikes
        for cid, (likes_line, dislikes_line) in enumerate(zip(lines[::2], lines[1::2])):
            # skips the number of products number and removes unnecessary whitespace
            likes = [like.strip() for like in likes_line.split(sep=" ")[1:]]
            dislikes = [dislike.strip() for dislike in dislikes_line.split(sep=" ")[1:]]
            customers.append(Customer(cid, likes, dislikes))
        return customers


if __name__ == '__main__':
    # example usage
    dataset_path = "hash-code-2022/input-data/a_an_example"
    customers = parse_dataset(dataset_path)
    for customer in customers:
        print(customer)
