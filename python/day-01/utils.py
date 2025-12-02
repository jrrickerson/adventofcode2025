

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
    remaining =  current + delta
    while remaining < 0:
        remaining += dial_size
    while remaining >= dial_size:
        remaining -= dial_size
    return remaining
