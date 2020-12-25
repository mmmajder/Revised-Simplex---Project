import numpy as np


def get_dishes(list_of_dishes, sum_of_calories):
    n = len(list_of_dishes)
    calories = [sum_of_calories]
    proteins = [0]
    carbs = [0]
    fats = [0]
    for dish in list_of_dishes:
        calories.append(-dish.calories)
        proteins.append(-dish.proteins)
        carbs.append(dish.carbs)
        fats.append(dish.fats)
    calories += [0] * (2 * n + 3)
    ones_array = np.ones((2 * n + 3, 2 * n + 3))

    proteins += ones_array[0]
    carbs += ones_array[1]
    fats += ones_array[2]
    min_max_dishes = []
    for i in range(len(list_of_dishes)):
        dishpoz = [0]
        dishpoz += [0] * i
        dishpoz += [1]
        dishpoz += [0] * (n - i - 1)
        dishpoz += ones_array[3 + 2 * i]
        dishneg = [0]
        dishneg += [0] * i
        dishneg += [-1]
        dishneg += [0] * (n - i - 1)
        dishneg += ones_array[3 + 2 * i + 1]
        min_max_dishes.append(dishpoz)
        min_max_dishes.append(dishneg)
    

    # A = np.array([[1, x1, x1 ** 2], [1, x2, x2 ** 2], [1, x3, x3 ** 2]])
    # print(A)


if __name__ == '__main__':
    get_dishes([])
