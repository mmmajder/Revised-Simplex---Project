import math

from Nutients import Nutrients


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
    fats_min, fats_max = calories * 0.15, calories * 0.3
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
