import math

import numpy as np
from prettytable import PrettyTable


def get_additonal_table(n, matrix):
    return matrix[:, 1:n + 1]


def display_additional_table(A):
    number_of_dishes = len(A[0]) - len(A)
    print(get_additonal_table(number_of_dishes, A))

def step3(B1, additional_table):
    first_row = B1[0]
    new_matrix = np.matmul(first_row, additional_table)
    new_matrix *= (-1)
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
    return min, position

def display_main_table(A, results, B1):
    additonal_table_variables, basis_table_variables = get_table_variables(A)
    additional_table = get_additonal_table(len(additonal_table_variables), A)
    table = create_main_table(B1, additional_table, additonal_table_variables, basis_table_variables, results)

    # while True:
    #     k - u kojoj koloni se nalazi najveci element
        # ck_zk, k = step3(B1, additional_table)
        # if ck_zk < 0:
        #     break
        # yk = np.matmul(np.matrix(B1), additional_table[:, k])
        # min_ratio, r = find_min_ratio(results, yk)




    print(table)


def create_main_table(B1, additional_table, additonal_table_variables, basis_table_variables, results):
    table = PrettyTable()
    table.add_column("B", basis_table_variables)
    table.add_column("XB", results)
    for i in range(len(basis_table_variables)):
        table.add_column(basis_table_variables[i], B1[i])
    table.add_column("yk", [""] * len(basis_table_variables))
    table.add_column("Min Ratio", ["---"] * len(basis_table_variables))
    for i in range(len(additonal_table_variables)):
        table.add_column(additonal_table_variables[i], additional_table[:, i])
    return table


def get_table_variables(A):
    additonal_table_variables = variables[1:len(A[0]) - len(A) + 1]
    basis_table_variables = [variables[0]]
    basis_table_variables += variables[len(A[0]) - len(A) + 1:]
    return additonal_table_variables, basis_table_variables


def calculate_ck_zk(B1, additional_table):
    first_row = B1[0]
    new_matrix = np.matmul(first_row, additional_table)
    new_matrix *= (-1)
    postion = np.where(new_matrix == np.amax(new_matrix))[0]
    return np.amax(new_matrix), postion


def revised_simplex_method(A, results, variables):
    B1 = display_B1(A)
    display_main_table(A, results, B1)
    calculate_ck_zk()


def display_B1(A):
    B1 = np.identity(len(A))
    table = PrettyTable(["B1", "MATRIX"])
    table.add_row(["B1", B1])
    print(table)
    return B1


def display_start_matrix(A, results, variables):
    table = PrettyTable(["MATRIX", "VARIABLES", "RESULTS"])
    for i in range(len(variables)):
        if i >= len(A):
            table.add_row(["", variables[i], ""])
        else:
            table.add_row([A[i], variables[i], results[i]])
    print(table)
    return variables


def generate_variables(A):
    variables = ["z"]
    m = len(A[0]) - len(A)
    for i in range(m):
        variables.append("x" + str(i + 1))
    for i in range(len(A) - 1):
        variables.append("s" + str(i + 1))
    return variables


def get_test_example_1():
    A = np.array([[1.0, -2.0, -1.0, 0.0, 0.0], [0.0, 3.0, 4.0, 1.0, 0.0], [0.0, 6.0, 1.0, 0.0, 1.0]])
    results = [0.0, 6.0, 3.0]
    return A, results

def get_test_example_2():
    A = np.array([[1.0, -3.0, -5.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 1.0, 0.0],
                  [0.0, 3.0, 2.0, 0.0, 0.0, 1.0]])
    results = [0.0, 4.0, 6.0, 18.0]
    return A, results

if __name__ == '__main__':
    # TEST EXAMPLE 1
    A = np.array([[1.0, -2.0, -1.0, 0.0, 0.0], [0.0, 3.0, 4.0, 1.0, 0.0], [0.0, 6.0, 1.0, 0.0, 1.0]])
    results = [0.0, 6.0, 3.0]
    variables = generate_variables(A)
    display_start_matrix(A, results, variables)
    revised_simplex_method(A, results, variables)

    print(25 * "-")
    # TEST EXAMPLE 2
    A = np.array([[1.0, -3.0, -5.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 1.0, 0.0],
                  [0.0, 3.0, 2.0, 0.0, 0.0, 1.0]])
    results = [0.0, 4.0, 6.0, 18.0]
    variables = generate_variables(A)
    display_start_matrix(A, results, variables)
    revised_simplex_method(A, results, variables)
