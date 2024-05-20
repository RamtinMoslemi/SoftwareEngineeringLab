@tag
Feature: Shipping Cost

  Scenario: Standard Shipping
    Given A package with weight 100
    When We ship using the standard method
    Then The shipping cost will be 250

  Scenario: Express Shipping
    Given A package with weight 100
    When We ship using the express method
    Then The shipping cost will be 350

  Scenario Outline: Shipping
    Given A package with weight <weight>
    When We ship using the <strategy> method
    Then The shipping cost will be <cost>

    Examples:
      | weight | strategy | cost |
      | 1      | Standard | 2.5  |
      | 10.0   | Standard | 25   |
      | 15.0   | Standard | 37.5 |
      | 20     | Standard | 50   |
      | 1      | Express  | 3.5  |
      | 10.0   | Express  | 35   |
      | 15.0   | Express  | 52.5 |
      | 20     | Express  | 70   |