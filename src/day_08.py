import itertools
from collections import defaultdict


def parse(lines):
    antennas = defaultdict(set)
    for a, line in enumerate(lines):
        for b, frequency in enumerate(line):
            if frequency == ".":
                continue
            antennas[frequency].add(complex(a, b))
    bounds = complex(len(lines), len(lines[0]))
    return antennas, bounds


def is_in_bounds(position, bounds):
    return (0 <= position.real < bounds.real) and (0 <= position.imag < bounds.imag)


def find_antinodes(nodes, bounds, start_step=1, end_step: int | None = 1):
    for node_a, node_b in itertools.combinations(nodes, 2):
        distance = node_b - node_a
        for node, direction in [(node_a, -1), (node_b, 1)]:
            step = start_step
            while (
                    (end_step is None or step <= end_step)
                    and is_in_bounds(antinode := node + direction * step * distance, bounds)
            ):
                yield antinode
                step += 1


def part_1(antennas, bounds):
    return len({antinode for nodes in antennas.values()
                for antinode in find_antinodes(nodes, bounds)})


def part_2(antennas, bounds):
    return len({antinode for nodes in antennas.values()
                for antinode in find_antinodes(nodes, bounds, start_step=0, end_step=None)})
