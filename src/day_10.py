import networkx as nx


def parse(lines, directions=(-1 + 0j, 0 + 1j, 1 + 0j, 0 - 1j)):
    graph = nx.DiGraph()
    trailheads = set()
    for a, line in enumerate(lines):
        for b, height_str in enumerate(line):
            position = complex(a, b)
            if (height := int(height_str)) == 0:
                trailheads.add(position)
            graph.add_node(position, height=height)

    for node, attr in graph.nodes.items():
        for direction in directions:
            if (next_node := node + direction) in graph and graph.nodes[next_node]["height"] == attr["height"] + 1:
                graph.add_edge(node, next_node)
    return graph, trailheads


def calc_score(graph, trailheads, peak_height=9, is_rating=False):
    score = 0
    for trailhead in trailheads:
        trail = nx.dfs_tree(graph, trailhead)
        peaks = {node for node in trail.nodes if graph.nodes[node]["height"] == peak_height}
        if is_rating:
            score += sum(len(list(nx.all_simple_paths(graph, trailhead, peak))) for peak in peaks)
        else:
            score += len(peaks)
    return score


def part_1(graph, trailheads):
    return calc_score(graph, trailheads)


def part_2(graph, trailheads):
    return calc_score(graph, trailheads, is_rating=True)
