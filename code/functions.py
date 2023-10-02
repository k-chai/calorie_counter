# menu to dict

def menu_to_dict(menu_type):
    try: 
        menu_dict = eval(menu_type + '_dict') #check if the dict already exist 
    except NameError:
        menu_dict = {
        item ["name"]: item
        for item in eval(menu_type)
        }  
    return(menu_dict)
    
    
# general

def find_menu_type(item):
    if item in meals_dict:
        return('meals')
    elif item in combos_dict:
        return('combos')
    else:
        raise KeyError

# calories

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
        # print('combo: ', item)
        meals_in_combo = combos_dict[item]['meals']
        for i in range(len(meals_in_combo)):
            for j in meals_dict:
                if meals_in_combo[i] == meals_dict[j]['id']:
                    meals_in_combo[i] = meals_dict[j]['name']
                    break
        # print(f'meals_in_combo: {meals_in_combo}')
        combo_calories_count = calories_counter_meals(*meals_in_combo)
        calories_count += combo_calories_count
        print(f'{item} combo calories count: {combo_calories_count}\n')
        # print(f'current calories count: {calories_count}')
    return(calories_count)

def calories_counter_order(*order):
    meals_dict = menu_to_dict('meals')
    combos_dict = menu_to_dict('combos')
    calories_count = 0
    for item in order:
        print(f'item: {item}')
        try:
            menu_type = find_menu_type(item)
            # print(f'menu_type: {menu_type}')
            calories_count += eval('calories_counter_' + menu_type + '(item)')
            # print(f'current calories count: {calories_count}\n')
        except KeyError:
            print(f'{item} is not on the menu\n')
    return(calories_count)


# price

def price_counter(*order):
    meals_dict = menu_to_dict('meals')
    combos_dict = menu_to_dict('combos')
    price_count = 0
        for item in order:
        try:
            menu_type = find_menu_type(item)
            # print(f'menu_type: {menu_type}')
            price_count_current = eval(menu_type + '_dict' + "[item]['price']")
            price_count += price_count_current
            print(f'{item} price count: {price_count_current}')
        except KeyError:
            print(f'{item} is not on the menu')
    return(price_count)



