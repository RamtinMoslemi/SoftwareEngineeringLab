from strategy import Standard, Express
from state import Transit, Delivered
from package import Package

if __name__ == '__main__':
    weight = float(input('Enter the weight of the package: '))
    command = input('Select a shipping strategy:\n1. Standard\n2. Express\n')
    strategy = Standard() if command == '1' else Express()
    pkg = Package(weight, strategy)

    while not pkg.has_been_delivered():
        command = input('Select an action:\n1. Change Shipping Strategy\n2. Update Package State\n3. Exit\n')
        if command == '1':
            command = input('Select a shipping strategy:\n1. Standard\n2. Express\n')
            new_strategy = Standard() if command == '1' else Express()
            pkg.update_strategy(new_strategy)
        elif command == '2':
            command = input('Select the package state:\n1. In-Transit\n2. Delivered\n')
            new_state = Transit() if command == '1' else Delivered()
            pkg.update_state(new_state)
        else:
            exit(0)
