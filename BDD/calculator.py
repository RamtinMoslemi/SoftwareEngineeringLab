class Calculator:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        self.memory = 0

    def __add__(self, other):
        self.memory += other
        return self.memory

    def __mul__(self, other):
        self.memory *= other
        return self.memory

    def __sub__(self, other):
        self.memory -= other
        return self.memory

    def __floordiv__(self, other):
        self.memory //= other
        return self.memory

    def calculate(self, a, b, operation):
        if operation == '+':
            self.memory = a + b
        elif operation == '-':
            self.memory = a - b
        elif operation == '*':
            self.memory = a * b
        elif operation == '/':
            self.memory = a / b
        elif operation == '^':
            self.memory = a ** b
        else:
            raise 'Invalid Operation!'
        return self.memory

    def operate(self, operation):
        return self.calculate(self.a, self.b, operation)
