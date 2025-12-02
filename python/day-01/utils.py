

def interpret_rotate(command: str) -> int:
    """Interpret commands on rotating a combination lock.
    Examples:
        R18 - Rotate right 18 places (add to the current dial position)
        L27 - Rotate left 27 places (subtract from the current dial position)
    """
    sign = -1 if command[0] == "L" else 1
    value = int(command[1:])

    return sign * value


def rotate(current: int, delta: int, dial_size: int = 100) -> int:
    """Rotate a combination dial lock a specific number of places, returning
    the new position of the dial
    Params:
        current - current position on the dial
        delta - number of places to change on the dial (pos / neg)
        dial_size - (default: 99) How many positions exist on the dial. If the
            dial is rotated above this number, the dial position
            resets to zero.
    """
    # Calculate full turns of the dial
    pass_zero = abs(int(float(delta) / dial_size))
    # Match the sign of the delta so modulo works as expected
    divisor = -1 * dial_size if delta < 0 else dial_size
    delta_remainder = delta % divisor

    # Deal with the remaining (non-full) rotation
    new_pos = current + delta_remainder
    if new_pos < 0:
        new_pos += dial_size
        # Don't double count a pass if we started at zero
        if current != 0:
            pass_zero += 1
    elif new_pos > dial_size:
        new_pos -= dial_size
        pass_zero += 1
    elif new_pos == dial_size:
        new_pos = 0
    return new_pos, pass_zero
