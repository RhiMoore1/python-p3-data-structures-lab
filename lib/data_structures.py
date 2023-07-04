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
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names



def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest.append(food)
    return spiciest


    

def print_spicy_foods(spicy_foods):
    spicy = []
    chili_image = "🌶"
    for food in spicy_foods:
        heat_level = food['heat_level']
        spicy.append(f"{food['name']} ({food['cuisine']}) | Heat Level: {chili_image * heat_level}")
    for food in spicy:
        print(food, end='\n')
    
    
# terminal output
# >>> print_spicy_foods(spicy_foods)
# Green Curry (Thai) | Heat Level: 🌶 🌶 🌶 🌶 🌶 🌶 🌶 🌶 🌶 
# Buffalo Wings (American) | Heat Level: 🌶 🌶 🌶 
# Mapo Tofu (Sichuan) | Heat Level: 🌶 🌶 🌶 🌶 🌶 🌶 

# >>> print_spicy_foods(spicy_foods)
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶





def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    pass

def create_spicy_food(spicy_foods, spicy_food):
    pass















# def get_spiciest_foods(spicy_foods):
#     spiciest = []
#     for food in spicy_foods:
#         spiciest.append(food["heat_level"])
#         spiciest.sort()
#     return spiciest
