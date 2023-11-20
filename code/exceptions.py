# -*- coding: utf-8  -*-

# the exception for calories limit
class MealTooBigError(Exception):
    def __init__(self, calories):
        self.message = f'Too many calories!' \
        f' {calories} exceeds the limit of of 2000.'
        super().__init__(self.message)


# the exception for meal out of the menu
class MealOutOfTheMenu(Exception):
    def __init__(self, meal):
        self.message = f'The meal "{meal}" is not in the menu.'
        super().__init__(self.message)
