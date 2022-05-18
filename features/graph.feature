Feature: Graph processing

 Scenario: find all cliques
   Given we have a graph given by edges
   When we find all cliques
   Then the number of cliques is 3


 Scenario: find path
   Given we have a graph given by edges and a start and end vertex
   When we find a path
   Then path is 0-1-2

    Scenario: find shortest path between all pairs
      Given an adjacency array of the graph
      When we calculate the shortest path between all pairs
      Then we get the paths

  Scenario: cloning a graph
    Given an undirected graph to clone
    When using DFS algorithm to discover and clone
    Then the copy is identical to the original


