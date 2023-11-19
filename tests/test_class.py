from module.Order_Class import Order
from datetime import datetime
from unittest import TestCase

# Order class tests
class OrderClassTestCase(TestCase):
    # Id
    def test_order_id_counter_change(self):
        order_1 = Order(['meal-3'], date="1-Jan-2022").order_id
        order_2 = Order(['combo-3']).order_id
        self.assertEqual(order_1, 'order--6',
                         f"Expected 'order--1', got {order_1}")
        self.assertEqual(order_2, 'order--7',
                         f"Expected 'order--2', got {order_2}")

    # Date
    def test_order_with_the_predefine_date(self):
        order = Order(['meal-1', 'meal-2'], date="1-Jan-2022")
        self.assertEqual(order.date, "2022-01-01")

    def test_order_without_the_predefine_date(self):
        order = Order(['meal-1', 'meal-2'])
        self.assertEqual(order.date, datetime.today().strftime("%Y-%m-%d"))

    # Calories of meals and combos
    def test_order_calories_calouter_with_meals(self):
        order = Order(['meal-1']).calories
        self.assertEqual(order, 600, f"Expected 600, got {order}")

    def test_order_calories_calouter_with_combos(self):
        result = Order(['combo-2']).calories
        self.assertEqual(result, 700, f'expected 700, got {result}')

    def test_order_calories_calouter_with_meals_and_combos(self):
        result = Order(['meal-4', 'combo-2']).calories
        self.assertEqual(result, 1050, f'expected 1050, got {result}')

    # Exception MealOutOfTheMenu
    def test_order_creation_exception_MealOutOfTheMeal(self):
        result = Order(['invalid-meal']).order_refused_reason
        self.assertEqual(result, 'The meal "invalid-meal" is not in the menu.',
                         f'Wrong message; expected: A meal "invalid-meal" is not in the menu')

    # Excpetion MealTooBigError
    def test_order_creation_exception_MealTooBigError(self):
        result = Order(['meal-4', 'meal-4', 'combo-2',
                       'meal-4', 'combo-3']).order_refused_reason
        self.assertEqual(result, 'Too many calories: 2205; maximum is 2000.',
                         f'Wrong message; expected: Too many calories: 2205; maximum is 2000.')

    # Price of meals and combos
    def test_order_price_with_meals(self):
        result = Order(['meal-1']).price
        self.assertEqual(result, 5, f"Expected 5, got {result}")

    def test_order_price_with_combos(self):
        result = Order(['combo-1']).price
        self.assertEqual(result, 11, f'expected 11, got {result}')

    def test_order_price_with_meals_and_combos(self):
        result = Order(['combo-1', 'meal-1']).price
        self.assertEqual(result, 16, f'expected 16, got {result}')

    def test_order_price_when_MealTooBigError(self):
        result = Order(['combo-1', 'meal-1', 'combo-1', 'meal-1']).price
        self.assertEqual(result, None, f'expected None, got {result}')

    # Order_accepted
    def test_order_if_order_accepted_correct(self):
        result = Order(['combo-1', 'meal-1']).order_accepted
        self.assertEqual(result, True, f'expected True, got {result}')

    def test_order_if_order_accepted_incorrect(self):
        result = Order(['invalid-meal']).order_accepted
        self.assertEqual(result, False, f'expected False, got {result}')