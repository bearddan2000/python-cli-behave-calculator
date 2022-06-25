Feature: Simple calculator

    Scenario Outline: Add numbers
        Given numbers <num1> and <num2>
        When I call add
        Then I see <result>
    Examples:
    | num1 | num2 | result |
    | 1    |    1 |      2 |
    | 1    |    2 |      3 |
    | 1    |    3 |      4 |
