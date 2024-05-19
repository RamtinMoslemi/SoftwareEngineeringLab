from payment import *
from order import Order
from food import Food

if __name__ == '__main__':
    customer_name = input('Enter Customer Name: ')
    order = Order(customer_name)

    sandwich = Food('Sandwich', 10)
    pizza = Food('Pizza', 20)

    while True:
        command = input('1. Order Sandwich 10$\n2. Order Pizza 20$\n3. Submit Order\n')
        if command == '1':
            order.add_item(sandwich)
        elif command == '2':
            order.add_item(pizza)
        elif command == '3':
            break

    method = input('Enter Your Payment Method (1 for online and 2 for on-site): ')
    order_service = OnlineOrderService() if method == '1' else OnSiteOrderService()

    print('Pay Price:')
    order_service.payment(order.get_total_price())

    print(order)
