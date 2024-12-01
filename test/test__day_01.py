import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse([
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ])


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


def test__part_1__example_1(example_1):
    assert part_1(*example_1) == 11


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(*puzzle_input))


def test__part_2__example_1(example_1):
    assert part_2(*example_1) == 31


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(*puzzle_input))
