
from behave import *

from algorithms.graph.clone_graph import *

graph_origin = UndirectedGraphNode('origin')
clone = UndirectedGraphNode('a')


@given('an undirected graph to clone')
def init_graph(context):
    global graph_origin
    node1 = UndirectedGraphNode('middle')
    node2 = UndirectedGraphNode('end')
    node1.add_neighbor(node2)
    graph_origin.add_neighbor(node1)


@when('using DFS algorithm to discover and clone')
def clone_using_recurs_DFS(context):
    global clone
    clone = clone_graph(graph_origin)


@then('the copy is identical to the original')
def check_clone(context):
    global clone
    assert(clone.label == 'origin'
           and clone.neighbors[0].label == 'middle'
           and clone.neighbors[0].neighbors[0].label == 'end'
           )

# For testing BDD test syntax:
init_graph(0)
clone_using_recurs_DFS(0)
check_clone(0)

