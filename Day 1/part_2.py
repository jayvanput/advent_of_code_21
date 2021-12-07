sample_report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# import input file
with open("input.txt") as f:
    file = f.read().splitlines()
    report = [int(i) for i in file]


def find_three_measurement_window_increases(report):

    tally = 0
    last_sum = None

    for index, depth in enumerate(report):
        # Skip first 2 pings.
        if index < 2:
            continue

        # Get last 2 values
        second_to_last_value = report[index - 2]
        last_value = report[index - 1]

        # Calculate three-measurement sliding window sum.
        window_sum = second_to_last_value + last_value + depth

        # Handle first window
        if last_sum == None:
            last_sum = window_sum
            continue

        if window_sum > last_sum:
            tally += 1

        last_sum = window_sum
    return tally


# Check against sample (should yield 7)
print(find_three_measurement_window_increases(sample_report))

# # Run against real report
print(find_three_measurement_window_increases(report))
