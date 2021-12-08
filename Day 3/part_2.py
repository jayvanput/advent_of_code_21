sample_report = ["00100", "11110", "10110", "10111", "10101",
                 "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

with open("input.txt") as f:
    report = f.read().splitlines()


def recursive_calc_life_support_part(report, iteration, tiebreaker):

    # Mod iterator in case we need to loop again.
    index = iteration % 12
    next_report = []

    # Stop conditions
    if len(report) == 2:
        print("here")
        if report[0][index] != report[1][index]:
            print(index, report[0][index], report[1][index])
            if report[0][index] == tiebreaker:
                return report[0]
            else:
                return report[1]
    if len(report) == 1:
        return report[0]

    # Calculate digit to filter on.
    one_tally = 0
    zero_tally = 0

    for string_of_bits in report:
        if string_of_bits[index] == "1":
            one_tally += 1
        else:
            zero_tally += 1

    if tiebreaker == "1":
        digit_filter = "1" if one_tally >= zero_tally else "0"
    else:
        digit_filter = "0" if one_tally >= zero_tally else "1"

    for string_of_bits in report:
        print(string_of_bits, string_of_bits[index], index)
        if string_of_bits[index] == digit_filter:
            next_report.append(string_of_bits)

    iteration += 1
    print(next_report, index, digit_filter)
    return recursive_calc_life_support_part(next_report, iteration, tiebreaker)


if __name__ == "__main__":

    iteration_step = 0

    # Tiebreaker value for when 2 values remain.
    oxygen_tiebreaker = "1"
    co2_tiebreaker = "0"

    oxygen_generator_rating_bin = recursive_calc_life_support_part(
        report, iteration_step, oxygen_tiebreaker)

    co2_scrubber_rating_bin = recursive_calc_life_support_part(
        report, iteration_step, co2_tiebreaker)

    print(oxygen_generator_rating_bin, co2_scrubber_rating_bin)

    oxygen_generator_rating = int(oxygen_generator_rating_bin, 2)
    co2_scrubber_rating = int(co2_scrubber_rating_bin, 2)
    print(oxygen_generator_rating * co2_scrubber_rating)
