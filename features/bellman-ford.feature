Feature: Bellman-ford test
  Scenario: test fail
    Given a graph given with negative circle
    When running Bellman-ford algorithm
    Then the result is fail

  Scenario: test success
    Given a graph given with no negative circle
    When running Bellman-ford algorithm
    Then the result is success

  Scenario: empty graph
    Given a graph given with no vertices
    When running Bellman-ford algorithm
    Then the result is success
