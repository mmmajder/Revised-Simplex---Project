import numpy as np

from revised_simplex_method_min import revised_simplex_method


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
    return np.array(list)


def get_nutrient_matrix(selected_dishes):
    n = len(selected_dishes)
    rows = 7 + 2 * n
    cols = 7 + 3 * n
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
        matrix[current_row + 1][current_col] = 1
        current_row += 2
    for i in range(rows):
        matrix[i][i + n] = 1
    return np.array(matrix)


def calculate_amounts(selected_dishes, nutrient_range):
    c = get_prices_array(selected_dishes)
    b = get_edges_array(selected_dishes, nutrient_range)
    A = get_nutrient_matrix(selected_dishes)
    print("c = ", c)
    print("b = ", b)
    print("A = ", A)
    revised_simplex_method(c, b, A)

