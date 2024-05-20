@tag
Feature: Calculator

  Scenario: add two numbers
    Given Two input values, 1 and 2
    When I add the two values
    Then I expect the result 3

  Scenario Outline: add two numbers
    Given Two input values, <first> and <second>
    When I add the two values
    Then I expect the result <result>

    Examples:
      | first | second | result |
      | 1     | 12     | 13     |
      | -1    | 6      | 5  	|
      | 2     | 2      | 4	    |

  Scenario: multiply two numbers
    Given Two input values, 3 and 2
    When I multiply the two values
    Then I expect the result 6

  Scenario Outline: add two numbers
    Given Two input values, <first> and <second>
    When I multiply the two values
    Then I expect the result <result>

    Examples:
      | first | second | result |
      | 7     | 12     | 84     |
      | 9     | 6      | 54  	|
      | 2     | 2      | 4	    |


  Scenario: raise to power
    Given Two input values, 4 and 5
    When I perform ^ on them
    Then I expect the result 1024


  Scenario Outline: fully functional calculator
    Given Two input values, <first> and <second>
    When I perform <opt> on them
    Then I expect the result <result>
    Examples:
      | first | second | opt | result |
      | 6     | 2      | *   | 12     |
      | 6     | 2      | /   | 3      |
      | 6     | 2      | ^   | 36     |

