import utils
import solve


def test_get_ranges_empty():
    input_data = []
    expected_ranges = []

    ranges = utils.get_ranges(input_data)

    assert ranges == expected_ranges


def test_get_ranges_single():
    input_data = ["11-22"]
    expected_ranges = [(11, 22)]

    ranges = utils.get_ranges(input_data)

    assert ranges == expected_ranges

def test_get_ranges_multiple():
    input_data = ["11-22,123-456,10280-12810"]
    expected_ranges = [(11, 22), (123, 456), (10280, 12810)]

    ranges = utils.get_ranges(input_data)

    assert ranges == expected_ranges


def test_get_ranges_multiline():
    input_data = ["11-22,123-456,10280-12810", "111-222,1256-1380", "90-99"]
    expected_ranges = [
        (11, 22), (123, 456), (10280, 12810),
        (111, 222), (1256, 1380),
        (90, 99)]

    ranges = utils.get_ranges(input_data)

    assert ranges == expected_ranges


def test_is_invalid_single_digit():
    product_id = 1

    invalid = utils.is_invalid(product_id)

    assert not invalid


def test_is_invalid_odd_digits():
    product_id = 12312

    invalid = utils.is_invalid(product_id)

    assert not invalid


def test_is_invalid_no_repeat():
    product_id = 1234

    invalid = utils.is_invalid(product_id)

    assert not invalid


def test_is_invalid_short_invalid():
    product_id = 55

    invalid = utils.is_invalid(product_id)

    assert invalid


def test_is_invalid_long_invalid():
    product_id = 1188511885

    invalid = utils.is_invalid(product_id)

    assert invalid


def test_get_invalid_none():
    id_range = (12, 19)
    expected_invalid = []

    invalid = utils.get_invalid(id_range)

    assert invalid == expected_invalid


def test_get_invalid_small_ints():
    id_range = (11, 22)
    expected_invalid = [11, 22]

    invalid = utils.get_invalid(id_range)

    assert invalid == expected_invalid


def test_get_invalid_larger_ints():
    id_range = (1188511880, 1188511890)
    expected_invalid = [1188511885]

    invalid = utils.get_invalid(id_range)

    assert invalid == expected_invalid


def test_part_1_sample_input():
    input_data = [
        "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,"
        "1698522-1698528,446443-446449,38593856-38593862,565653-565659,"
        "824824821-824824827,2121212118-2121212124",
    ]

    invalid_sum = solve.part_1(input_data)

    assert invalid_sum == 1227775554

