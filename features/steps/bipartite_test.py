from behave import *

from algorithms.graph import check_bipartite

graph = {}
result = False


@given('a bipartite graph')
def init_bipartite(context):
    global graph
    graph = {0: [0, 1, 1, 0], 1: [1, 0, 0, 1], 2: [1, 0, 0, 0], 3: [0, 1, 0, 0]}


@given('a not bipartite graph')
def init_non_bipartite(context):
    global graph
    graph = {0: [0, 1, 1, 0], 1: [1, 0, 1, 0], 2: [1, 0, 0, 0], 3: [0, 0, 0, 0]}


@when('bipartite test is performed')
def perform_test(context):
    global graph, result
    result = check_bipartite(graph)


@then('the result is bipartite')
def check_result_is_success(context):
    global result
    assert (result == True)


@then('the result is not bipartite')
def check_result_is_fail(context):
    global result
    assert (result == False)


init_bipartite(0)
perform_test(0)
check_result_is_success(0)
