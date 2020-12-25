class Dish:
    def __init__(self, list):
        self.name = list[0]
        self.calories = int(list[1])
        # in %
        self.proteins = int(list[2])
        self.carbs = int(list[3])
        self.fats = int(list[4])
        # min and max amount of food to be eaten
        self.min = int(list[5])
        self.max = int(list[6])
        self.price = int(list[7])