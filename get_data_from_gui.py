import numpy as np
from scipy.optimize import linprog

from revised_simplex_method_min import revised_simplex_method


def get_prices_array(selected_dishes):
    prices = []
    for dish in selected_dishes:
        prices.append(dish.price)
    for i in range(7 + len(selected_dishes)):
        prices.append(0)
    return np.array(prices)


def get_edges_array(selected_dishes, nutrient_range):
    list = nutrient_range.to_array()
    for dish in selected_dishes:
        list.append(-dish.min / 100)
    return np.array(list)


def get_nutrient_matrix(selected_dishes):
    n = len(selected_dishes)
    rows = 7 + n
    cols = 7 + 2 * n
    matrix = np.zeros((rows, cols))
    for j in range(n):
        matrix[0][j] = -selected_dishes[j].calories
        matrix[1][j] = -selected_dishes[j].proteins
        matrix[2][j] = selected_dishes[j].proteins
        matrix[3][j] = -selected_dishes[j].carbs
        matrix[4][j] = selected_dishes[j].carbs
        matrix[5][j] = -selected_dishes[j].fats
        matrix[6][j] = selected_dishes[j].fats
    current_row = 7
    for current_col in range(0, n):
        matrix[current_row][current_col] = -1
        current_row += 1
    for i in range(rows):
        matrix[i][i + n] = 1
    return np.array(matrix)


def find_index_in_list(B, i):
    for j in range(len(B)):
        if B[j] == i:
            return j
    return -1


def correct_order(B, XB, n):
    list = []
    for i in range(n):
        position = find_index_in_list(B, i)
        list.append(round(XB[position], 2))
    return list


def get_amounts_of_selected_dishes(selected_dishes, nutrient_range):
    solution = calculate_amounts(selected_dishes, nutrient_range)
    if not solution:
        return False
    return correct_order(solution[0], solution[1], len(selected_dishes))


def calculate_amounts(selected_dishes, nutrient_range):
    c = get_prices_array(selected_dishes)
    b = get_edges_array(selected_dishes, nutrient_range)
    A = get_nutrient_matrix(selected_dishes)
    print("THEIR SIMPLEX")
    linprog_simplex(selected_dishes, nutrient_range)
    print("\n\n\nOUR SIMPLEX")
    print("c = ", c)
    print("b = ", b)
    print("A = ", A)
    return revised_simplex_method(c, b, A)


def get_prices_array_za_ugradjeni(selected_dishes):
    prices = []
    for dish in selected_dishes:
        prices.append(dish.price)
    return np.array(prices)


def get_nutrient_matrix_za_ugradjeni(selected_dishes):
    n = len(selected_dishes)
    rows = 7 + n
    cols = n
    matrix = np.zeros((rows, cols))
    for j in range(n):
        matrix[0][j] = -selected_dishes[j].calories
        matrix[1][j] = -selected_dishes[j].proteins
        matrix[2][j] = selected_dishes[j].proteins
        matrix[3][j] = -selected_dishes[j].carbs
        matrix[4][j] = selected_dishes[j].carbs
        matrix[5][j] = -selected_dishes[j].fats
        matrix[6][j] = selected_dishes[j].fats
        matrix[7 + j][j] = -1
    return np.array(matrix)


def linprog_simplex(selected_dishes, nutrient_range):
    c = get_prices_array_za_ugradjeni(selected_dishes)
    b = get_edges_array(selected_dishes, nutrient_range)
    A = get_nutrient_matrix_za_ugradjeni(selected_dishes)
    opt = linprog(c=c, A_ub=A, b_ub=b, method="revised simplex")
    print("c = ", c)
    print("b = ", b)
    print("A = ", A)
    print(" opt ", opt)
    return c, b, A
