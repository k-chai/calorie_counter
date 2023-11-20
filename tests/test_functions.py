from module.exception import MealTooBigError, MealOutOfTheMenu
from unittest import TestCase
from module.functions import calories_counter

# Tests for basic dict data
class CaloriesCounterTestCase(TestCase):
    def test_raise_error_if_too_much_calories(self):
        with self.assertRaises(MealTooBigError) as e:
            calories_counter(
                'Vegan Combo', 'something')
            self.assertEqual(e.exception.message,
                             'Too many calories: 2600; maximum is 2000.',
                             f'Wrong message; expected: Too many calories: 2600')

    def test_raise_error_if_meal_out_of_the_menu(self):
        with self.assertRaises(MealOutOfTheMenu) as e:
            calories_counter('Vegan Combo', 'something')
            self.assertEqual(e.exception.message,
                             'A meal "something" is not in the menu',
                             f'Wrong message; expected: A meal "something" is not in the menu')
