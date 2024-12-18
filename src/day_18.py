import networkx as nx


def parse(lines, size, initial_fallen):
    falling_bytes = [complex(*map(int, line.split(","))) for line in lines]
    graph = nx.Graph()
    for a in range(size + 1):
        for b in range(size + 1):
            if (position := complex(a, b)) not in falling_bytes[:initial_fallen]:
                graph.add_node(position)
    for node in graph.nodes:
        for direction in [1 + 0j, 0 + 1j]:
            if (adjacent_node := node + direction) in graph:
                graph.add_edge(node, adjacent_node)
    return graph, size, falling_bytes[initial_fallen:]

def part_1(graph, size, _):
    return nx.shortest_path_length(graph, 0 + 0j, complex(size, size))


def part_2(graph, size, falling_bytes):
    current_path = None
    for falling_byte in falling_bytes:
        graph.remove_node(falling_byte)
        if current_path and falling_byte not in current_path:
            continue
        try:
            # Only get a new path if the previous one is now blocked
            current_path = set(nx.shortest_path(graph, 0 + 0j, complex(size, size)))
        except nx.NetworkXNoPath:
            return f"{int(falling_byte.real)},{int(falling_byte.imag)}"
