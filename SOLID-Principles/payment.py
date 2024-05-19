class OrderService:
    def register(self, customer_name):
        raise NotImplementedError

    def payment(self, price):
        raise NotImplementedError


class OnlineOrderService(OrderService):
    def register(self, customer_name):
        print('online order registered for ' + customer_name)

    def payment(self, price):
        print('online payment with price : ' + str(price) + '$')


class OnSiteOrderService(OrderService):
    def register(self, customer_name):
        print('on-site order registered for ' + customer_name)

    def payment(self, price):
        print('on-site payment with price : ' + str(price) + '$')
