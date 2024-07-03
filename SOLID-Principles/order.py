from food import Food
import datetime


class Order:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.foods = list()
        self.order_date = datetime.datetime.now()

    def add_item(self, food: Food):
        if food in self.foods:
            food.quantity += 1
        elif isinstance(food, Food):
            self.foods.append(food)
        else:
            raise 'Not a food'

    def get_total_price(self) -> float:
        return sum(self.foods)

    def __str__(self):
        string = 'Customer ' + self.customer_name + '\'s orders are:\n'
        for food in self.foods:
            string += '\t' + str(food) + '\n'
        string += 'Total Price is ' + str(self.get_total_price()) + '$'
        return string
