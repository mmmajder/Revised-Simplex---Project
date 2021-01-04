class Dish:
    def __init__(self, list):
        self.name = list[0]
        # in g on 100g of food
        self.calories = float(list[1])
        self.proteins = round(float(list[2]), 1)
        self.carbs = round(float(list[3]), 1)
        self.fats = round(float(list[4]), 1)
        # min and max amount of food recommended to be eaten
        self.min = round(float(list[5]), 1)
        self.price = round(float(list[6]), 1)

    def to_string(self):
        return str(self.name + '|' +
                   str(self.calories) + '|' +
                   str(self.proteins) + '|' +
                   str(self.carbs) + '|' +
                   str(self.fats) + '|' +
                   str(self.min) + '|' +
                   str(self.price) + '\n')
