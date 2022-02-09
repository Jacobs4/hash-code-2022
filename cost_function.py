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

    # FIXME: this implementation still bottlenecks the SA algorithm(it spends here over ~90% of the time)

    def check_customer(customer: Customer):
        """Returns 0 if one of the requirements isn't satisfied, otherwise returns 1."""
        for disliked_ingredient in customer.dislikes:
            if disliked_ingredient in pizza_ingredients:
                return 0
        for liked_ingredient in customer.likes:
            if liked_ingredient not in pizza_ingredients:
                return 0
        return 1

    score = 0
    for customer in customers:
        score += check_customer(customer)
    return score
