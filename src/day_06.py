from numpy import array


def parse(lines):
    start_pos = None
    obstructions = set()
    for j, line in enumerate(lines):
        for i, item in enumerate(line):
            match item:
                case "#":
                    obstructions.add((j, i))
                case "^":
                    start_pos = (j, i)
    bounds = (len(lines), len(lines[0]))
    return start_pos, obstructions, bounds


def is_in_bounds(pos, bounds):
    return (0 <= pos).all() and (pos < bounds).all()


def rotate(guard_dir):
    match tuple(guard_dir):
        case (-1, 0):
            return array((0, 1))
        case (0, 1):
            return array((1, 0))
        case (1, 0):
            return array((0, -1))
        case (0, -1):
            return array((-1, 0))


def get_guard_logs(start_pos, obstructions, bounds, start_dir=(-1, 0)):
    guard_pos = array(start_pos)
    guard_dir = array(start_dir)
    guard_logs = {(start_pos, start_dir)}
    while is_in_bounds(guard_next := guard_pos + guard_dir, bounds):
        if tuple(guard_next) in obstructions:
            guard_dir = rotate(guard_dir)
        else:
            guard_pos = guard_next
        if (guard_log := (tuple(guard_pos), tuple(guard_dir))) not in guard_logs:
            guard_logs.add(guard_log)
            continue
        return None
    return guard_logs

def is_loop(start_pos, obstructions, bounds, start_dir):
    pass


def part_1(start_pos, obstructions, bounds):
    guard_logs = get_guard_logs(start_pos, obstructions, bounds)
    return len({guard_pos for guard_pos, _ in guard_logs})


def part_2(start_pos, obstructions, bounds):
    total = 0
    guard_logs = get_guard_logs(start_pos, obstructions, bounds)
    possible_obstructions = {tuple(array(guard_pos) + array(guard_dir)) for guard_pos, guard_dir in guard_logs}
    for i, possible_obstruction in enumerate(possible_obstructions):
        if (possible_obstruction == start_pos) or (possible_obstruction in obstructions) or (not is_in_bounds(array(possible_obstruction), bounds)):
            continue
        new_obstructions = set(obstructions)
        new_obstructions.add(possible_obstruction)
        if get_guard_logs(start_pos, new_obstructions, bounds) is None:
            total += 1
    return total