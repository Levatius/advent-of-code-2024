from itertools import pairwise


def parse(lines):
    return [[int(value) for value in line.split()] for line in lines]


def is_safe(report, dampener=False):
    deltas = [b - a for a, b in pairwise(report)]
    safety_max = len(deltas)
    safety_level = max(sum(1 <= delta <= 3 for delta in deltas), sum(-3 <= delta <= -1 for delta in deltas))

    if safety_level == safety_max:
        return True
    elif dampener and safety_level >= safety_max - 2:
        # Apply the Problem Dampener across the elements of each report
        for i in range(len(report)):
            dampened_report = report[:i] + report[i + 1:]
            if is_safe(dampened_report):
                return True
    return False


def part_1(reports):
    return sum(is_safe(report) for report in reports)


def part_2(reports):
    return sum(is_safe(report, dampener=True) for report in reports)
