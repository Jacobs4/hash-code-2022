"""Taboo search algorithm implementation

Based on: Dominik Żurek (https://github.com/Treborsky/hash-code-2022/blob/main/simulated_annealing.py) ;)

"""


import copy, random
from typing import List, Callable
from __future__ import annotations

from cost_function import naive_cost_function
from custom_parser import Customer


class TSSolution:

	def __init__(self, customers: List[Customer], pizza_ingredients: List[str] = None):
		self.customers = customers
		if pizza_ingredients is None:
			self._initial_solution()
		else:
			self.pizza_ingredients = pizza_ingredients

	def _initial_solution(self):
		"""Makes a pizza with all the ingredients customers like.
		
		"""
		self.pizza_ingredients = []
		for customer in self.customers:
			self.pizza_ingredients += customer.likes
		self.pizza_ingredients = list(set(self.pizza_ingredients)) # remove duplicate ingredients

	@property
	def score(self) -> int:
		return naive_cost_function(self.pizza_ingredients, self.customers)

	def submission_format(self) -> str:
		"""Returns the solution as the number of ingredients followed by the names of the ingredients.
		
		"""
		ingredients = " ".join([str(ingredient) for ingredient in self.pizza_ingredients])
		return f'{len(self.pizza_ingredients)} ' + ingredients

	def create_new_solution(self) -> TSSolution:
		"""Creates a new solution by changing the current one with a neighbourhood operator.
		
		"""
		operators = [add_liked_ingredient, remove_disliked_ingredient]
		operator: neighbourhood_operator = random.choice(operators)
		new_pizza_ingredients = operator(self.pizza_ingredients, self.customers)
		return TSSolution(self.customers, new_pizza_ingredients)


# neighbourhood operators
neighbourhood_operator = Callable[[List[str], List[Customer]], List[str]]


def remove_disliked_ingredient(pizza_ingredients: List[str], customers: List[Customer]) -> List[str]:
    """Removes an ingredient a random customer dislikes from the pizza.
	
	"""
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
    """Adds an ingredient a random customer likes to the pizza.
	
	"""
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

def taboo_search(customers: List[Customer], ) -> TSSolution:
	"""Taboo search metaheuristic customized for the One Pizza problem
	
	Args:
		customers (List[Customer])	: list of surveyed customers
		max_iter (int)	: maximum iterations allowed in the algorythm
		tl_short (int)	: short term taboo list size
		tl_medium (int)	: medium term taboo list size
		tl_long	(int)	: long term taboo list size
		ssm (Callable)	: solution selection method
	
	Returns:
		sl_best (List[str]): best suboptimal solution
	
	"""
	# TODO: implement suke
	return TSSolution(customers)
