from collections import Counter


def parse(lines):
    return zip(*[map(int, line.split("   ")) for line in lines])


def part_1(left_list, right_list):
    return sum(abs(right - left) for left, right in zip(sorted(left_list), sorted(right_list)))


def part_2(left_list, right_list):
    right_counts = Counter(right_list)
    return sum(left * right_counts[left] for left in left_list)
