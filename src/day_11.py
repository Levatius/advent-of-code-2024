from collections import defaultdict
from math import log10, floor


def parse(line):
    stones = defaultdict(int)
    for value in line.split():
        stones[int(value)] += 1
    return stones


def simulate(stones, blinks):
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for value, count in stones.items():
            if value == 0:
                new_stones[1] += count
            elif (digits := floor(log10(value)) + 1) % 2 == 0:
                divisor = 10 ** (digits // 2)
                new_stones[value // divisor] += count
                new_stones[value % divisor] += count
            else:
                new_stones[value * 2024] += count
        stones = new_stones
    return stones


def part_1(stones):
    final_stones = simulate(stones, blinks=25)
    return sum(count for count in final_stones.values())


def part_2(stones):
    final_stones = simulate(stones, blinks=75)
    return sum(count for count in final_stones.values())
