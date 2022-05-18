from behave import *

from algorithms.graph import all_pairs_shortest_path
from algorithms.graph.find_path import *

path = []
graph = []
start = 0
end = 0


@given('we have a graph given by edges and a start and end vertex')
def init_graph(context):
    global graph, start, end
    graph = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
    start = 0
    end = 2


@when('we find a path')
def execute_find(context):
    global graph, start, end, path
    path = find_path(graph, start, end, [])


@then('path is 0-1-2')
def assert_result(context):
    global path
    print(path)
    assert(len(path) == 3 and path[0] == 0 and path[1] == 1 and path[2] == 2)

init_graph(0)
execute_find(0)
assert_result(0)

a = []
shortest_path_result = []


@given('an adjacency array of the graph')
def init_adj_graph(context):
    global a
    a = [[0, 0.1, 0.101, 0.142, 0.277],
         [0.465, 0, 0.191, 0.192, 0.587],
         [0.245, 0.554, 0, 0.333, 0.931],
         [1.032, 0.668, 0.656, 0, 0.151],
         [0.867, 0.119, 0.352, 0.398, 0]]


@when('we calculate the shortest path between all pairs')
def calculate_shortest_paths(context):
    global a, shortest_path_result
    shortest_path_result = all_pairs_shortest_path(a)


@then('we get the paths')
def assert_shortest_paths(context):
    global shortest_path_result
    assert(len(shortest_path_result) == 5)

