import pytest
from aocd import get_data

from src.day_00 import parse, part_1, part_2


@pytest.fixture
def example_1():
    lines = []
    return lines


@pytest.fixture
def example_2():
    lines = []
    return lines


@pytest.mark.skip(reason="Not Implemented")
def test__part_1__example_1(example_1):
    assert part_1(example_1)


@pytest.mark.skip(reason="Not Implemented")
def test__part_2__example_1(example_1):
    assert part_2(example_1)


@pytest.mark.skip(reason="Not Implemented")
def test__part_2__example_2(example_2):
    assert part_2(example_2)
