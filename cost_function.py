from typing import List
from custom_parser import Customer


def naive_cost_function(pizza_ingredients: List[str], customers: List[Customer]) -> int:
    """
    Scores pizza ingredients by checking if a given customer would order such pizza.
    The rules are that a customer will order a pizza if all the ingredients they like are on the pizza,
    and none of the ingredients they dislike are on the pizza.

    Args:
        pizza_ingredients: list of ingredients on a the pizza.
        customers: list of Customers that were surveyed.

    Returns:
        The number of customers that would order the pizza.

    """
    score = 0
    for customer in customers:
        if all([liked_ingredient in pizza_ingredients for liked_ingredient in customer.likes]) and \
                not any([disliked_ingredient in pizza_ingredients for disliked_ingredient in customer.dislikes]):
            score += 1
    return score

