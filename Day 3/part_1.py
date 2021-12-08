sample_report = ["00100", "11110", "10110", "10111", "10101",
                 "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

with open("input.txt") as f:
    report = f.read().splitlines()


def calc_gamma_and_epsilon_product(report):

    # If value of 1s > threshold, then gamma is 1, else 0
    threshold = len(report) / 2

    # Initialize counter for each position in string of bits of arbitrary length n.
    n = len(report[0])
    position_counts_of_1s = [0] * n

    for string_of_bits in report:
        for index, bit in enumerate(string_of_bits):
            if bit == "1":
                position_counts_of_1s[index] += 1

    gamma_list = []
    epsilon_list = []

    for count in position_counts_of_1s:
        if count > threshold:
            gamma_list.append("1")
            epsilon_list.append("0")
        else:
            gamma_list.append("0")
            epsilon_list.append("1")

    gamma = int("".join(gamma_list), 2)
    epsilon = int("".join(epsilon_list), 2)

    print(gamma * epsilon)


calc_gamma_and_epsilon_product(report)
