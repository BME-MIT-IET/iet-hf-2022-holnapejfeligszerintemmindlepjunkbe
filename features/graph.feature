Feature: Graph

  Scenario: find all cliques
    Given we have a graph given by edges
    When we find all cliques
    Then the number of cliques is 1
