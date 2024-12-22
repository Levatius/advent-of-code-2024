import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse([
        "1",
        "10",
        "100",
        "2024",
    ])


@pytest.fixture
def example_2():
    return parse([
        "1",
        "2",
        "3",
        "2024",
    ])


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


def test__part_1__example_1(example_1):
    assert part_1(example_1) == 37327623


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(puzzle_input))


def test__part_2__example_2(example_2):
    assert part_2(example_2) == 23


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(puzzle_input))
