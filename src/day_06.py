# Rotates the given direction by 90 degrees clockwise
NEXT_DIRECTION = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


def parse(lines):
    position = None
    obstructions = set()
    for j, line in enumerate(lines):
        for i, item in enumerate(line):
            match item:
                case "#":
                    obstructions.add((j, i))
                case "^":
                    position = (j, i)
    bounds = (len(lines), len(lines[0]))
    return position, obstructions, bounds


# PART 1


def is_in_bounds(position, bounds):
    return (0 <= position[0] < bounds[0]) and (0 <= position[1] < bounds[1])


def move(position, direction, steps=1):
    return position[0] + steps * direction[0], position[1] + steps * direction[1]


def get_path(position, obstructions, bounds, direction=(-1, 0)):
    path = [(position, direction)]
    while is_in_bounds(next_position := move(position, direction), bounds):
        if next_position in obstructions:
            direction = NEXT_DIRECTION[direction]
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
        start_position = move(position, direction, steps=-1)
        start_direction = NEXT_DIRECTION[direction]
        obstructions[position] = (start_position, start_direction)
    return obstructions


def is_loop(position, obstructions, bounds, direction):
    # Starts at the temporal obstruction, seeks loop or out of bounds
    corners = set()
    while is_in_bounds(next_position := move(position, direction), bounds):
        if next_position in obstructions:
            if (corner := (position, direction)) not in corners:
                corners.add(corner)
            else:
                # We have seen this corner before => Looping
                return True
            direction = NEXT_DIRECTION[direction]
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
