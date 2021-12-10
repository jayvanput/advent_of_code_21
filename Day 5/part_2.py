from os import name


sample_lines = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"
]


with open("input.txt") as f:
    lines = f.read().splitlines()


def build_grid(x, y):
    grid = []
    for _ in range(y):
        grid.append([0] * x)

    return grid


def parse_line(line):
    coords_1_str, coords_2_str = line.split("->")
    coords_1 = [int(x) for x in coords_1_str.strip().split(",")]
    coords_2 = [int(x) for x in coords_2_str.strip().split(",")]

    return [coords_1, coords_2]


def is_vertical_line(line):
    if line[0][0] == line[1][0]:
        return True
    return False


def is_horizontal_line(line):
    if line[0][1] == line[1][1]:
        return True
    return False


if __name__ == "__main__":

    horizontal_lines = []
    vertical_lines = []
    diagonal_lines = []

    # x and y used to build grid.
    max_x = 0
    max_y = 0

    for line in lines:
        coords = parse_line(line)

        if is_horizontal_line(coords):
            horizontal_lines.append(coords)
        elif is_vertical_line(coords):
            vertical_lines.append(coords)
        else:
            diagonal_lines.append(coords)

        # Check if either x value is higher than current max
        if coords[0][0] > max_x:
            max_x = coords[0][0]
        if coords[1][0] > max_x:
            max_x = coords[1][0]

        # Check if either y value is higher than current max
        if coords[0][1] > max_y:
            max_y = coords[0][1]
        if coords[1][1] > max_y:
            max_y = coords[1][1]

    grid = build_grid(max_x + 1, max_y + 1)

    # Generate all horizontal lines in grid
    for line in vertical_lines:
        # Can use either x value from coords.
        x = line[0][0]

        y_values = [line[0][1], line[1][1]]
        y_values.sort()

        for y in range(y_values[0], y_values[1] + 1):
            grid[y][x] += 1

    # Generate all vertical lines in grid
    for line in horizontal_lines:
        # Can use either x value from coords.
        y = line[0][1]

        x_values = [line[0][0], line[1][0]]
        x_values.sort()

        for x in range(x_values[0], x_values[1] + 1):
            grid[y][x] += 1

    for line in diagonal_lines:
        x_values = [line[0][0], line[1][0]]
        y_values = [line[0][1], line[1][1]]

        x_step = -1 if x_values[0] - x_values[1] > 0 else 1
        y_step = -1 if y_values[0] - y_values[1] > 0 else 1

        while x_values[0] != x_values[1]:
            grid[y_values[0]][x_values[0]] += 1
            x_values[0] += x_step
            y_values[0] += y_step
        grid[y_values[1]][x_values[1]] += 1

    # for row in grid:
    #     print(row)

    values_gte_2 = 0
    for row in grid:
        for x in row:
            if x >= 2:
                values_gte_2 += 1
    print(values_gte_2)
