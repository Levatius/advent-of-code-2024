import itertools
import re
from dataclasses import dataclass

import numpy as np


@dataclass
class Step:
    x: int
    y: int

    @classmethod
    def from_str(cls, step_str):
        return cls(*map(int, re.findall(r"\d+", step_str)))


@dataclass
class Machine:
    button_a: Step
    button_b: Step
    prize: Step


def parse(lines):
    lines = [line for line in lines if line]
    machines = []
    for button_a_str, button_b_str, prize_str in itertools.batched(lines, 3):
        machines.append(Machine(
            button_a=Step.from_str(button_a_str),
            button_b=Step.from_str(button_b_str),
            prize=Step.from_str(prize_str),
        ))
    return machines


def calc_minimum_tokens(machines: list[Machine], limit=None, boost=0):
    tokens = 0
    for machine in machines:
        coefficient_matrix = [[machine.button_a.x, machine.button_b.x], [machine.button_a.y, machine.button_b.y]]
        ordinate = [machine.prize.x + boost, machine.prize.y + boost]
        solutions = np.linalg.solve(coefficient_matrix, ordinate)
        if np.allclose((int_solutions := np.round(solutions)), solutions):
            if limit is not None and (int_solutions[0] > limit or int_solutions[1] > limit):
                continue
            tokens += 3 * int_solutions[0] + 1 * int_solutions[1]
    return tokens

def part_1(machines):
    return calc_minimum_tokens(machines, limit=100)

def part_2(machines):
    return calc_minimum_tokens(machines, boost=10_000_000_000_000)
