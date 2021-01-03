import numpy as np
from scipy.optimize import linprog


def example_parameters():
    c = np.array([3.0, 2.0, 6.0, 0.0, 0.0])
    b = np.array([5.0, 4.0])
    A = np.array([[4.0, 8.0, -1.0, 1.0, 0.0], [7.0, -2.0, 2.0, 0.0, -1.0]])
    return c, b, A


def example_parameters_2():
    obj = np.array([3.0, 2.0, 6.0])
    rhs_ineq = np.array([5.0, -4.0])
    lhs_ineq = np.array([[4.0, 8.0, -1.0], [-7.0, 2.0, -2.0]])
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
                  method="revised simplex")
    print(opt)


def example_parameters1():
    c = np.array([-2.0, 3.0, 0.0, 0.0])
    b = np.array([4.0, 6.0])
    A = np.array([[1.0, 1.0, 1.0, 0.0], [1.0, -1.0, 0.0, 1.0]])
    return c, b, A


def exmaple_parameters1_2():
    c = np.array([-2.0, 3.0])
    b = np.array([4.0, 6.0])
    A = np.array([[1.0, 1.0], [1.0, -1.0]])
    opt = linprog(c=c, A_ub=A, b_ub=b, method="revised simplex")
    print(" opt ", opt)


def ugradjeni():
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
    method = "revised simplex")
    print(opt)


def our_example():
    c = np.array([0.4, 1.5, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    A = np.array([[84.0, 120.0, 385.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [1.3, 2.2, 15.5, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [1.3, 2.2, 15.5, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [3.5, 2.2, 72.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [3.5, 2.2, 72.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.1, 12.1, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.1, 12.1, 2.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]])
    b = np.array([-2760.0, 204.0, -122.4, 425.0, -255.0, 92.0, -46.0, 2000.0, -0.5, 1000.5, -0.2, 1000.0, -0.3])
    #opt = linprog(c=c, A_ub=A, b_ub=b, method="revised simplex")
    #print(opt)
    return c, b, A


def example_parameters3():
    c = np.array([1.0, -1.0, 4.0, 0.0, 0.0])
    b = np.array([3.0, 1.0])
    A = np.array([[1.0, -1.0, 1.0, 1.0, 0.0], [-1.0, 1.0, 1.0, 0.0, 1.0]])
    opt = linprog(c=c, A_ub=A, b_ub=b, method="revised simplex")
    print(" opt ", opt)
    return c, b, A


def example_parameters4():
    obj = np.array([1.5, 0.4, 0.1])
    rhs_ineq = np.array([1590, -66.0, 88.0, -165.0, 275.0, -26.5, 165.0, -20.0, 150.0, -50.0, 200.0, -50.0, 200.0])
    lhs_ineq = np.array([[120.0, 365.0, 84.0], [2.2, 10.3, 0.1], [], [12.1], [20.0], [150.0]])
    # 120.0|2.2|2.2|12.1|20.0|150.0
    # All-purpose flour|365.0|10.3|73.4|1.0|10.0|100.0|0.1
    # Apple|84.0|1.3|3.5|0.1|50.0|200.0|0.4
    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
                  method="revised simplex")
    print(opt)