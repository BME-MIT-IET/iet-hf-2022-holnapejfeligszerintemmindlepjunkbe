from behave import *
from algorithms.graph.check_digraph_strongly_connected import *

graph = Graph   # Directed graph
result = False

@given('a k4 complete graph')
def init_strongly_connected_graph(context):
    global graph
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)


@given('a one way path')
def init_strongly_connected_graph(context):
    global graph
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)


@when('strong connection is checked')
def perform_check(context):
    global graph, result
    result = graph.is_strongly_connected()


@then('the result shows that the graph is strongly connected')
def check_result_is_strong(context):
    global result
    assert (result == True)


@then('the result shows that the graph is not strongly connected')
def check_result_is_strong(context):
    global result
    assert (result == False)
