from code.exceptions import MealTooBigError, MealOutOfTheMenu
from data.food_read import meals_dict, combos_dict

def id_to_name(*id_list):
    ids = id_list.copy()
    for i in range(len(ids)):
        for j in meals_dict:
            if ids[i] == meals_dict[j]['id']:
                ids[i] = meals_dict[j]['name']
    return(ids)

# general
def find_menu_type(item):
    if item in meals_dict:
        return('meals')
    elif item in combos_dict:
        return('combos')
    else:
        raise KeyError

# calories non-recurcive
def calories_counter_meals(*order):
    calories_count = 0
    for item in order:
        # print(f'meal: {item}')
        meal_calories_count = meals_dict[item]['calories']
        calories_count += meal_calories_count
        print(f'{item} meal calories count: {meal_calories_count}')
    return(calories_count)

def calories_counter_combos(*order):
    calories_count = 0
    for item in order:
        meals_in_combo = combos_dict[item]['meals']
        for i in range(len(meals_in_combo)):
            for j in meals_dict:
                if meals_in_combo[i] == meals_dict[j]['id']:
                    meals_in_combo[i] = meals_dict[j]['name']
                    break
        combo_calories_count = calories_counter_meals(*meals_in_combo)
        calories_count += combo_calories_count
        print(f'{item} combo calories count: {combo_calories_count}\n')
    return(calories_count)

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
    return(calories_count)

# calories recurcive
def calories_counter(*order):
    calories_count = 0
    for item in order:
        # print(f'item: {item}')
        try:
            menu_type = find_menu_type(item)
            if menu_type == 'meals':
                calories_count += meals_dict[item]['calories']
            elif menu_type == 'combos':
                calories_count += calories_counter(id_to_name(*meals_dict[item]['calories']))
        except KeyError:
            raise MealOutOfTheMenu(meal)
        if calories_count > 2000:
            raise MealTooBigError(calories_count)
    return(calories_count)

# price
def price_counter(*order):
    price_count = 0
    for item in order:
        try:
            menu_type = find_menu_type(item)
            price_count_current = eval(menu_type + '_dict' + "[item]['price']")
            price_count += price_count_current
            # print(f'{item} price count: {price_count_current}')
        except KeyError:
            # print(f'{item} is not on the menu')
            pass
    return(price_count)



