from numpy import array


class Dir:
    N = array((-1, 0))
    E = array((0, 1))
    S = array((1, 0))
    W = array((0, -1))


def parse(lines):
    return array([list(line) for line in lines])


def is_in_bounds(pos, grid):
    return (0 <= pos).all() and (pos < grid.shape).all()


def part_1(grid):
    total = 0
    direction_group = [Dir.N, Dir.N + Dir.E, Dir.E, Dir.E + Dir.S, Dir.S, Dir.S + Dir.W, Dir.W, Dir.W + Dir.N]
    for j, line in enumerate(grid):
        for i, value in enumerate(line):
            if value != "X":
                continue
            for direction in direction_group:
                pos = array((j, i))
                for letter_to_find in "MAS":
                    pos += direction
                    if not is_in_bounds(pos, grid):
                        break
                    letter = grid[*pos]
                    if letter != letter_to_find:
                        break
                else:
                    total += 1
    return total


def part_2(grid):
    total = 0
    direction_groups = [[Dir.N + Dir.W, Dir.S + Dir.E], [Dir.N + Dir.E, Dir.S + Dir.W]]
    for j, line in enumerate(grid):
        for i, value in enumerate(line):
            if value != "A":
                continue
            for direction_group in direction_groups:
                pos = array((j, i))
                letters = [grid[*(pos + direction)] for direction in direction_group if
                           is_in_bounds(pos + direction, grid)]
                if "M" not in letters or "S" not in letters:
                    break
            else:
                total += 1
    return total
