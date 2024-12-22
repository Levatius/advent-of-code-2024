import itertools
from math import floor


def parse(lines):
    return [int(line) for line in lines]


def generate_secret_numbers(secret_number, iterations=2000):
    secret_numbers = [secret_number]
    for _ in range(iterations):
        secret_number = secret_numbers[-1]
        for value in [64, 1 / 32, 2048]:
            secret_number ^= floor(secret_number * value)
            secret_number %= 16777216
        secret_numbers.append(secret_number)
    return secret_numbers


def part_1(secret_numbers):
    return sum(generate_secret_numbers(secret_number)[-1] for secret_number in secret_numbers)


def sliding_window(iterable, n):
    for i in range(n, len(iterable) + 1):
        yield tuple(iterable[i - n:i])


def part_2(secret_numbers, window_length=4):
    # Example: [[3, 0, 6, 5, 4, 4, 6, 4, 4, 2, ...], ...]
    price_lists = [
        [generated_secret_number % 10 for generated_secret_number in generate_secret_numbers(secret_number)]
        for secret_number in secret_numbers
    ]
    # Example: [[-3, 6, -1, -1, 0, 2, -2, 0, -2, ...], ...]
    difference_lists = [
        [price_b - price_a for price_a, price_b in itertools.pairwise(price_list)]
        for price_list in price_lists
    ]
    # Example: [[(-3, 6, -1, -1), (6, -1, -1, 0), (-1, -1, 0, 2), ...], ...] with window_length=4
    window_lists = [
        [window for window in sliding_window(difference_list, window_length)]
        for difference_list in difference_lists
    ]

    window_to_price_maps = []
    for window_list, price_list in zip(window_lists, price_lists):
        window_to_price_map = {}
        # Prices are assigned to the end of each window, i.e. skip the first few prices
        for window, price in zip(window_list, price_list[window_length:]):
            # Windows can show up multiple times with different prices, only record the first price for each window
            if window not in window_to_price_map:
                window_to_price_map[window] = price
        window_to_price_maps.append(window_to_price_map)

    # Gather all windows across all monkeys, we will check each one to find the best window overall
    all_windows = set(window for window in itertools.chain(*window_lists))

    most_bananas = max(
        sum(window_to_price_map.get(window, 0) for window_to_price_map in window_to_price_maps)
        for window in all_windows
    )
    return most_bananas
