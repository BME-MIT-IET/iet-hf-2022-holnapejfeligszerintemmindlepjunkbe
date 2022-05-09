from behave import *

cliques = []
edges = []


@given('we have a graph given by edges')
def init_graph(context):
    edges = [[0, 1], [1, 2], [2, 0]]


@when('we find all cliques')
def init_graph(context):
    from algorithms.graph.find_all_cliques import find_all_cliques
    cliques = find_all_cliques(edges)


@then('the number of cliques is 1')
def init_graph(context):
    assert (len(cliques) == 3)
