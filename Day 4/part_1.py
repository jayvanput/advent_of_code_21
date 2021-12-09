sample_order = "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1".split(
    ",")
sample_boards = [[["22", "13", "17", "11", "0"],
                  ["8", "2", "23", "4", "24"],
                  ["21", "9", "14", "16", "7"],
                  ["6", "10", "3", "18", "5"],
                  ["1", "12", "20", "15", "19"]],
                 [["3", "15", "0", "2", "22"],
                  ["9", "18", "13", "17", "5"],
                  ["19", "8", "7", "25", "23"],
                  ["20", "11", "10", "24", "4"],
                  ["14", "21", "16", "12", "6"]],
                 [["14", "21", "17", "24", "4"],
                  ["10", "16", "15", "9", "19"],
                  ["18", "8", "23", "26", "20"],
                  ["22", "11", "13", "6", "5"],
                  ["2", "0", "12", "3", "7"]]]

with open("input.txt") as f:
    report = f.read().splitlines()


def generate_boards(file_list):

    list_of_boards = []
    board = []
    for index, row in enumerate(file_list):
        if index == 0:
            draw_order = row.split(",")
            continue
        if row == "":
            list_of_boards.append(board)
            board = []
            continue
        cleaned_row = row.split(" ")
        cleaned_row = [x for x in cleaned_row if x != ""]
        for index, number in enumerate(cleaned_row):
            if len(number) == 1:
                number = number.zfill(2)
            cleaned_row[index] = number
        board.append(cleaned_row)
    return draw_order, list_of_boards


def convert_board_to_ints(board):
    for index, row in enumerate(board):
        board[index] = [int(x) for x in row]
    return board


def check_for_win(board):

    number_of_columns = len(board[0])
    columns_sum = [0] * number_of_columns

    for row in board:
        if sum(row) == 5000:
            return board
        # Only works when we assume square boards.
        for index, number in enumerate(row):
            columns_sum[index] += number

    if 5000 in columns_sum:
        return board


def find_winning_board(order, list_of_boards):

    for index, board in enumerate(list_of_boards):
        list_of_boards[index] = convert_board_to_ints(board)
    print(list_of_boards)
    for draw in order:
        for board in list_of_boards:
            for index, row in enumerate(board):
                # Cant set to 0 and do basic sum because 0 is on the board. Choose arbitrarily large number
                board[index] = [1000 if x == int(draw) else x for x in row]

            if check_for_win(board) is not None:
                return board, int(draw)


if __name__ == "__main__":
    draw_order, list_of_boards = generate_boards(report)

    winning_board, final_draw = find_winning_board(draw_order, list_of_boards)

    for index, row in enumerate(winning_board):
        winning_board[index] = [x if x != 1000 else 0 for x in row]

    remaining_numbers_sum = 0
    for row in winning_board:
        remaining_numbers_sum += sum(row)

    print(remaining_numbers_sum * final_draw)
