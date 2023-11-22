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


# calories non-recurcive
def calories_counter_meals(*order):
    calories_count = 0
    for item in order:
        meal_calories_count = MEALS_DICT[item]['calories']
        calories_count += meal_calories_count
        print(f'{item} meal calories count: {meal_calories_count}')
    return calories_count


def calories_counter_combos(*order):
    calories_count = 0
    for item in order:
        meals_in_combo = COMBOS_DICT[item]['meals']
        for i in range(len(meals_in_combo)):
            for j in MEALS_DICT:
                if meals_in_combo[i] == MEALS_DICT[j]['id']:
                    meals_in_combo[i] = MEALS_DICT[j]['name']
                    break
        combo_calories_count = calories_counter_meals(*meals_in_combo)
        calories_count += combo_calories_count
        print(f'{item} combo calories count: {combo_calories_count}\n')
    return calories_count


def calories_counter_order(*order):
    calories_count = 0
    for item in order:
        print(f'item: {item}')
        try:
            menu_type = find_menu_type(item)
            calories_count += eval('calories_counter_' + menu_type + '(item)')
        except KeyError:
            print(f'{item} is not on the menu\n')
        if calories_count > 2000:
            raise MealTooBigError(calories_count)
    return calories_count


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
