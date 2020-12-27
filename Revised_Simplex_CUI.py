from prettytable import PrettyTable

from Revised_Simplex_Method import get_test_example_1, generate_variables, display_B1, display_main_table


def display_start_matrix(A, results, variables):
    table = PrettyTable(["MATRIX", "VARIABLES", "RESULTS"])
    for i in range(len(variables)):
        if i >= len(A):
            table.add_row(["", variables[i], ""])
        else:
            table.add_row([A[i], variables[i], results[i]])
    print(table)
    return variables

def revised_simplex_cui():
    A, results = get_test_example_1()
    variables = display_start_matrix(A, results, generate_variables(A))
    B1 = display_B1(A)
    display_main_table(A, results, B1)


if __name__ == '__main__':
    revised_simplex_cui()