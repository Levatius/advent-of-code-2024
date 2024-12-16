from dataclasses import dataclass

import networkx as nx


@dataclass(frozen=True)
class Node:
    position: complex
    level: str  # Nodes on the H-level only connect horizontally, nodes on the V-level only connect vertically


def parse(lines):
    maze = nx.Graph()
    for a, line in enumerate(lines):
        for b, value in enumerate(line):
            if value == "#":
                continue
            position = complex(a, b)
            # Add a node with this position to both the H and V levels
            for level in ["H", "V"]:
                maze.add_node(Node(position, level), value=value)
            # Costs 1000 points to switch between the H and V levels (except at the end)
            cost = 1000 if value != "E" else 0
            maze.add_edge(Node(position, "H"), Node(position, "V"), cost=cost)

    connection_direction = {"H": 0 + 1j, "V": 1 + 0j}
    for node in maze:
        direction = connection_direction[node.level]
        if (adjacent_node := Node(node.position + direction, node.level)) not in maze:
            continue
        maze.add_edge(node, adjacent_node, cost=1)

    return maze


def get_node(maze, value, level="H"):
    return next(node for node, attr in maze.nodes.items() if attr["value"] == value and node.level == level)


def part_1(maze):
    start, end = get_node(maze, "S"), get_node(maze, "E")
    return nx.shortest_path_length(maze, start, end, weight="cost")


def part_2(maze):
    start, end = get_node(maze, "S"), get_node(maze, "E")
    return len({node.position for path in nx.all_shortest_paths(maze, start, end, weight="cost") for node in path})
