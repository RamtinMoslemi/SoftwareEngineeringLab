class OrderService:
    def register(self, customer_name):
        raise NotImplementedError

    def payment(self, price: float):
        raise NotImplementedError


class OnlineOrderService(OrderService):
    def register(self, customer_name: str):
        print('online order registered for ' + customer_name)

    def payment(self, price: float):
        print('online payment with price : ' + str(price) + '$')


class OnSiteOrderService(OrderService):
    def register(self, customer_name: str):
        print('on-site order registered for ' + customer_name)

    def payment(self, price: float):
        print('on-site payment with price : ' + str(price) + '$')
