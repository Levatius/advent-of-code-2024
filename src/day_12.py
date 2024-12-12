import networkx as nx

DIRECTIONS = (-1 + 0j, 0 + 1j, 1 + 0j, 0 - 1j)


def parse(lines):
    garden = nx.Graph()
    for a, line in enumerate(lines):
        for b, plant in enumerate(line):
            garden.add_node(complex(a, b), plant=plant)

    for plot, attr in garden.nodes.items():
        for direction in DIRECTIONS:
            if (adjacent_plot := plot + direction) in garden and garden.nodes[adjacent_plot]["plant"] == attr["plant"]:
                garden.add_edge(plot, adjacent_plot)
    return garden


def part_1(garden):
    price = 0
    for region in nx.connected_components(garden):
        # Area * Perimeter
        price += len(region) * sum(4 - garden.degree(plot) for plot in region)
    return price


def part_2(garden):
    price = 0
    for region in nx.connected_components(garden):
        fences = nx.Graph()
        for plot in region:
            for direction in DIRECTIONS:
                # No fence between connected plots
                if plot + direction in region:
                    continue
                # Divide the direction by anything but 2 (see the A-B example in part 2)
                fences.add_node(plot + direction / 4)
        for fence in fences:
            for direction in DIRECTIONS:
                if (adjacent_fence := fence + direction) in fences:
                    fences.add_edge(fence, adjacent_fence)
        # Area * Sides
        price += len(region) * len(list(nx.connected_components(fences)))
    return price
