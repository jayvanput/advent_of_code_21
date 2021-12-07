sample_report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# import input file
with open("input.txt") as f:
    file = f.read().splitlines()
    report = [int(i) for i in file]


def find_increases(report):
    tally = 0
    last_value = None

    for depth in report:
        # handle starting value
        if last_value == None:
            last_value = depth
            continue
        if depth > last_value:
            tally += 1
        last_value = depth

    return tally


# Check against sample (should yield 7)
print(find_increases(sample_report))

# Run against real report
print(find_increases(report))
