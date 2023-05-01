spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [item['name'] for item in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spicy = [object for object in spicy_foods if object['heat_level'] > 5]
    return spicy

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        n = food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: " + "🌶" * n)
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spicy = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(spicy)

def get_average_heat_level(spicy_foods):
    heat_level = 0
    for food in spicy_foods:
        heat_level += food['heat_level']
    average = heat_level / 3
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
