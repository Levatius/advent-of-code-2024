import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse([
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC",
    ])


@pytest.fixture
def example_2():
    return parse([
        "OOOOO",
        "OXOXO",
        "OOOOO",
        "OXOXO",
        "OOOOO",
    ])


@pytest.fixture
def example_3():
    return parse([
        "RRRRIICCFF",
        "RRRRIICCCF",
        "VVRRRCCFFF",
        "VVRCCCJFFF",
        "VVVVCJJCFE",
        "VVIVCCJJEE",
        "VVIIICJJEE",
        "MIIIIIJJEE",
        "MIIISIJEEE",
        "MMMISSJEEE",
    ])


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


def test__part_1__example_1(example_1):
    assert part_1(example_1) == 140


def test__part_1__example_2(example_2):
    assert part_1(example_2) == 772


def test__part_1__example_3(example_3):
    assert part_1(example_3) == 1930


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(puzzle_input))


def test__part_2__example_3(example_3):
    assert part_2(example_3) == 1206


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(puzzle_input))
