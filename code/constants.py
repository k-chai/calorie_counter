import json


def menu_to_dict(menu):
    menu_dict = {
        item['id']: item
        for item in menu
    }
    return menu_dict


with open("data/meals.json") as file:
    meals = json.load(file)['meals']

with open("data/combos.json") as file:
    combos = json.load(file)['combos']

MEALS_DICT = menu_to_dict(meals)
COMBOS_DICT = menu_to_dict(combos)
