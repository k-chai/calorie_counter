from code.exceptions import MealTooBigError, MealOutOfTheMenu
from code.constants import MEALS_DICT, COMBOS_DICT


def name_to_id(*id_list):
    ids = list(id_list).copy()
    for i in range(len(ids)):
        item = str(ids[i]).lower()
        for j in MEALS_DICT:
            if item == MEALS_DICT[j]['name']:
                ids[i] = MEALS_DICT[j]['id']
                continue
        for j in COMBOS_DICT:
            if item == COMBOS_DICT[j]['name']:
                ids[i] = COMBOS_DICT[j]['id']
                continue
    return ids


# general
def find_menu_type(item):
    if item in MEALS_DICT:
        return 'meals'
    elif item in COMBOS_DICT:
        return 'combos'
    else:
        raise KeyError


# calories recurcive
def calories_counter(*order):
    calories_count = 0
    order_modified = name_to_id(*order)
    for item in order_modified:
        try:
            menu_type = find_menu_type(item)
            if menu_type == 'meals':
                calories_count += MEALS_DICT[item]['calories']
            elif menu_type == 'combos':
                calories_count += calories_counter(
                    *COMBOS_DICT[item]['meals'])
        except KeyError:
            raise MealOutOfTheMenu(item)
    if calories_count > 2000:
        raise MealTooBigError(calories_count)
    return calories_count


# price
def price_counter(*order):
    order_modified = name_to_id(*order)
    price_count = 0
    for item in order_modified:
        try:
            menu_type = find_menu_type(item)
            price_count_current = eval(
                (menu_type + '_dict').upper() + "[item]['price']")
            price_count += price_count_current
        except KeyError:
            raise MealOutOfTheMenu(item)
    return price_count
