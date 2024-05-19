from behave import given, when, then
from calculator import Calculator


@given('Two input values, {a:d} and {b:d}')
def step_given_two_input_values(context, a, b):
    context.calculator = Calculator(a, b)


@when('I add the two values')
def step_when_i_add_the_two_values(context):
    context.result = context.calculator.calculate(context.calculator.a, context.calculator.b, '+')


@when('I perform {operation} on them')
def step_when_i_perform_operation_on_them(context, operation):
    context.result = context.calculator.calculate(context.calculator.a, context.calculator.b, operation)


@then('I expect the result {expected_result:d}')
def step_then_i_expect_the_result(context, expected_result):
    assert context.result == expected_result, f"Expected {expected_result} but got {context.result}"
