import unittest
from main import count_available_fresh_ingredients_ids

class TestCountAvailableFreshIngredientsIds(unittest.TestCase):
    def test_count_available_fresh_ingredients_ids(self):
        count = count_available_fresh_ingredients_ids(
            'files/ingredients/fresh/range-ids-test.txt',
            'files/ingredients/available/ids-test.txt'
        )
        self.assertEqual(count, 3)
