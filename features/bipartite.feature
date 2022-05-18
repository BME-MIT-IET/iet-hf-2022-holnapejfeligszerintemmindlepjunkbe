Feature: Bipartite test

  Scenario: bipartite graph
    Given a bipartite graph
    When bipartite test is performed
    Then the result is bipartite

  Scenario: not bipartite graph
    Given a not bipartite graph
    When bipartite test is performed
    Then the result is not bipartite


