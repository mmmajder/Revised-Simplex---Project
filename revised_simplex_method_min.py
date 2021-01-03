from itertools import combinations

from examples import *


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


def phase_one(b, A):
    list_of_variables = list(range(len(A[0])))
    for B in combinations(list_of_variables, len(A)):
        A_on_B = get_A_on_B(A, B)
        try:
            A_on_B_inv = np.linalg.inv(A_on_B)
            XB = A_on_B_inv.dot(b)
            if np.all((XB > 0)):
                print(B)
                return A_on_B, A_on_B_inv, XB, list(B)
        except:
            continue
    return False


def revised_simplex_method(c, b, A):
    if phase_one(b, A):
        A_on_B, A_on_B_inv, XB, B = phase_one(b, A)
    else:
        return
    i = 0
    while True:
        cb = get_cb(c, B)
        if i != 0:
            XB = A_on_B_inv.dot(b)
        pi = cb.dot(A_on_B_inv)
        k = get_position_of_pivot(B, A, c, pi)
        if k == -1:
            break
        alfa = A_on_B_inv.dot(A[:, k])
        postion_j = get_min_XB_div_alfaB(XB, alfa)
        B[postion_j] = k
        A_on_B_inv = change_A_on_B_inv(A_on_B_inv, postion_j, alfa)
        i += 1

    print("-" * 100)
    print(B)
    print(XB)


if __name__ == '__main__':
    c, b, A = example_parameters()
    example_parameters_2()
    #     # c, b, A = example_parameters1()
    #     # exmaple_parameters1_2()
    #     c, b, A = our_example()
    #     revised_simplex_method(c, b, A)
    #     #ugradjeni()
    #     # c, b, A = example_parameters2()
    #     # c,b,A = example_parameters3()
    revised_simplex_method(c, b, A)
