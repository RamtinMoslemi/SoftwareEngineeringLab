from behave import given, when, then
from package import Package
from strategy import Standard, Express


@given('A package with weight {weight:d}')
def step_given_packet_with_int_weight(context, weight):
    context.package = Package(weight=weight)


@given('A package with weight {weight:f}')
def step_given_packet_with_float_weight(context, weight):
    context.package = Package(weight=weight)


@when('We ship using the standard method')
def step_when_we_ship_standard(context):
    context.package.update_strategy(new_strategy=Standard())


@when('We ship using the express method')
def step_when_we_ship_express(context):
    context.package.update_strategy(new_strategy=Express())


@when('We ship using the {strategy} method')
def step_when_we_ship_using(context, strategy):
    if strategy == 'Standard':
        new_strategy = Standard()
    elif strategy == 'Express':
        new_strategy = Express()
    else:
        raise 'Invalid Strategy'
    context.package.update_strategy(new_strategy=new_strategy)


@then('The shipping cost will be {cost:f}')
def step_we_expect_float_cost(context, cost):
    assert context.package.get_cost() == cost, f"Expected {cost} but got {context.package.get_cost()}"


@then('The shipping cost will be {cost:d}')
def step_we_expect_int_cost(context, cost):
    assert context.package.get_cost() == cost, f"Expected {cost} but got {context.package.get_cost()}"
