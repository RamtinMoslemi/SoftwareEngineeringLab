class Strategy:
    def get_cost(self, weight):
        raise NotImplemented


class Standard(Strategy):
    def get_cost(self, weight):
        cost = weight * 2.5
        print(f'Standard Shipping Cost is {cost}$')
        return cost


class Express(Strategy):
    def get_cost(self, weight):
        cost = weight * 3.5
        print(f'Express Shipping Cost is {cost}$')
        return cost
