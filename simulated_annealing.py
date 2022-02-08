import random
import math
import copy
from typing import List, Callable
from custom_parser import parse_dataset, Customer
from cost_function import naive_cost_function


class Solution:
    def __init__(self, customers: List[Customer], pizza_ingredients: List[str] = None):
        self.customers = customers
        if pizza_ingredients is None:
            self._initial_solution()
        else:
            self.pizza_ingredients = pizza_ingredients

    def _initial_solution(self):
        """Makes a pizza with all the ingredients customers like."""
        self.pizza_ingredients = []
        for customer in self.customers:
            self.pizza_ingredients += customer.likes
        # remove duplicate ingredients
        self.pizza_ingredients = list(set(self.pizza_ingredients))

    @property
    def score(self) -> int:
        return naive_cost_function(self.pizza_ingredients, self.customers)

    def submission_format(self) -> str:
        """Returns the solution as the number of ingredients followed by the names of the ingredients."""
        ingredients = " ".join([str(ingredient) for ingredient in self.pizza_ingredients])
        return f'{len(self.pizza_ingredients)} ' + ingredients

    def create_new_solution(self) -> 'Solution':
        """Creates a new solution by changing the current one with a neighbourhood operator."""
        operators = [add_liked_ingredient, remove_disliked_ingredient]
        operator: neighbourhood_operator = random.choice(operators)
        new_pizza_ingredients = operator(self.pizza_ingredients, self.customers)
        return Solution(self.customers, new_pizza_ingredients)


# neighbourhood operators

neighbourhood_operator = Callable[[List[str], List[Customer]], List[str]]


def remove_disliked_ingredient(pizza_ingredients: List[str], customers: List[Customer]) -> List[str]:
    """Removes an ingredient a random customer dislikes from the pizza."""
    pizza_ingredients = copy.copy(pizza_ingredients)
    customers_that_dislike_stuff = [customer for customer in customers if customer.dislikes]
    if not customers_that_dislike_stuff:
        return pizza_ingredients
    random_customer = random.choice(customers_that_dislike_stuff)
    for disliked_ingredient in random_customer.dislikes:
        if disliked_ingredient in pizza_ingredients:
            pizza_ingredients.remove(disliked_ingredient)
            break
    return pizza_ingredients


def add_liked_ingredient(pizza_ingredients: List[str], customers: List[Customer]) -> List[str]:
    """Adds an ingredient a random customer likes to the pizza."""
    pizza_ingredients = copy.copy(pizza_ingredients)
    customers_that_like_stuff = [customer for customer in customers if customer.likes]
    if not customers_that_like_stuff:
        return pizza_ingredients
    random_customer = random.choice(customers_that_like_stuff)
    for liked_ingredient in random_customer.likes:
        if liked_ingredient not in pizza_ingredients:
            pizza_ingredients.append(liked_ingredient)
            break
    return pizza_ingredients


# cooling schedules

cooling_schedule = Callable[[float, float, int], float]


def exponential_cooling_schedule(t_start: float, alpha: float, iteration: int) -> float:
    """Returns the new temperature of the system changed according to the exponential cooling schedule."""
    return t_start * alpha ** iteration


def simulated_annealing(customers: List[Customer], t_start: float, t_stop: float, t_iter: int, alpha: float,
                        change_temperature: cooling_schedule) -> Solution:
    """Simulated annealing optimization algorithm.

    Args:
        customers: list of surveyed customers.
        t_start: starting temperature of the system.
        t_stop: temperature after which the algorithm will halt.
        t_iter: number of iterations in a given temperature.
        alpha: the rate of temperature change coefficient.
        change_temperature: the cooling schedule used in the algorithm.

    Returns:
        Best found solution for the problem.

    """
    current_solution = Solution(customers)
    best_solution = current_solution
    t_current = t_start
    iterations = 0

    while t_current > t_stop:
        for k in range(t_iter):
            new_solution = current_solution.create_new_solution()
            if new_solution.score >= current_solution.score:
                current_solution = new_solution
                if current_solution.score >= best_solution.score:
                    best_solution = current_solution
            else:
                delta = new_solution.score - current_solution.score
                sigma = random.random()
                if sigma < math.exp(delta / t_current):
                    current_solution = new_solution
            iterations += 1

        t_current = change_temperature(t_start, alpha, iterations)
        print(t_current)

    return best_solution


if __name__ == '__main__':
    customers = parse_dataset("input-data/c_coarse.in.txt")
    solution = simulated_annealing(customers, t_start=100, t_stop=1, t_iter=20, alpha=0.99,
                                   change_temperature=exponential_cooling_schedule)
    print(solution.score)
    print(solution.submission_format())

