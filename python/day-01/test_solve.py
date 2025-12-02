import solve
from utils import interpret_rotate, rotate


def test_interpret_rotate_left():
    rotate_command = "L27"
    expected_value = -27

    result = interpret_rotate(rotate_command)

    assert result == expected_value


def test_interpret_rotate_right():
    rotate_command = "R18"
    expected_value = 18

    result = interpret_rotate(rotate_command)

    assert result == expected_value


def test_interpret_rotate_left_zero():
    rotate_command = "L0"
    expected_value = 0

    result = interpret_rotate(rotate_command)

    assert result == expected_value


def test_interpret_rotate_right_zero():
    rotate_command = "R0"
    expected_value = 0

    result = interpret_rotate(rotate_command)

    assert result == expected_value


def test_rotate_left_positive():
    start_pos = 50
    delta = -27
    expected_pos = 50 - 27

    pos = rotate(start_pos, delta)

    assert pos == expected_pos


def test_rotate_right_positive():
    start_pos = 50
    delta = 18
    expected_pos = 50 + 18

    pos = rotate(start_pos, delta)

    assert pos == expected_pos


def test_rotate_left_past_zero():
    start_pos = 5
    delta = -10
    expected_pos = 95 

    pos = rotate(start_pos, delta)

    assert pos == expected_pos


def test_rotate_right_past_max():
    start_pos = 92
    delta = 15
    expected_pos = 7

    pos = rotate(start_pos, delta)

    assert pos == expected_pos


def test_rotate_left_multiple_rotations():
    start_pos = 5
    delta = -110
    expected_pos = 95 

    pos = rotate(start_pos, delta)

    assert pos == expected_pos


def test_rotate_right_multiple_rotations():
    start_pos = 92
    delta = 115
    expected_pos = 7

    pos = rotate(start_pos, delta)

    assert pos == expected_pos

def test_part_1_sample_input():
    input_data = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    zero_count = solve.part_1(input_data)

    assert zero_count == 3
