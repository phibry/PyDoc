emptyboard = ["   ", " | ", "   ", " | ", "   ",
              "---", "---", "---", "---", "---",
              "   ", " | ", "   ", " | ", "   ",
              "---", "---", "---", "---", "---",
              "   ", " | ", "   ", " | ", "   "]

boarddesc = [" 1 ", " | ", " 2 ", " | ", " 3 ",
             "---", "---", "---", "---", "---",
             " 4 ", " | ", " 5 ", " | ", " 6 ",
             "---", "---", "---", "---", "---",
             " 7 ", " | ", " 8 ", " | ", " 9 "]


# First Row:    [0][2][4]
# Second Row:   [10][12][14]
# Third row:    [20][22][24]

emptyboard[24] = " O "


def board_desc(desc):
    print("Board Description:")
    for i in range(0, len(desc) - 1, 5):
        print(desc[i] + desc[i + 1] + desc[i + 2] + desc[i + 3] + desc[i + 4])
    print("\n")


def create_board(board):
    for i in range(0, len(board) - 1, 5):
        print(board[i] + board[i + 1] + board[i + 2] +
              board[i + 3] + board[i + 4])
    print("\n")


def win_condition(board):
    # 8 different possibilites to win a game
    def check(board):
        booleanlist = []
        conditions = {"C1": [1, 2, 3], "C2": [4, 5, 6], "C3": [7, 8, 9], "C4": [
            1, 4, 7], "C5": [2, 5, 8], "C6": [3, 6, 9], "C7": [1, 5, 9], "C8": [3, 5, 9]}
        for i in range(1, 9):
            a, b, c = conditions["C" + str(i)]
            to_check = [board[board_generator[a]][1] +
                        board[board_generator[b]][1] + board[board_generator[c]][1]]
            if to_check == ['XXX'] or to_check == ['OOO']:
                booleanlist.append(True)
                break
            else:
                booleanlist.append(False)
        return booleanlist
    return True in check(board)


# 8 different possibilites to win a game
# def check(board):
#     booleanlist = []
#     conditions = {"C1": [1, 2, 3], "C2": [4, 5, 6], "C3": [7, 8, 9], "C4": [
#         1, 4, 7], "C5": [2, 5, 8], "C6": [3, 6, 9], "C7": [1, 5, 9], "C8": [3, 5, 9]}
#     for i in range(1, 9):
#         a, b, c = conditions["C" + str(i)]
#         to_check = [board[board_generator[a]][1] +
#                     board[board_generator[b]][1] + board[board_generator[c]][1]]
#         print(to_check == ['XXX'] or to_check == ['OOO'])
#         if to_check == ['XXX'] or to_check == ['OOO']:
#             booleanlist.append(True)
#             print("Winner found")
#             break
#         else:
#             booleanlist.append(False)
#     # return


board_desc(boarddesc)

create_board(emptyboard)


board_generator = {1: 0, 2: 2, 3: 4,
                   4: 10, 5: 12, 6: 14,
                   7: 20, 8: 22, 9: 24}


userinput1 = board_generator[9]
emptyboard[userinput1] = " X "
create_board(emptyboard)

userinput2 = board_generator[8]
emptyboard[userinput2] = " O "
create_board(emptyboard)

userinput1 = board_generator[1]
emptyboard[userinput1] = " X "
create_board(emptyboard)

userinput2 = board_generator[2]
emptyboard[userinput2] = " O "
create_board(emptyboard)

userinput1 = board_generator[5]
emptyboard[userinput1] = " X "
create_board(emptyboard)

print(win_condition(emptyboard))
