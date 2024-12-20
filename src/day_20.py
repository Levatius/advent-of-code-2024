from collections import defaultdict

import numpy as np
from scipy.spatial import KDTree


def parse(lines):
    positions = set()
    start = None
    end = None
    for a, line in enumerate(lines):
        for b, value in enumerate(line):
            position = a, b
            if value != "#":
                positions.add(position)
            if value == "S":
                start = position
            elif value == "E":
                end = position

    racetrack = [start]
    while racetrack[-1] != end:
        for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if (next_position := tuple(racetrack[-1][i] + direction[i] for i in range(2))) in positions:
                # Do not add already added positions
                if len(racetrack) >= 2 and next_position == racetrack[-2]:
                    continue
                racetrack.append(next_position)
                break
    racetrack_map = {position: i for i, position in enumerate(racetrack)}
    return racetrack_map


def to_tuple(array: np.array) -> tuple:
    return tuple(map(int, array))


def find_cheats(racetrack_map, min_time_save, max_cheat_time):
    cheats = defaultdict(int)
    racetrack_tree = KDTree(list(racetrack_map.keys()))
    for i, j in racetrack_tree.query_pairs(r=max_cheat_time, p=1):
        a = racetrack_tree.data[i]
        b = racetrack_tree.data[j]
        distance = racetrack_map[to_tuple(b)] - racetrack_map[to_tuple(a)]
        cheat_distance = int(np.linalg.norm(b - a, ord=1))
        time_save = distance - cheat_distance
        if time_save >= min_time_save:
            cheats[time_save] += 1
    return cheats


def part_1(racetrack_map, min_time_save=100):
    return sum(count for time_save, count in find_cheats(racetrack_map, min_time_save, max_cheat_time=2).items())


def part_2(racetrack_map, min_time_save=100):
    return sum(count for time_save, count in find_cheats(racetrack_map, min_time_save, max_cheat_time=20).items())
