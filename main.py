from Amounts_gui import start_amount
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
    # start_calculator()
    start_amount()
