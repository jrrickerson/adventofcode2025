import utils


def get_input_data(filename):  # pragma: no cover
    with open(filename) as infile:
        return [line.strip() for line in infile]


def part_1(input_data):
    START_POS = 50

    zero_count = 0
    deltas = [utils.interpret_rotate(cmd) for cmd in input_data if cmd]
    current = START_POS
    #print("START PART 1")
    for delta in deltas:
        #print(f"Current pos: {current}")
        current, _ = utils.rotate(current, delta)
        if current == 0:
            zero_count += 1

    return zero_count


def part_2(input_data):
    START_POS = 50

    zero_count = 0
    deltas = [utils.interpret_rotate(cmd) for cmd in input_data if cmd]
    current = START_POS
    #print("START PART 2")
    #print(f"Current pos: {current}")
    for delta in deltas:
        current, pass_zero = utils.rotate(current, delta)
        #print(f"Delta: {delta}, Current pos: {current}, Passed 0: {pass_zero}")
        zero_count += pass_zero
        if current == 0:
            zero_count += 1

    return zero_count


def main(input_file):  # pragma: no cover
    input_data = get_input_data(input_file)

    part_1_result = part_1(input_data)
    part_2_result = part_2(input_data)

    solution = f"""
    Part 1: {part_1_result}
    Part 2: {part_2_result}
    """
    return solution


if __name__ == "__main__":  # pragma: no cover
    print(
        "Solving Puzzle for Day 1:", "https://adventofcode.com/2025/day/1"
    )
    print(main("../puzzles/day-01.input"))
