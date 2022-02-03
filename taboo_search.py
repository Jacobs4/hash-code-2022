from typing import List
from __future__ import annotations

from cost_function import naive_cost_function
from custom_parser import Customer


class TabooSearch:
	"""Taboo Search implementation for the One Pizza problem.
	
	The cost function is hardcoded, the solution is a vector of ingredients.
	"""
	def __init__(self):

		# program data
		self.m_ingredients: List[str]
		self.m_customers: List[Customer]

		# algorythm data
		self.glb_best: int			# global best
		self.sol_best: List[str]	# solution vector containing ingredients

	def solve(self, iter_max: int=1000) -> TabooSearch:
		"""Approximates the solution using Taboo Search algo
		
		Args:
			iter_max: maximum number of iterations before the algorythm stops

		Returns:
			TabooSearch: itself, with updated parameters
		"""
		# TODO: implement tą suke
		return self
