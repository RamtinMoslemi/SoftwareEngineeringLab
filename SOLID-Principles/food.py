class Food:
    def __init__(self, food_name: str, food_price: float):
        self.name = food_name
        self.price = food_price
        self.quantity = 1

    def __radd__(self, other):
        return other + self.price * self.quantity

    def __str__(self):
        return str(self.quantity) + ' x ' + self.name + ' ' + str(self.price) + '$'
