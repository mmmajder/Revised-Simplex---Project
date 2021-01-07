import math
from itertools import combinations

import numpy as np
from scipy.optimize import linprog

NO_SOLUTION = False


def linprog_example():
    obj = [0.4, 1.5, 0.8]
    lhs_ineq = [[-84.0, -120.0, -385.0],
                [1.3, 2.2, 15.5],
                [-1.3, -2.2, -15.5],
                [3.5, 2.2, 72.0],
                [-3.5, -2.2, -72.0],
                [0.1, 12.1, 2.5],
                [-0.1, -12.1, -2.5],
                [-1.0, 0.0, 0.0],
                [0.0, -1.0, 0.0],
                [0.0, 0.0, -1.0]]

    rhs_ineq = [-2760.0, 204.0, -122.4, 425.0, -255.0, 92.0, -46.0, -0.5, -0.2, -0.3]
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")
    print(opt)


def our_example():
    c = np.array([0.4, 1.5, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    A = np.array([[-84.0, -120.0, -385.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [1.3, 2.2, 15.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [-1.3, -2.2, -15.5, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [3.5, 2.2, 72.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [-3.5, -2.2, -72.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.1, 12.1, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                  [-0.1, -12.1, -2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                  [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                  [0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
    b = np.array([-2760.0, 204.0, -122.4, 425.0, -255.0, 255.0, -46.0, -0.5, -0.2, -0.3])
    return c, b, A


def get_list_B(b):
    return list(range(0, len(b)))


def get_A_on_B(A, list_B):
    return A[:, list_B]


def get_cb(c, list_B):
    return c[list(list_B)]


def get_position_of_pivot(list_B, A, c, pi):
    for position in range(len(A[0, :])):
        if position not in list_B:
            x = c[position] - pi.dot(A[:, position])
            if x < 0:
                return position
    return -1


def get_min_pos_XB_div_alfaB(XB, alfa):
    min = math.inf
    position_min = -1
    for i in range(len(XB)):
        if alfa[i] <= 10e-6:
            continue
        if XB[i] / alfa[i] > 0:
            if XB[i] / alfa[i] < min:
                min = XB[i] / alfa[i]
                position_min = i
    return position_min


def get_min_XB_div_alfaB(XB, alfa):
    min_XB_dev_alfaB = min(XB / alfa)
    position = np.where(XB / alfa == min_XB_dev_alfaB)
    return position[0][0]


def change_A_on_B_inv(A_on_B_inv, postion_j, alfa):
    for i in range(len(A_on_B_inv)):
        R = A_on_B_inv[:, i]
        R[postion_j] = float(R[postion_j]) / float(alfa.item(postion_j))
        for j in range(len(R)):
            if j != postion_j:
                R[j] = R[j] - alfa.item(j) * R[postion_j]
        A_on_B_inv[:, i] = R
    return A_on_B_inv


def get_combination_of_variables(A, i):
    return combinations(len(A[0]), len(A))


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
    global NO_SOLUTION
    NO_SOLUTION = True
    return [], [], [], []


def revised_simplex_method(c, b, A):
    A_on_B, A_on_B_inv, XB, B = phase_one(b, A)
    if NO_SOLUTION:
        print("no solution")
        return []
    while True:
        cb = get_cb(c, B)
        pi = cb.dot(A_on_B_inv)
        k = get_position_of_pivot(B, A, c, pi)
        if k == -1:
            break
        alfa = A_on_B_inv.dot(A[:, k])
        postion_j = get_min_pos_XB_div_alfaB(XB, alfa)
        B[postion_j] = k
        A_on_B_inv = change_A_on_B_inv(A_on_B_inv, postion_j, alfa)
        XB = A_on_B_inv.dot(b)

    print(B)
    print(XB)
    return [B, XB]


if __name__ == '__main__':
    c, b, A = our_example()
    revised_simplex_method(c, b, A)
    linprog_example()
