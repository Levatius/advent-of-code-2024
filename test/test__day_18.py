import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse([
        "5,4",
        "4,2",
        "4,5",
        "3,0",
        "2,1",
        "6,3",
        "2,4",
        "1,5",
        "0,6",
        "3,3",
        "2,6",
        "5,1",
        "1,2",
        "5,5",
        "2,5",
        "6,5",
        "1,4",
        "0,4",
        "6,4",
        "1,1",
        "6,1",
        "1,0",
        "0,5",
        "1,6",
        "2,0",
    ], size=6, initial_fallen=12)


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines, size=70, initial_fallen=1024)


def test__part_1__example_1(example_1):
    assert part_1(*example_1) == 22


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(*puzzle_input))


def test__part_2__example_1(example_1):
    assert part_2(*example_1) == "6,1"


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(*puzzle_input))
