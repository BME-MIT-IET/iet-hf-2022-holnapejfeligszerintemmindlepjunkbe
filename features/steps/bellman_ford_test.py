from behave import *

from algorithms.graph import bellman_ford

graph = {}
result = False


@given('a graph given with negative circle')
def init_graph_with_neagtive_circle(context):
    global graph
    graph = {'a': {'b': 2, 'c': -6},
             'b': {'a': 4},
             'c': {'b': 1}
             }


@given('a graph given with no negative circle')
def init_graph_without_neagtive_circle(context):
    global graph
    graph = {'a': {'b': 2, 'c': -1},
             'b': {'a': 4},
             'c': {'b': 1}
             }

@given('a graph given with no vertices')
def init_empty_graph(context):
    global graph
    graph = {}


@when('running Bellman-ford algorithm')
def run_bellman_ford(context):
    global graph, result
    result = bellman_ford(graph, 'a')


@then('the result is success')
def check_result_success(context):
    global result
    assert (True == result)


@then('the result is fail')
def check_result_fail(context):
    global result
    assert (False == result)





init_graph_without_neagtive_circle(0)
run_bellman_ford(0)
check_result_success(0)

