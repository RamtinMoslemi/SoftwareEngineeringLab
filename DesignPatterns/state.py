class State:
    def handle(self):
        raise NotImplemented


class Transit(State):
    def handle(self):
        print('Package is in transit ...')


class Delivered(State):
    def handle(self):
        print('Package has been delivered.')
