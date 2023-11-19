from module.exception import MealTooBigError, MealOutOfTheMenu
from unittest import TestCase
from module.functions_calorie_counter import (
    total_calories_counter,
    calorie_counter_advanced_data,
    costs_counter_advanced_data,
)

# Tests for basic dict data
class CaloriesCounterTestCase(TestCase):
    def test_count_meals_calories(self):
        result = total_calories_counter(['Hamburger'])
        self.assertEqual(result, 600, f"Expected 600, got {result}")

    def test_count_combo_calories(self):
        result = total_calories_counter(['Veggie Combo'])
        self.assertEqual(result, 700, f'expected 700, got {result}')

    def test_count_combo_and_meals_calories(self):
        result = total_calories_counter(['Hamburger', 'Veggie Combo'])
        self.assertEqual(result, 1300, f'expected 1300, got {result}')

    def test_raise_error_if_too_much_calories(self):
        with self.assertRaises(MealTooBigError) as e:
            total_calories_counter(
                ['Hamburger', 'Veggie Combo', 'Hamburger', 'Veggie Combo'])
            self.assertEqual(e.exception.message, 'Too many calories: 2600; maximum is 2000.',
                             f'Wrong message; expected: Too many calories: 2600')

    def test_raise_error_if_meal_out_of_the_menu(self):
        with self.assertRaises(MealOutOfTheMenu) as e:
            total_calories_counter(['combo-4'])
            self.assertEqual(e.exception.message, 'A meal "combo-4" is not in the menu',
                             f'Wrong message; expected: A meal "combo-4" is not in the menu')

# Tests for advanced data
class CaloriesCounterAdvancedDataTestCase(TestCase):
    def test_count_meals_calories_advanced(self):
        result = calorie_counter_advanced_data(['meal-1'])
        self.assertEqual(result, 600, f"Expected 600, got {result}")

    def test_count_combo_calories_advanced(self):
        result = calorie_counter_advanced_data(['combo-2'])
        self.assertEqual(result, 700, f'expected 700, got {result}')

    def test_count_combo_and_meals_calories_advanced(self):
        result = calorie_counter_advanced_data(['meal-1', 'combo-2'])
        self.assertEqual(result, 1300, f'expected 1300, got {result}')

    def test_raise_error_if_too_much_calories_advanced(self):
        with self.assertRaises(MealTooBigError) as e:
            calorie_counter_advanced_data(
                ['meal-4', 'meal-4', 'combo-2', 'meal-4', 'combo-3'])
            self.assertEqual(e.exception.message, 'Too many calories: 2205; maximum is 2000.',
                             f'Wrong message; expected: Too many calories: 2205')

    def test_meal_out_of_the_menu_advanced(self):
        with self.assertRaises(MealOutOfTheMenu) as e:
            calorie_counter_advanced_data(['hamburger'])
            self.assertEqual(e.exception.message, 'The meal "hamburger" is not in the menu.',
                             f'Wrong message; expected: The meal "hamburger" is not in the menu')

# Price counter with the same tests
class CostCounterTestCase(TestCase):
    def test_count_meals_costs(self):
        result = costs_counter_advanced_data(['meal-1'])
        self.assertEqual(result, 5, f"Expected 5, got {result}")

    def test_count_combo_costs(self):
        result = costs_counter_advanced_data(['combo-1'])
        self.assertEqual(result, 11, f'expected 11, got {result}')

    def test_count_combo_and_meals_count(self):
        result = costs_counter_advanced_data(['combo-1', 'meal-1'])
        self.assertEqual(result, 16, f'expected 16, got {result}')

    def test_meal_out_of_the_menu(self):
        with self.assertRaises(MealOutOfTheMenu) as e:
            costs_counter_advanced_data(['combo-12'])
            self.assertEqual(
                e.exception.message, 'A meal - combo-12 is not in the menu', 'wrong message')