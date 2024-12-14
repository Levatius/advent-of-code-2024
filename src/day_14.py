import math
import re
from collections import Counter
from dataclasses import dataclass


@dataclass
class Robot:
    position: complex
    velocity: complex

    @classmethod
    def from_line(cls, line):
        m = re.fullmatch(r"p=(?P<p_a>.+),(?P<p_b>.+) v=(?P<v_a>.+),(?P<v_b>.+)", line)
        return cls(
            position=complex(int(m.group("p_a")), int(m.group("p_b"))),
            velocity=complex(int(m.group("v_a")), int(m.group("v_b"))),
        )

    def move(self, bounds, seconds=1):
        position = self.position + seconds * self.velocity
        self.position = complex(position.real % bounds.real, position.imag % bounds.imag)

    def get_quadrant(self, centre):
        if self.position.real < centre.real and self.position.imag < centre.imag:
            return "A"
        elif self.position.real > centre.real and self.position.imag < centre.imag:
            return "B"
        elif self.position.real < centre.real and self.position.imag > centre.imag:
            return "C"
        elif self.position.real > centre.real and self.position.imag > centre.imag:
            return "D"


def parse(lines):
    return [Robot.from_line(line) for line in lines]


def get_centre(bounds):
    return complex((bounds.real - 1) // 2, (bounds.imag - 1) // 2)


def part_1(robots, bounds):
    for robot in robots:
        robot.move(bounds, seconds=100)

    centre = get_centre(bounds)
    counts = Counter(robot.get_quadrant(centre) for robot in robots)
    return math.prod(count for quadrant, count in counts.items() if quadrant)


def part_2(robots, bounds):
    centre = get_centre(bounds)
    records = []
    for seconds in range(1, 10_000):
        sum_to_centre = 0
        for robot in robots:
            robot.move(bounds)
            sum_to_centre += abs(robot.position - centre)
        records.append((seconds, sum_to_centre))
    return min(records, key=lambda record: record[1])[0]
