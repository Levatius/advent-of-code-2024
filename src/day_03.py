import math
import re
from enum import StrEnum


class Operator(StrEnum):
    MULTIPLY = "mul"
    DO = "do"
    DONT = "don't"


def parse(line):
    instructions = []
    for instruction_str in re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", line):
        operator, operand_str = re.match(r"([\w']+)\((.*)\)", instruction_str).groups()
        operands = tuple(map(int, operand_str.split(","))) if operand_str else None
        instructions.append((operator, operands))
    return instructions


def part_1(instructions):
    return sum(math.prod(operands) for operator, operands in instructions if operator == Operator.MULTIPLY)


def part_2(instructions):
    total = 0
    multiply_enabled = True
    for operator, operands in instructions:
        match operator:
            case Operator.MULTIPLY:
                if multiply_enabled:
                    total += math.prod(operands)
            case Operator.DO:
                multiply_enabled = True
            case Operator.DONT:
                multiply_enabled = False
    return total
