Feature: count connected number of component

  Scenario: 0 vertex input
    Given an empty graph
    When number of components is calculated
    Then the number is "0"

  Scenario: complete graph input
    Given a complete graph
    When number of components is calculated
    Then the number is "1"

  Scenario: two component input
    Given a two component graph
    When number of components is calculated
    Then the number is "2"


