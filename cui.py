import numpy as np
from scipy.optimize import linprog
from prettytable import PrettyTable

from logic import get_test_example_1, generate_variables, get_initial_B1, get_table_variables, get_additional_table, \
    get_ck_zk, get_yk, find_min_ratio, changeB1, change_Xb, change_additional_table, get_test_example_2, \
    get_test_example_3, get_test_example_4, get_test_example_5, get_test_example_6, get_test_example_res, \
    get_test_example_7


def display_start_matrix(A, results, variables):
    table = PrettyTable(["MATRIX", "VARIABLES", "RESULTS"])
    for i in range(len(variables)):
        if i >= len(A):
            table.add_row(["", variables[i], ""])
        else:
            table.add_row([A[i], variables[i], results[i]])
    print(table)


def display_B1(B1):
    table = PrettyTable(["B1", "MATRIX"])
    for i in range(len(B1)):
        table.add_row(["", B1[i]])
    print(table)


def display_main_table_not_filled(B1, additional_table, additional_table_variables, basis_table_variables, results):
    table = PrettyTable()
    table.add_column("B", basis_table_variables)
    table.add_column("XB", results)
    for i in range(len(basis_table_variables)):
        table.add_column(basis_table_variables[i], B1[:, i])
    table.add_column("yk", [""] * len(basis_table_variables))
    table.add_column("Min Ratio", ["---"] * len(basis_table_variables))
    for i in range(len(additional_table_variables)):
        table.add_column(additional_table_variables[i], additional_table[:, i])
    print(table)


def display_yk(yk, k):
    yk = yk[0].tolist()
    table = PrettyTable(["y" + str(k + 1), "MATRIX"])
    for i in range(len(yk[0])):
        table.add_row(["", yk[0][i]])
    print(table)


def display_main_table_filled(B1, additional_table, additional_table_variables, basis_table_variables, results, yk, k,
                              list_for_min_ratio):
    table = PrettyTable()
    table.add_column("B", basis_table_variables)
    table.add_column("XB", results)
    for i in range(len(basis_table_variables)):
        table.add_column(basis_table_variables[i], B1[:, i])
    table.add_column("y" + str(k + 1), yk.tolist()[0])
    table.add_column("Min Ratio", list_for_min_ratio)
    for i in range(len(additional_table_variables)):
        table.add_column(additional_table_variables[i], additional_table[:, i])
    print(table)


def display_solution_table(results, yk, basis_table_variables, B1, k, r):
    table = PrettyTable()
    list_of_R = []
    for i in range(len(results)):
        list_of_R.append("R" + str(i + 1))
    table.add_column("", list_of_R)
    table.add_column("XB", results)
    list_of_B = []
    for i in range(1, len(basis_table_variables)):
        list_of_B.append(B1[:, i])
        table.add_column(basis_table_variables[i], B1[:, i])
    table.add_column("y" + str(k + 1), yk.tolist()[0])
    print(table)


def revised_simplex_cui(A, results):
    B1, additional_table, additional_table_variables, basis_table_variables = phase1(A, results)
    num_of_iter = 0
    while True:
        num_of_iter = display_iteration_number(num_of_iter)
        ck_zk, k = step3(B1, additional_table, additional_table_variables, basis_table_variables, num_of_iter, results)
        if ck_zk < 0:
            break
        list_for_min_ratio, r, yk = step4(B1, additional_table, k, results)
        additional_table, additional_table_variables, basis_table_variables = step5(B1, additional_table,
                                                                                    additional_table_variables,
                                                                                    basis_table_variables, k,
                                                                                    list_for_min_ratio, r, results, yk)
        B1 = changeB1(B1, r, yk)
        results = change_Xb(results, r, yk)

    print(results)


def step5(B1, additional_table, additional_table_variables, basis_table_variables, k, list_for_min_ratio, r, results,
          yk):
    display_main_table_filled(B1, additional_table, additional_table_variables, basis_table_variables, results, yk,
                              k, list_for_min_ratio)
    print("We are going to change " + basis_table_variables[r] + " and " + additional_table_variables[k])
    display_solution_table(results, yk, basis_table_variables, B1, k, r)
    additional_table, additional_table_variables, basis_table_variables = change_additional_table(additional_table,
                                                                                                  additional_table_variables,
                                                                                                  B1,
                                                                                                  basis_table_variables,
                                                                                                  r, k)
    return additional_table, additional_table_variables, basis_table_variables


