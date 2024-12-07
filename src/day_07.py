from math import floor, log10
from operator import add, mul


def parse(lines):
    calibration_equations = []
    for line in lines:
        test_value_str, equation_values_str = line.split(": ")
        test_value = int(test_value_str)
        equation_values = list(map(int, equation_values_str.split()))
        calibration_equations.append((test_value, equation_values))
    return calibration_equations


def apply_operators(test_value, lhs, rhs_list, operators):
    for operator in operators:
        new_lhs = operator(lhs, rhs_list[0])
        if new_lhs > test_value:
            continue
        elif new_rhs_list := rhs_list[1:]:
            yield from apply_operators(test_value, new_lhs, new_rhs_list, operators)
        else:
            yield new_lhs


def part_1(calibration_equations):
    operators = (add, mul)
    return sum(test_value for test_value, equation_values in calibration_equations if
               test_value in apply_operators(test_value, equation_values[0], equation_values[1:], operators))


def concat(a, b):
    return a * 10 ** floor(log10(b) + 1) + b


def part_2(calibration_equations):
    operators = (add, mul, concat)
    return sum(test_value for test_value, equation_values in calibration_equations if
               test_value in apply_operators(test_value, equation_values[0], equation_values[1:], operators))
