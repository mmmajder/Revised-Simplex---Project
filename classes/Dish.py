class Dish:
    def __init__(self, list):
        self.name = list[0]
        self.calories = int(list[1])
        # in %
        self.proteins = int(list[2])
        self.carbs = int(list[3])
        self.fats = int(list[4])
        # min and max amount of food to be eaten
        self.min = float(list[5])
        self.max = float(list[6])
        self.price = float(list[7])

    def to_string(self):
        return str(self.name + '|' +
                   str(self.calories) + '|' +
                   str(self.proteins) + '|' +
                   str(self.carbs) + '|' +
                   str(self.fats) + '|' +
                   str(self.min) + '|' +
                   str(self.max) + '|' +
                   str(self.price) + '\n')
