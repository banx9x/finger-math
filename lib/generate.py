from random import randint, choice
from enum import Enum


class Operator(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    GROUP = "()"


def generator(allow_operators, num_of_operands, min_operand, max_operand, allow_negative, previous_expression=None,
              previous_operator=None, previous_operand=None):
    """Generate random math expression"""
    current_value = 0

    if previous_expression:
        current_value = eval(previous_expression)

    if num_of_operands == 1:
        if previous_operator == Operator.SUB and not allow_negative:
            last_operand = randint(min_operand, max(min_operand, min(current_value, max_operand)))
        else:
            last_operand = randint(min_operand, max_operand)

        return f"{previous_expression} {previous_operator.value} {last_operand}"
    else:
        if previous_expression is not None and previous_operator is not None:
            if previous_operator == Operator.SUB and not allow_negative:
                next_operand = randint(min_operand, max(min_operand, min(current_value, max_operand)))
            else:
                next_operand = randint(min_operand, max_operand)

            next_expression = f"{previous_expression} {previous_operator.value} {next_operand}"

            if eval(next_expression) == 0 and not allow_negative:
                next_operator = Operator.ADD
            else:
                next_operator = choice(allow_operators)

            return generator(allow_operators, num_of_operands - 1, min_operand, max_operand, allow_negative,
                             next_expression, next_operator, next_operand)
        else:
            first_operand = randint(min_operand, max_operand)
            first_operator = choice(allow_operators)
            first_expression = f"{first_operand}"

            return generator(allow_operators, num_of_operands - 1, min_operand, max_operand, allow_negative,
                             first_expression, first_operator, first_operand)

