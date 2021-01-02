import math

import numpy as np
from prettytable import PrettyTable
from numpy.linalg import inv


def get_test_example_1():
    A = np.array([[1.0, -2.0, -1.0, 0.0, 0.0], [0.0, 3.0, 4.0, 1.0, 0.0], [0.0, 6.0, 1.0, 0.0, 1.0]])
    results = np.array([[0.0], [6.0], [3.0]])
    return A, results


def get_test_example_2():
    A = np.array([[1.0, -3.0, -5.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 1.0, 0.0],
                  [0.0, 3.0, 2.0, 0.0, 0.0, 1.0]])
    results = np.array([0.0, 4.0, 6.0, 18.0])
    return A, results


def get_test_example_3():
    A = np.array([[1.0, -2.0, 3.0, 0.0, 0.0], [0.0, 1.0, 1.0, 1.0, 0.0], [0.0, 1.0, -1.0, 0.0, 1.0]])
    results = np.array([0.0, 4.0, 6.0])
    return A, results
def get_test_example_7():
    A = np.array([[1.0, 1.0, -1.0, 4.0, 0.0, 0.0], [0.0, 1.0, -1.0, 1.0, 1.0, 0.0], [0.0, -1.0, 1.0, 1.0, 0.0, 1.0]])
    results = np.array([0.0, 3.0, 1.0])
    return A, results

def get_test_example_res():
    A = np.array([[1.0, 0.4, 1.5, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, -84.0, -120.0, -385.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 1.3, 2.2, 15.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, -1.3, -2.2, -15.5, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 3.5, 2.2, 72.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, -3.5, -2.2, -72.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.1, 12.1, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, -0.1, -12.1, -2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
    results = np.array([0.0, -2760.0, 204.0, -122.4, 425.0, -255.0, 92.0, -46.0, 2000.0, -0.5, 1000.5, -0.2, 1000.0, -0.3])

    # obj = [0.4, 1.5, 0.8]
    # lhs_ineq = [[-84.0, -120.0, -385.0],
    #             [1.3, 2.2, 15.5],
    #             [-1.3, -2.2, -15.5],
    #             [3.5, 2.2, 72.0],
    #             [-3.5, -2.2, -72.0],
    #             [0.1, 12.1, 2.5],
    #             [-0.1, -12.1, -2.5],
    #             [1.0, 0.0, 0.0],
    #             [-1.0, 0.0, 0.0],
    #             [0.0, 1.0, 0.0],
    #             [0.0, -1.0, 0.0],
    #             [0.0, 0.0, 1.0],
    #             [0.0, 0.0, -1.0]]
    # rhs_ineq = [-2760.0, 204.0, -122.4, 425.0, -255.0, 92.0, -46.0, 2.0, -0.5, 1.5, -0.2, 1.0, -0.3]
    return A, results

    # obj = [-40.0, -200.0, -50.0]
    # lhs_ineq = [[-100.0, -150.0, -25.0],
    #             [-10.0, -25.0, -15.0],
    # [10.0, 15.0, 15.0],
    # [80.0, 60.0, 70.0],
    # [1.0, 0.0, 0.0],
    # [-1.0, 0.0, 0.0],
    # [0.0, 1.0, 0.0],
    # [0.0, -1.0, 0.0],
    # [0.0, 0.0, 1.0],
    # [0.0, 0.0, -1.0]]
    # rhs_ineq = [-2369.0, -144.0, 316.0, 67.0, 300.0, -50.0, 500.0, -50.0, 200.0, -10.0]


def get_test_example_4():
    A = np.array([[1.0, -60.0, -30.0, -20.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 8.0, 6.0, 1.0, 1.0, 0.0, 0.0, 0.0],
                  [0.0, 4.0, 2.0, 1.5, 0.0, 1.0, 0.0, 0.0],
                  [0.0, 2.0, 1.5, 0.5, 0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]])
    results = np.array([0.0, 48.0, 20.0, 8.0, 5.0])
    return A, results


def get_test_example_5():
    A = np.array([[1.0, -20.0, -12.0, -40.0, -25.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0],
                  [0.0, 3.0, 2.0, 1.0, 0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0, 2.0, 3.0, 0.0, 0.0, 1.0]])
    results = np.array([0.0, 50.0, 100.0, 90.0])
    return A, results


def get_test_example_6():
    A = np.array([[1.0, -2.0, 1.0, 0.0, 0.0, 0.0],
                  [0.0, -3.0, 2.0, 1.0, 0.0, 0.0],
                  [0.0, 2.0, -4.0, 0.0, 1.0, 0.0],
                  [0.0, 1.0, 1.0, 0.0, 0.0, 1.0]])
    results = np.array([0.0, 2.0, 3.0, 6.0])
    return A, results


def generate_variables(A):
    variables = ["z"]
    m = len(A[0]) - len(A)
    for i in range(m):
        variables.append("x" + str(i + 1))
    for i in range(len(A) - 1):
        variables.append("s" + str(i + 1))
    return variables


def get_initial_B1(A):
    return np.eye(len(A), dtype=float)


def get_table_variables(A, variables):
    additonal_table_variables = variables[1:len(A[0]) - len(A) + 1]
    basis_table_variables = [variables[0]]
    basis_table_variables += variables[len(A[0]) - len(A) + 1:]
    return additonal_table_variables, basis_table_variables


def get_additional_table(n, matrix):
    return matrix[:, 1:n + 1]


def get_ck_zk(B1, additional_table):
    first_row = B1[0]
    new_matrix = (np.matmul(first_row, additional_table)) * (-1)
    position = np.where(new_matrix == np.amax(new_matrix))[0]
    return np.amax(new_matrix), position[0]


def get_yk(B1, additional_table, k):
    return np.matmul(np.matrix(B1), additional_table[:, k])


def find_min_ratio(results, yk):
    min = math.inf
    position = math.inf
    list_for_min_ratio = []
    for i in range(len(results)):
        if yk.item(0, i) > 0:
            value = results[i] / yk.item(0, i)
            list_for_min_ratio.append(value)
            if value < min:
                min = value
                position = i
        else:
            list_for_min_ratio.append("---")

    return min, position, list_for_min_ratio


def change_Xb(results, r, yk):
    results[r] = results[r] / yk.item(r)
    for j in range(len(results)):
        if j != r:
            results[j] = results[j] - yk.item(j) * results[r]
    return results


def changeB1(B1, r, yk):
    for i in range(1, len(B1)):
        R = B1[:, i]
        R[r] = float(R[r]) / float(yk.item(r))
        for j in range(len(R)):
            if j != r:
                R[j] = R[j] - yk.item(j) * R[r]
        B1[:, i] = R
    return B1


def change_additional_table(additional_table, additional_table_variables, B1, basis_table_variables, r, k):
    additional_table[:, k] = B1[:, r]
    basis_table_variables[r], additional_table_variables[k] = additional_table_variables[k], basis_table_variables[r]
    return additional_table, additional_table_variables, basis_table_variables
