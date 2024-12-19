from functools import cache


def parse(lines):
    available_towels = frozenset(lines[0].split(", "))
    display_towels = lines[2:]
    return available_towels, display_towels


@cache
def count_possible_towels(display_towel: str, available_towels: frozenset[str]):
    possible_towels = 0
    for available_towel in available_towels:
        if not display_towel.startswith(available_towel):
            continue
        if remaining_towel := display_towel.removeprefix(available_towel):
            possible_towels += count_possible_towels(remaining_towel, available_towels)
        else:
            possible_towels += 1
    return possible_towels


def part_1(available_towels, display_towels):
    return sum(count_possible_towels(display_towel, available_towels) > 0 for display_towel in display_towels)


def part_2(available_towels, display_towels):
    return sum(count_possible_towels(display_towel, available_towels) for display_towel in display_towels)
