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
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    
get_spicy_food_by_cuisine(spicy_foods, "Thai")


# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     by_cuisine = []
#     for food in spicy_foods:
#         if food["cuisine"] == cuisine:
#             by_cuisine.append(food)
#     return by_cuisine
# get_spicy_food_by_cuisine(spicy_foods, "Thai")




def print_spiciest_foods(spicy_foods):
    spicy = []
    chili_image = "🌶"
    for food in spicy_foods:
        heat_level = food["heat_level"]
        if heat_level > 5:
            spicy.append(f"{food['name']} ({food['cuisine']}) | Heat Level: {chili_image * heat_level}")
    for food in spicy:
        print(food)




def get_average_heat_level(spicy_foods):
    heat_level = 0
    for food in spicy_foods:
        heat_level += food["heat_level"]
        ave = heat_level / len(spicy_foods)
    return ave




def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods












