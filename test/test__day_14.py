import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse([
        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3",
    ]), 11 + 7j


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines), 101 + 103j


def test__part_1__example_1(example_1):
    assert part_1(*example_1) == 12


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(*puzzle_input))


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(*puzzle_input))
