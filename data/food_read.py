import json


# menu to dict

# def menu_type_to_dict(menu_type):
#     try: 
#         menu_dict = eval(menu_type + '_dict') #check if the dict already exist 
#     except NameError:
#         menu_dict = {
#         item ["name"]: item
#         for item in eval(menu_type)
#         }  
#     return(menu_dict)


def menu_to_dict(menu):
    menu_dict = {
        item['name']: item
        for item in menu
    }  
    return(menu_dict)

with open("data/meals.json") as file:
	meals = json.load(file)['meals']

with open("data/combos.json") as file:
	combos = json.load(file)['combos']

meals_dict = menu_to_dict(meals)
combos_dict = menu_to_dict(combos)
