from behave import *

from algorithms.graph.find_all_cliques import find_all_cliques

cliques = []
edges = []


@given('we have a graph given by edges')
def init_graph(context):
    global edges
    edges = {'0': {0, 1}, '1': {1, 2}, '2': {2, 0}}


@when('we find all cliques')
def execute_find(context):
    global edges, cliques
    cliques = find_all_cliques(edges)


@then('the number of cliques is 3')
def assert_result(context):
    global cliques
    assert (len(cliques) == 3)

