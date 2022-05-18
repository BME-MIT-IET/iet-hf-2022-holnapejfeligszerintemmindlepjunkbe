Feature: Check if graph is strongly connected

  Scenario: graph is k4
    Given a k4 complete graph
    When strong connection is checked
    Then the result shows that the graph is strongly connected

  Scenario: graph is a one way circle
    Given a one way path
    When strong connection is checked
    Then the result shows that the graph is not strongly connected




