import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")

@pytest.fixture
def example_2():
    return parse("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")


@pytest.fixture
def puzzle_input():
    return parse("\n".join(puzzle_input_lines))


def test__part_1__example_1(example_1):
    assert part_1(example_1) == 161


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(puzzle_input))


def test__part_2__example_2(example_2):
    assert part_2(example_2) == 48


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(puzzle_input))
