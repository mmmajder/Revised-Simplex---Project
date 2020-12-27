import math

import numpy as np
from Dish import Dish

NUMBER_OF_VARIABLES = 2


def get_additonal_table(n, matrix):
    # print(len(matrix))
    print(n)
    return matrix[:, 1:n]


def getMax(B1, additional_table):
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


def get_results(calories_min, carbs_max, fat_max, list_of_dishes, protein_min):
    results = np.array([0.0, calories_min, protein_min, carbs_max, fat_max])
    for dish in list_of_dishes:
        results = np.append(results, dish.max)
        results = np.append(results, -dish.min)
    return results


def make_matrix(list_of_dishes, n):
    calories, carbs, fats, proteins, price = initialize_parameters()
    for dish in list_of_dishes:
        price.append(float(-dish.price))
        calories.append(float(-dish.calories))
        proteins.append(float(-dish.proteins))
        carbs.append(float(dish.carbs))
        fats.append(float(dish.fats))
    price += [0.0] * (2 * n + 4)
    identity_array = np.identity(2 * n + 4)
    calories += identity_array[0].tolist()
    proteins += identity_array[1].tolist()
    carbs += identity_array[2].tolist()
    fats += identity_array[3].tolist()
    price = np.array([price])
    calories = np.array([calories])
    proteins = np.array([proteins])
    carbs = np.array([carbs])
    fats = np.array([fats])
    matrix = np.concatenate((price, calories, proteins, carbs, fats), axis=0)
    min_max_dishes = []
    for i in range(len(list_of_dishes)):
        dishpoz = [0.0]
        dishpoz += [0.0] * i
        dishpoz += [1.0]
        dishpoz += [0.0] * (n - i - 1)
        dishpoz += identity_array[4 + 2 * i].tolist()
        dishneg = [0.0]
        dishneg += [0.0] * i
        dishneg += [-1.0]
        dishneg += [0.0] * (n - i - 1)
        dishneg += identity_array[4 + 2 * i + 1].tolist()
        # arr = numpy.array(lst)
        min_max_dishes.append(dishpoz)
        min_max_dishes.append(dishneg)
        dishpoz = np.array([dishpoz])
        dishneg = np.array([dishneg])
        matrix = np.concatenate((matrix, dishpoz, dishneg), axis=0)
    return matrix


def initialize_parameters():
    price = [1.]
    calories = [0.]
    proteins = [0.]
    carbs = [0.]
    fats = [0.]
    return calories, carbs, fats, proteins, price


def get_dishes(file_name):
    dishes = []
    file = open(file_name)
    for line in file.readlines():
        dishes.append(Dish(line.rstrip().split('|')))
    file.close()
    return dishes

def changeB1(B1, r, yk):
    # print(B1)
    for i in range(1, len(B1)):
        R = B1[:, i]
        R[r] = R[r] / yk[r]
        for j in range(len(R)):
            if j != r:
                R[j] = R[j] - yk[j] * R[r]
        B1[:, i] = R
    return B1



def create_solution(r, results, yk):
    R = np.array(results)
    R[r] = R[r] / yk[r]
    # print(R)
    for i in range(len(R)):
        if i != r:
            R[i] = R[i] - yk[i] * R[r]
    return R.tolist()


def start(A, results):
    n, m = A.shape
    B1 = np.identity(n)
    additional_table = get_additonal_table(NUMBER_OF_VARIABLES + 1, A)
    # print(additional_table)

    while True:
        # y1 = c1-z1
        ck_zk, k = getMax(B1, additional_table)
        if ck_zk < 0:
            break
        # print(k)
        # k - u kojoj koloni se nalazi najveci element
        # print(ck_zk)

        # print(additional_table[:, k])
        yk = np.matmul(np.matrix(B1), additional_table[:, k])
        # print(yk)
        min_ratio, r = find_min_ratio(results, yk)
        # print(min_ratio, r)

        results = create_solution(r, results, yk)
        # print(additional_table[:, k][0])
        print(B1[:, r])
        for i in range(len(additional_table[:, k])):
            # print(additional_table[:, k][i])
            print(B1[:, r][i])
            additional_table[:, k][i] = B1[:, r][i]

        print(additional_table[:, k])
        print(B1[:, r])
        additional_table[:, k] = B1[:, r]
        # for i in range(len(additional_table[:, r])):
        #     additional_table[:,r][i][0] = B1[:,k][i]

        B1 = changeB1(B1, r, yk)

        print(additional_table)
        print(results)
        print(B1)
        print("--------------------")
    print(results)


if __name__ == '__main__':
    # A = np.array([[1.0, -2.0, -1.0, 0.0, 0.0], [0.0, 3.0, 4.0, 1.0, 0.0], [0.0, 6.0, 1.0, 0.0, 1.0]])
    # results = [0.0, 6.0, 3.0]
    # DISHES = get_dishes("dishes.txt")
    #
    A = np.array([[1.0, -3.0, -5.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 1.0, 0.0],
                  [0.0, 3.0, 2.0, 0.0, 0.0, 1.0]])
    results = [0.0, 4.0, 6.0, 18.0]
    start(A, results)
