sample_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open("input.txt") as f:
    lines = f.read().split(",")
    positions = [int(x) for x in lines]


def calculate_best_position(positions_list):
    max_position = max(positions_list)
    distance_sums = []

    for i in range(max_position):
        position_distance_sum = 0
        for position in positions_list:
            steps = position - i
            position_distance_sum += abs(steps)

        distance_sums.append(position_distance_sum)

    return min(distance_sums)


if __name__ == "__main__":
    print(calculate_best_position(positions))
