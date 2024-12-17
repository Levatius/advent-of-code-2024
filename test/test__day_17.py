import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse([
        "Register A: 729",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,1,5,4,3,0",
    ])


@pytest.fixture
def example_2():
    return parse([
        "Register A: 2024",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,3,5,4,3,0",
    ])


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


def test__part_1__example_1(example_1):
    assert part_1(*example_1) == "4,6,3,5,6,3,5,2,1,0"


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(*puzzle_input))


def test__part_2__example_2(example_2):
    assert part_2(*example_2) == 117440


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(*puzzle_input))
