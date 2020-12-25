from calculator_gui import start_calculator
from Dish import Dish


def get_dishes(file_name):
    dishes = []
    file = open(file_name)
    for line in file.readlines():
        dishes.append(Dish(line.rstrip().split('|')))
    file.close()
    return dishes

if __name__ == '__main__':
    # DISHES = get_dishes("dishes.txt")
    # print(DISHES)
    start_calculator()