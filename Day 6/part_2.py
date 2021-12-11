sample_school = [3, 4, 3, 1, 2]
school = [2, 4, 1, 5, 1, 3, 1, 1, 5, 2, 2, 5, 4, 2, 1, 2, 5, 3, 2, 4, 1, 3, 5, 3, 1, 3, 1, 3, 5, 4, 1, 1, 1, 1, 5, 1, 2, 5, 5, 5, 2, 3, 4, 1, 1, 1, 2, 1, 4, 1, 3, 2, 1, 4, 3, 1, 4, 1, 5, 4, 5, 1, 4, 1, 2, 2, 3, 1, 1, 1, 2, 5, 1, 1, 1, 2, 1, 1, 2, 2, 1, 4, 3, 3, 1, 1, 1, 2, 1, 2, 5, 4, 1, 4, 3, 1, 5, 5, 1, 3, 1, 5, 1, 5, 2, 4, 5, 1, 2, 1, 1, 5, 4, 1, 1, 4, 5, 3, 1, 4, 5, 1, 3, 2, 2, 1, 1, 1, 4, 5, 2, 2, 5, 1, 4, 5, 2, 1, 1, 5, 3, 1, 1, 1, 3, 1, 2, 3, 3,
          1, 4, 3, 1, 2, 3, 1, 4, 2, 1, 2, 5, 4, 2, 5, 4, 1, 1, 2, 1, 2, 4, 3, 3, 1, 1, 5, 1, 1, 1, 1, 1, 3, 1, 4, 1, 4, 1, 2, 3, 5, 1, 2, 5, 4, 5, 4, 1, 3, 1, 4, 3, 1, 2, 2, 2, 1, 5, 1, 1, 1, 3, 2, 1, 3, 5, 2, 1, 1, 4, 4, 3, 5, 3, 5, 1, 4, 3, 1, 3, 5, 1, 3, 4, 1, 2, 5, 2, 1, 5, 4, 3, 4, 1, 3, 3, 5, 1, 1, 3, 5, 3, 3, 4, 3, 5, 5, 1, 4, 1, 1, 3, 5, 5, 1, 5, 4, 4, 1, 3, 1, 1, 1, 1, 3, 2, 1, 2, 3, 1, 5, 1, 1, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 5, 3]


def simulate_growth(school, days):
    iteration = 0

    count_fish_in_day_cycle = []

    for i in range(9):
        count_initial_state = school.count(i)
        count_fish_in_day_cycle.append(count_initial_state)

    while iteration < days:
        newly_bred_count = count_fish_in_day_cycle.pop(0)
        count_fish_in_day_cycle.append(newly_bred_count)
        count_fish_in_day_cycle[6] += newly_bred_count

        iteration += 1

    print(count_fish_in_day_cycle)
    return sum(count_fish_in_day_cycle)


if __name__ == "__main__":
    print(simulate_growth(school, 256))
