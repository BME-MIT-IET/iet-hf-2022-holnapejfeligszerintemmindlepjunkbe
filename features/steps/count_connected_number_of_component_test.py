from behave import *

from algorithms.graph.count_connected_number_of_component import count_components

number_of_components = 0
graph = {}


@given('an empty graph')
def init_empty_graph(context):
    global graph
    graph = {}


@given('a complete graph')
def init_complete_graph(context):
    global graph
    graph = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}


@given('a two component graph')
def init_two_component_graph(context):
    global graph
    graph = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}, 4: {5}, 5: {4}}


@when('number of components is calculated')
def count_number_of_components(context):
    global graph, number_of_components
    number_of_components = count_components(graph, len(graph))


@then('the number is "{number}"')
def check_number_of_components(context, number):
    global number_of_components
    assert (number_of_components == int(number))


init_complete_graph(0)
count_number_of_components(0)
check_number_of_components(0, 1)
