import math

from classes.Dish import Dish
from classes.Nutrients import Nutrients


def get_nutrient_range_string(nutrient_range):
    return "Calories: " + str(round(nutrient_range.calories, 1)) + "kcal\tProteins: " + str(
        round(nutrient_range.proteins_min, 1)) + "-" + str(round(nutrient_range.proteins_max, 1)) + "g\tCarbs: " + str(
        round(nutrient_range.carbs_min, 1)) + "-" + str(round(nutrient_range.carbs_max, 1)) + \
           "g\tFats: " + str(round(nutrient_range.fats_min, 1)) + "-" + str(round(nutrient_range.fats_max, 1)) + "g"


def get_dishes(file_name):
    dishes = []
    file = open(file_name)
    for line in file.readlines():
        dishes.append(Dish(line.rstrip().split('|')))
    file.close()
    return dishes


def get_string_dishes(file_name):
    dishes = []
    file = open(file_name)
    for line in file.readlines():
        if line:
            dishes.append(line.rstrip().split('|'))
    file.close()
    return sorted(dishes, key=lambda dish: dish[0], reverse=False)


def get_dish(name):
    for dish in get_dishes("material/dishes.txt"):
        if dish.name == name:
            return dish
    return None


def save_dishes(file_name, dishes):
    file = open(file_name, 'w')
    for dish in dishes:
        file.write(dish.to_string())
    file.close()


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


def get_activity_factor(activity):
    if activity == 0:
        return 1.2
    elif activity == 1:
        return 1.4
    elif activity == 2:
        return 1.6
    return 1.75


def calculate_calories(age, gender, height, weight, activity, goal):
    calories = 10 * weight + 6.25 * height - 5 * age
    if gender == "female":
        calories -= 161
    else:
        calories += 5
    calories *= get_activity_factor(activity)
    calories = roundup(calories)
    if goal == 0:
        return calories - 500
    if goal == 2:
        return calories + 500
    return calories


def protein_range_by_activity(weight, activity):
    if activity == 0:
        return 0.8 * weight, 1.2 * weight
    elif activity == 1:
        return 1.2 * weight, 1.6 * weight
    elif activity == 2:
        return 1.6 * weight, 1.7 * weight
    return 1.7 * weight, 1.9 * weight


def carb_range_by_activity(weight, activity):
    weight = float(weight)
    if activity == 0:
        return weight, 3 * weight
    elif activity == 1:
        return 3 * weight, 5 * weight
    elif activity == 2:
        return 5 * weight, 7 * weight
    return 7 * weight, 12 * weight


def protein_range(weight, activity, goal):
    protein_min, protein_max = protein_range_by_activity(weight, activity)
    if goal in [2, 3]:
        return protein_min * 1.2, protein_max * 1.5
    return protein_min, protein_max


def nutrient_range(age, gender, height, weight, activity, goal):
    calories = calculate_calories(age, gender, height, weight, activity, goal)
    protein_min, protein_max = protein_range(weight, activity, goal)
    carbs_min, carbs_max = carb_range_by_activity(weight, activity)
    fats_min, fats_max = round(calories / 9 * 0.15, 1), round(calories / 9 * 0.3, 1)
    return Nutrients(calories, protein_min, protein_max, carbs_min, carbs_max, fats_min, fats_max)


def get_goals():
    return ['lose weigth', 'maintain', 'gain weigth', 'gain muscle']


def get_activities():
    return ['little or no exercise',
            '1-3 workouts a week',
            '4-5 workouts a week',
            '6-7 workouts a week']


def list_of_strings_in_range(a, b, text):
    list = []
    for i in range(a, b):
        list.append(str(i) + text)
    return list


def get_total_price(selected_dishes, amounts):
    total_price = 0
    if len(selected_dishes) != len(amounts):
        print("error")
    for i in range(len(amounts)):
        total_price += amounts[i] * selected_dishes[i].price
    return round(total_price, 2)
