import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1(request):
    return parse([
        "########",
        "#..O.O.#",
        "##@.O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########",
        "",
        "<^^>>>vv<v>>v<<",
    ], request.param)


@pytest.fixture
def example_2(request):
    return parse([
        "##########",
        "#..O..O.O#",
        "#......O.#",
        "#.OO..O.O#",
        "#..O@..O.#",
        "#O#..O...#",
        "#O..O..O.#",
        "#.OO.O.OO#",
        "#....O...#",
        "##########",
        "",
        "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^",
        "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v",
        "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<",
        "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^",
        "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><",
        "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^",
        ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^",
        "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>",
        "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>",
        "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^",
    ], request.param)

@pytest.fixture
def example_3(request):
    return parse([
        "#######",
        "#...#.#",
        "#.....#",
        "#..OO@#",
        "#..O..#",
        "#.....#",
        "#######",
        "",
        "<vv<<^^<<^^",
    ], request.param)


@pytest.fixture
def puzzle_input(request):
    return parse(puzzle_input_lines, request.param)


@pytest.mark.parametrize("example_1", [False], indirect=True)
def test__part_1__example_1(example_1):
    assert part_1(*example_1) == 2028


@pytest.mark.parametrize("example_2", [False], indirect=True)
def test__part_1__example_2(example_2):
    assert part_1(*example_2) == 10092


@pytest.mark.parametrize("puzzle_input", [False], indirect=True)
def test__part_1__puzzle_input(puzzle_input):
    print(part_1(*puzzle_input))


@pytest.mark.parametrize("example_3", [True], indirect=True)
def test__part_2__example_3(example_3):
    assert part_2(*example_3) == 618

@pytest.mark.parametrize("example_2", [True], indirect=True)
def test__part_2__example_2(example_2):
    assert part_2(*example_2) == 9021


@pytest.mark.parametrize("puzzle_input", [True], indirect=True)
def test__part_2__puzzle_input(puzzle_input):
    print(part_2(*puzzle_input))
