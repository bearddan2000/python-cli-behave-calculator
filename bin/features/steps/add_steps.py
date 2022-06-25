from behave import *

from main import add

@given('numbers {num1} and {num2}')
def the_number(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)

@when('I call add')
def call_to_function(context):
    context.result = add(context.num1, context.num2)

@then('I see {num}')
def compare_result(context, num):
    x = int(num)
    assert context.result == x, "Got %d" % x
