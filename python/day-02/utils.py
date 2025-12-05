

def get_ranges(input_data: list[str]) -> list[tuple[int, int]]:
    lines = [line.split(",") for line in input_data]
    range_text = [group for line in lines for group in line]
    ranges = []
    for group in range_text:
        start, end = group.split("-")
        ranges.append((int(start), int(end)))

    return ranges


def get_invalid(id_range: tuple[int, int]) -> list[int]:
    start, end = id_range

    invalid_ids = []
    for product_id in range(start, end + 1):
        if is_invalid(product_id):
            invalid_ids.append(product_id)

    return invalid_ids


def is_invalid(product_id: int) -> bool:
    str_id = str(product_id)
    id_len = len(str_id)
    # Throw out any ids with an odd number of digits
    if id_len % 2 != 0:
        return False
    if str_id[:id_len // 2] == str_id[id_len // 2:]:
        return True
    return False


    
