from itertools import combinations

import numpy as np


def get_prices_array(selected_dishes):
    prices = []
    for dish in selected_dishes:
        prices.append(dish.price)
    for i in range(7):
        prices.append(0)
    return np.array(prices)


def get_edges_array(selected_dishes, nutrient_range):
    list = nutrient_range.to_array()
    for dish in selected_dishes:
        list.append(-dish.min)
        list.append(dish.max)
    return list


def get_nutrient_matrix(selected_dishes):
    n = len(selected_dishes)
    rows = 7 + 2 * n
    cols = 7 + 3 * n
    matrix = np.zeros((rows, cols))
    for j in range(n):
        matrix[0][j] = selected_dishes[j].calories
        matrix[1][j] = -selected_dishes[j].proteins
        matrix[2][j] = selected_dishes[j].proteins
        matrix[3][j] = -selected_dishes[j].carbs
        matrix[4][j] = selected_dishes[j].carbs
        matrix[5][j] = -selected_dishes[j].fats
        matrix[6][j] = selected_dishes[j].fats
    current_row = 7
    for current_col in range(0, n):
        matrix[current_row][current_col] = -1
        matrix[current_row + 1][current_col] = 1
        current_row += 2
    for i in range(rows):
        matrix[i][i + n] = 1
    return np.array(matrix)

def get_list_B(b):
    return list(range(0, len(b)))


def get_A_on_B(A, list_B):
    return A[:, list_B]


def get_cb(c, list_B):
    return c[list(list_B)]


def calculate_amounts(selected_dishes, nutrient_range):
    c = get_prices_array(selected_dishes)
    b = get_edges_array(selected_dishes, nutrient_range)
    A = get_nutrient_matrix(selected_dishes)
    print("c = ", c)
    print("b = ", b)
    print("A = ", A)
    A_on_B, A_on_B_inv, XB, l = phase_one(b, A)
    print("B = ", A_on_B)

def phase_one(b, A):
    list_of_variables = list(range(len(A[0])))
    for B in combinations(list_of_variables, len(A)):
        A_on_B = get_A_on_B(A, B)
        try:
            A_on_B_inv = np.linalg.inv(A_on_B)
            XB = A_on_B_inv.dot(b)
            if np.all((XB > 0)):
                return A_on_B, A_on_B_inv, XB, list(B)
        except:
            continue
    return False
