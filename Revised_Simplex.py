import math

import numpy as np
from numpy.linalg import inv

from Dish import Dish


def get_additonal_table(n, matrix):
    # 5 because of price, calories, proteins, carbs, fats
    return matrix[0:2 * n + 5, 1:n + 1]


def getMax(B1, additional_table):
    first_row = B1[0] * (-1)
    new_matrix = np.matmul(first_row, additional_table)
    postion = np.where(new_matrix == np.amax(new_matrix))[0]
    return np.amax(new_matrix), postion


def find_min_ratio(results, y1):
    min = math.inf
    position = math.inf
    for i in range(len(results)):
        if y1[i] > 0:
            if results[i] / y1[i] < min:
                min = results[i] / y1[i]
                position = i
    return min[0], position


def put_dishes_in_matrix(list_of_dishes, calories_min, protein_min, carbs_max, fat_max):
    # step 1
    n = len(list_of_dishes)
    matrix = make_matrix(list_of_dishes, n)
    print(matrix)
    results = get_results(calories_min, carbs_max, fat_max, list_of_dishes, protein_min)
    print(results)

    # step 2
    B1 = np.identity(2 * n + 5)
    additional_table = get_additonal_table(n, matrix)
    print(additional_table)

    # step 3
    # y1 = c1-z1
    c1_z1, k = getMax(B1, additional_table)
    print(k)
    # k - u kojoj koloni se nalazi najveci element
    print(c1_z1)

    # step 4
    print(additional_table[:, k])
    yk = np.matmul(inv(np.matrix(B1)), additional_table[:, k])
    print(yk)
    min_ration, r = find_min_ratio(results, yk)
    print(min_ration, r)

    # step 5
    # create_solution()


def get_results(calories_min, carbs_max, fat_max, list_of_dishes, protein_min):
    results = np.array([0.0, calories_min, protein_min, carbs_max, fat_max])
    for dish in list_of_dishes:
        results = np.append(results, dish.max)
        results = np.append(results, -dish.min)
    return results


def make_matrix(list_of_dishes, n):
    calories, carbs, fats, proteins, price = initialize_parameters()
    for dish in list_of_dishes:
        price.append(float(-dish.price))
        calories.append(float(-dish.calories))
        proteins.append(float(-dish.proteins))
        carbs.append(float(dish.carbs))
        fats.append(float(dish.fats))
    price += [0.0] * (2 * n + 4)
    identity_array = np.identity(2 * n + 4)
    calories += identity_array[0].tolist()
    proteins += identity_array[1].tolist()
    carbs += identity_array[2].tolist()
    fats += identity_array[3].tolist()
    price = np.array([price])
    calories = np.array([calories])
    proteins = np.array([proteins])
    carbs = np.array([carbs])
    fats = np.array([fats])
    matrix = np.concatenate((price, calories, proteins, carbs, fats), axis=0)
    min_max_dishes = []
    for i in range(len(list_of_dishes)):
        dishpoz = [0.0]
        dishpoz += [0.0] * i
        dishpoz += [1.0]
        dishpoz += [0.0] * (n - i - 1)
        dishpoz += identity_array[4 + 2 * i].tolist()
        dishneg = [0.0]
        dishneg += [0.0] * i
        dishneg += [-1.0]
        dishneg += [0.0] * (n - i - 1)
        dishneg += identity_array[4 + 2 * i + 1].tolist()
        # arr = numpy.array(lst)
        min_max_dishes.append(dishpoz)
        min_max_dishes.append(dishneg)
        dishpoz = np.array([dishpoz])
        dishneg = np.array([dishneg])
        matrix = np.concatenate((matrix, dishpoz, dishneg), axis=0)
    return matrix


def initialize_parameters():
    price = [1.]
    calories = [0.]
    proteins = [0.]
    carbs = [0.]
    fats = [0.]
    return calories, carbs, fats, proteins, price


def get_dishes(file_name):
    dishes = []
    file = open(file_name)
    for line in file.readlines():
        dishes.append(Dish(line.rstrip().split('|')))
    file.close()
    return dishes


if __name__ == '__main__':
    DISHES = get_dishes("dishes.txt")
    put_dishes_in_matrix(DISHES, 2369, 144, 316, 67)
