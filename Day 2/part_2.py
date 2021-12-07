sample_course = ["forward 5", "down 5",
                 "forward 8", "up 3", "down 8", "forward 2"]

with open("input.txt") as f:
    file = f.read().splitlines()


def get_product_of_final_positions_with_aim(course):

    hor = 0
    vert = 0
    aim = 0

    for step in course:
        dir, mag_str = step.split(" ")
        mag = int(mag_str)

        # Translate steps
        if dir == "forward":
            hor += mag
            vert += mag * aim
        elif dir == "up":
            aim -= mag
        else:  # Can only be down
            aim += mag

    print(hor * vert)


get_product_of_final_positions_with_aim(sample_course)

get_product_of_final_positions_with_aim(file)
