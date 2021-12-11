sample_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open("input.txt") as f:
    lines = f.read().split(",")
    positions = [int(x) for x in lines]


def calculate_best_position(positions_list):
    max_position = max(positions_list)
    total_fuel_per_position = []
    fuel_per_step = {}

    # Calculate all costs for all steps up front. Then link to it.
    for i in range(max_position + 1):
        fuel_per_step[i] = int(i*(i+1)/2)

    for i in range(max_position):
        fuel_sums = 0
        for position in positions_list:
            steps = abs(position - i)
            fuel_sums += fuel_per_step[steps]
        total_fuel_per_position.append(fuel_sums)
    return min(total_fuel_per_position)


if __name__ == "__main__":
    print(calculate_best_position(positions))
