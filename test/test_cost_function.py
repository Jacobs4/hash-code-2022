import pytest
import json

from cost_function import naive_cost_function
from custom_parser import Customer


with open("test/tests_data.json", "r") as f:
    data = json.load(f)
    test_naive_cost_function_data = []
    for test_case in data["naive_cost_function"]:
        pizza = test_case["pizza"]
        customers = [Customer(c["id"], c["likes"], c["dislikes"]) for c in test_case["customers"]]
        score = test_case["score"]
        test_naive_cost_function_data.append((pizza, customers, score))


@pytest.mark.parametrize('pizza, customers, expected_score', test_naive_cost_function_data)
def test_naive_cost_function(pizza, customers, expected_score):
    assert naive_cost_function(pizza, customers) == expected_score