def step4(B1, additional_table, k, results):
    yk = get_yk(B1, additional_table, k)
    display_yk(yk, k)
    min_ratio, r, list_for_min_ratio = find_min_ratio(results, yk)
    print("XBr/Yrk = Min{XBi/Yik, Yik>0}")
    print("XB" + str(r) + "/Y" + str(r) + str(k + 1) + "=" + str(min_ratio))
    return list_for_min_ratio, r, yk


def step3(B1, additional_table, additional_table_variables, basis_table_variables, num_of_iter, results):
    ck_zk, k = get_ck_zk(B1, additional_table)
    display_main_table_not_filled(B1, additional_table, additional_table_variables, basis_table_variables, results)
    print("Ck-Zk=Max{(Cj-Zj)>0}")
    print("c" + str(k + 1) + "-z" + str(k + 1) + "=" + str(ck_zk))
    return ck_zk, k


def display_iteration_number(num_of_iter):
    num_of_iter += 1
    print("\n\n\n" + str(num_of_iter) + ". ITERATION")
    return num_of_iter


def phase1(A, results):
    print(A, results)
    variables = generate_variables(A)
    print(variables)
    display_start_matrix(A, results, generate_variables(A))
    B1 = get_initial_B1(A)
    display_B1(B1)
    additional_table_variables, basis_table_variables = get_table_variables(A, variables)
    additional_table = get_additional_table(len(additional_table_variables), A)
    return B1, additional_table, additional_table_variables, basis_table_variables


def integrated_simplex():
    # obj = [-2.0, 1.0]
    # lhs_ineq = [[-3.0, 2.0],
    #             [2.0, -4.0],
    #             [1.0, 1.0]]
    # rhs_ineq = [2, 3, 6]

    # obj = [-2.0, 3.0]
    # lhs_ineq = [[1.0, 1.0],
    #             [1.0, -1.0]]
    # rhs_ineq = [4, 6]

    #
    # obj = [-40.0, -200.0, -50.0]
    # lhs_ineq = [[-100.0, -150.0, -25.0],
    #             [-10.0, -25.0, -15.0],
    #             [10.0, 15.0, 15.0],
    #             [80.0, 60.0, 70.0],
    #             [1.0, 0.0, 0.0],
    #             [-1.0, 0.0, 0.0],
    #             [0.0, 1.0, 0.0],
    #             [0.0, -1.0, 0.0],
    #             [0.0, 0.0, 1.0],
    #             [0.0, 0.0, -1.0]]
    # rhs_ineq = [-2369.0, -144.0, 316.0, 67.0, 300.0, -50.0, 500.0, -50.0, 200.0, -10.0]

    obj = [0.4, 1.5, 0.8]
    lhs_ineq = [[-84.0, -120.0, -385.0],
                [1.3, 2.2, 15.5],
                [-1.3, -2.2, -15.5],
                [3.5, 2.2, 72.0],
                [-3.5, -2.2, -72.0],
                [0.1, 12.1, 2.5],
                [-0.1, -12.1, -2.5],
                [1.0, 0.0, 0.0],
                [-1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, -1.0, 0.0],
                [0.0, 0.0, 1.0],
                [0.0, 0.0, -1.0]]
    rhs_ineq = [-2760.0, 204.0, -122.4, 425.0, -255.0, 92.0, -46.0, 2000.0, -0.5, 1000.5, -0.2, 1000.0, -0.3]

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
                  method="revised simplex")
    return opt


if __name__ == '__main__':
    # A, results = get_test_example_1()
    # A, results = get_test_example_2()

    # A, results = get_test_example_4()
    # revised_simplex_cui(A, results)
    # print("-"*100)
    # A, results = get_test_example_5()
    # A, results = get_test_example_7()

    A, results = get_test_example_res()

    # A, results = get_test_example_3()
    revised_simplex_cui(A, results)
    print("-" * 100)
    opt = integrated_simplex()
    print(opt)
