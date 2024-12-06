def parse(lines):
    position = None
    obstructions = set()
    for a, line in enumerate(lines):
        for b, item in enumerate(line):
            match item:
                case "#":
                    obstructions.add(complex(a, b))
                case "^":
                    position = complex(a, b)
    bounds = complex(len(lines), len(lines[0]))
    return position, obstructions, bounds


# PART 1


def is_in_bounds(position, bounds):
    return (0 <= position.real < bounds.real) and (0 <= position.imag < bounds.imag)


def get_path(position, obstructions, bounds, direction=-1 + 0j):
    path = [(position, direction)]
    while is_in_bounds(next_position := position + direction, bounds):
        if next_position in obstructions:
            direction = direction * -1j
        else:
            position = next_position
        path.append((position, direction))
    return path


def part_1(position, obstructions, bounds):
    path = get_path(position, obstructions, bounds)
    return len({position for position, _ in path})


# PART 2


def find_temporal_obstructions(path):
    # Temporal obstructions are found along the path
    obstructions = {}
    for position, direction in path:
        # Only consider the first approach to a temporal obstruction
        if position in obstructions:
            continue
        # Rewrite history, we will check for a loop from here
        start_position = position - direction
        start_direction = direction * -1j
        obstructions[position] = (start_position, start_direction)
    return obstructions


def is_loop(position, obstructions, bounds, direction):
    # Starts at the temporal obstruction, seeks loop or out of bounds
    corners = set()
    while is_in_bounds(next_position := position + direction, bounds):
        if next_position in obstructions:
            if (corner := (position, direction)) not in corners:
                corners.add(corner)
            else:
                # We have seen this corner before => Looping
                return True
            direction = direction * -1j
        else:
            position = next_position
    return False


def part_2(position, obstructions, bounds):
    total = 0
    path = get_path(position, obstructions, bounds)
    temporal_obstructions = find_temporal_obstructions(path)
    # Start is not allowed
    temporal_obstructions.pop(position)

    for temporal_obstruction, (position, direction) in temporal_obstructions.items():
        all_obstructions = obstructions.union({temporal_obstruction})
        total += is_loop(position, all_obstructions, bounds, direction)
    return total
