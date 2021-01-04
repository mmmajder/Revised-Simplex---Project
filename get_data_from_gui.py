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
        list.append(-dish.min)
    return np.array(list)


def get_nutrient_matrix(selected_dishes):
    n = len(selected_dishes)
    print("n = ", n)
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
    print(matrix)
    return np.array(matrix)


def calculate_amounts(selected_dishes, nutrient_range):
    c = get_prices_array(selected_dishes)
    b = get_edges_array(selected_dishes, nutrient_range)
    A = get_nutrient_matrix(selected_dishes)
    print("c = ", c)
    print("b = ", b)
    print("A = ", A)
    revised_simplex_method(c, b, A)
    ugradjeni(selected_dishes, nutrient_range)


def get_prices_array_za_ugradjeni(selected_dishes):
    prices = []
    for dish in selected_dishes:
        prices.append(dish.price)
    return np.array(prices)


def get_nutrient_matrix_za_ugradjeni(selected_dishes):
    n = len(selected_dishes)
    print("n = ", n)
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
    return np.array(matrix)


def ugradjeni(selected_dishes, nutrient_range):
    c = get_prices_array_za_ugradjeni(selected_dishes)
    b = get_edges_array(selected_dishes, nutrient_range)
    A = get_nutrient_matrix_za_ugradjeni(selected_dishes)
    opt = linprog(c=c, A_ub=A, b_ub=b, method="revised simplex")
    print("c = ", c)
    print("b = ", b)
    print("A = ", A)
    print(" opt ", opt)
    return c, b, A