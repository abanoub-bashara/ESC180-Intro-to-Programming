"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""


def is_sq_in_board(board, y, x):
    y_cor = False
    x_cor = False

    if y >= 0 and y <= len(board) - 1:
        y_cor = True
    if x >= 0 and x <= len(board[0]) - 1:
        x_cor = True

    return (y_cor and x_cor)

def is_sequence_complete(board, col, y_start, x_start, length, d_y, d_x):
    #check if start position is valid
    if is_sq_in_board(board, y_start, x_start) is True:
    #calculate end coordinate:
        y_end = y_start + (length - 1) * d_y
        x_end = x_start + (length - 1) * d_x
        x_end_next = x_end + d_x
        y_end_next = y_end + d_y
        x_start_before = x_start - d_x
        y_start_before = y_start - d_y

        if is_sq_in_board(board, y_end, x_end) is True:
            if is_sq_in_board(board, y_end_next, x_end_next) is True:
                if board[y_end_next][x_end_next] == col:
                    return False
            if is_sq_in_board(board, y_start_before, x_start_before) is True:
                if board[y_start_before][x_start_before] == col:
                    return False

            if is_sq_in_board(board, y_end, x_end):
                for i in range (length):
                    if board[y_start][x_start] != col:
                        return False
                    y_start += d_y
                    x_start += d_x
                return True

    return False


def is_empty(board):

    for i in range (len(board)):
        for n in range (len(board[i])):
            if board[i][n] != " ":
                return False
    return True


def is_bounded(board, y_end, x_end, length, d_y, d_x):

    end_bound = False
    start_bound = False

    y_after = y_end + d_y
    x_after = x_end + d_x

    y_before = y_end - (length-1)*d_y - d_y
    x_before = x_end - (length-1)*d_x - d_x

    if is_sq_in_board(board, y_after, x_after) is True:
        if board[y_after][x_after] != " ":
            end_bound = True
        else:
            end_bound = False
    else:
        end_bound = True

    if is_sq_in_board(board, y_before, x_before) is True:
        if board[y_before][x_before] != " ":
            start_bound = True
        else:
            start_bound = False
    else:
        start_bound = True

    if end_bound == True and start_bound == True:
        return "CLOSED"
    elif end_bound == True or start_bound == True:
        return "SEMIOPEN"
    else:
        return "OPEN"




def search_max(board):

    scores = {}

    for row in range (len(board)):
        for column in range (len(board)):
            if board[row][column] == " ":
                board[row][column] = "b"
                score_at_position = score(board)
                scores [(row, column)] = score_at_position
                board[row][column] = " "

    move_y = (max(scores, key=scores.get))[0]
    move_x = (max(scores, key=scores.get))[1]

    return move_y, move_x

def is_win(board):
    is_full = True

    #Check if board is fully full:
    for i in range (len(board)):
        for n in range (len(board[i])):
            if board [i][n] == " ":
                is_full = False
    if is_full == True:
        return "Draw"
    else:
        sequences = [[0, 1], [1, 0], [1, 1], [1, -1]]
        for s in range (len(sequences)):
            d_y = sequences[s][0]
            d_x = sequences[s][1]
            for colour in range (2):
                for row in range (len(board)):
                    for column in range (len(board[0])):
                        if colour == 0:
                            col = "w"
                        else:
                            col = "b"

                        if is_sequence_complete \
                        (board, col, row, column, 5, d_y, d_x) \
                        == True and col == "w":
                            return "White won"
                        elif is_sequence_complete\
                        (board, col, row, column, 5, d_y, d_x) \
                        == True and col == "b":
                            return "Black won"

        return "Continue playing"






def detect_row(board, col, y_start, x_start, length, d_y, d_x):

    open_seq_count, semi_open_seq_count = 0, 0
    if is_sq_in_board(board, y_start, x_start):
        for i in range (length):

            y = y_start + (i*d_y)
            x = x_start + (i*d_x)
            y_end = y_start + (i*d_y) + (length-1)*d_y
            x_end = x_start + (i*d_x) + (length-1)*d_x

            if is_sequence_complete(board, col, y, x, length, d_y, d_x) is True:

                if is_bounded(board, y_end, x_end, length, d_y, d_x) == "OPEN":
                    open_seq_count += 1
                elif is_bounded(board, y_end, x_end, length, d_y, d_x) == "SEMIOPEN":
                    semi_open_seq_count += 1

            # print(f"i: {i}, y_start: {y}, x_start: {x}, y_end: {y_end}, x_end: {x_end}, open: {open_seq_count}, semi: {open_seq_count}")

        return open_seq_count, semi_open_seq_count
    else:
        return None







def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0




    sequences = [[0, 1], [1, 0], [1, 1], [1, -1]]
    for s in range (len(sequences)):
        d_y = sequences[s][0]
        d_x = sequences[s][1]

    #horizontals
        if s == 0:
            for i in range(len(board)):
                y_start = i
                x_start = 0
                res = rows_helper(board, col, y_start, x_start, length, d_y, d_x)
                open_seq_count += res[0]
                semi_open_seq_count += res[1]

    #verticals
        elif s == 1:
            for i in range(len(board)):
                y_start = 0
                x_start = i
                res = rows_helper(board, col, y_start, x_start, length, d_y, d_x)
                open_seq_count += res[0]
                semi_open_seq_count += res[1]

    #top left to bottom right
        elif s == 2:
            for n in range (len(board)-1):
                y_start = 0
                x_start = n+1
                res = rows_helper(board, col, y_start, x_start, length, d_y, d_x)
                open_seq_count += res[0]
                semi_open_seq_count += res[1]
            for q in range (len(board)):
                y_start = q
                x_start = 0
                res = rows_helper(board, col, y_start, x_start, length, d_y, d_x)
                open_seq_count += res[0]
                semi_open_seq_count += res[1]

    #top right to bottom left
        elif s == 3:
            for n in range (len(board)):
                y_start = n
                x_start = len(board) - 1
                res = rows_helper(board, col, y_start, x_start, length, d_y, d_x)
                open_seq_count += res[0]
                semi_open_seq_count += res[1]
            for q in range (len(board)-1):
                y_start = 0
                x_start = q
                res = rows_helper(board, col, y_start, x_start, length, d_y, d_x)
                open_seq_count += res[0]
                semi_open_seq_count += res[1]

    return open_seq_count, semi_open_seq_count


def rows_helper(board, col, y_start, x_start, length, d_y, d_x):
    y_end = y_start + (length - 1) * d_y
    x_end = x_start + (length - 1) * d_x
    if detect_row(board, col, y_start, x_start, length, d_y, d_x) is not None:
        res = detect_row(board, col, y_start, x_start, length, d_y, d_x)
    return res





def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])




def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            #print("Open rows of length %d: %d" % (i, open))
            #print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print (game_res)


        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x






def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_is_bounded2():
    board = make_empty_board(8)
    x = 1; y = 1; d_x = 1; d_y = 1; length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 5
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")



def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y, x,length, d_y, d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0





if __name__ == '__main__':
    # easy_testset_for_main_functions()
    play_gomoku(8)