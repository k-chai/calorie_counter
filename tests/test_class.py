from module.Order_Class import Order
from unittest import TestCase


# Order class tests
class OrderClassTestCase(TestCase):
    # Exception MealOutOfTheMenu
    def test_MealOutOfTheMeal(self):
        result = Order('Vegan Combo', 'something').order_refused_reason
        self.assertEqual(result, 'The meal "something" is not in the menu.',
                         f'Wrong message; expected: '
                         f' A meal "something" is not in the menu')

    # Excpetion MealTooBigError
    def test_MealTooBigError(self):
        result = Order(
            'Vegan Combo', 'Veggie combo', 'Cheesy Combo').order_refused_reason
        self.assertEqual(result, 'Too many calories! 2225 exceeds the limit of of 2000.',
                         f'Wrong message; expected:' \
                         f' Too many calories: 2205; maximum is 2000.')
