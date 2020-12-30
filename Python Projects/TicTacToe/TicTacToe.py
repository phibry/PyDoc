def board_desc(desc):
  print("Board Description:")
  for i in range(0, len(desc) - 1, 5):
    print(desc[i] + desc[i + 1] + desc[i + 2] + desc[i + 3] + desc[i + 4])
  print("\n")


def create_board(board):
  for i in range(0, len(board) - 1, 5):
    print(board[i] + board[i + 1] + board[i + 2] +
          board[i + 3] + board[i + 4])


def player_markers():
  marker = ''
  while marker not in ["X", "O"]:  # Check if Input is X or O, else: Try again
    marker = input("Player 1: Do you want to play as X or O: ").upper()
  if marker == "X":
    markers = {"P1": " X ", "P2": " O "}
    return markers
  else:
    markers = {"P1": " O ", "P2": " X "}
    return markers


def whose_turn(i):
  # Which players turn
  userinput = 0
  while userinput not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    if i % 2 == 0:
      userinput = input("Player 1: Place your marker: ")
      turn = "P1"
    else:
      userinput = input("Player 2: Place your marker: ")
      turn = "P2"
  return int(userinput), turn


def place_marker(markers, playboard, i, userinput, turn):
  global board_generator
  # Check if location already has a marker in place
  while playboard[board_generator[userinput]] != "   ":
    userinput = int(
        input("At this location has already a marker been placed, choose another: "))

  playboard[board_generator[userinput]] = markers[turn]
  return playboard


def win_condition(board):
    # 8 different possibilites to win a game
  def check(board):
    global board_generator
    booleanlist = []
    conditions = {"C1": [1, 2, 3], "C2": [4, 5, 6], "C3": [7, 8, 9], "C4": [
        1, 4, 7], "C5": [2, 5, 8], "C6": [3, 6, 9], "C7": [1, 5, 9], "C8": [3, 5, 7]}
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


def replay():
  return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')


def play():
  while True:
    # Are you ready?
    play_game = input("Are you ready to play? Enter Yes or No: ")
    if play_game.lower()[0] == 'y':
      game_on = True
    else:
      game_on = False

    markers = player_markers()
    # Define markers for the two players
    print(f'Player 1 is {markers["P1"]} and Player 2 is {markers["P2"]}')

    # Show Board Description
    boarddesc = [" 1 ", " | ", " 2 ", " | ", " 3 ",
                 "---", "---", "---", "---", "---",
                 " 4 ", " | ", " 5 ", " | ", " 6 ",
                 "---", "---", "---", "---", "---",
                 " 7 ", " | ", " 8 ", " | ", " 9 "]

    board_desc(boarddesc)

    # Starting Board
    emptyboard = ["   ", " | ", "   ", " | ", "   ",
                  "---", "---", "---", "---", "---",
                  "   ", " | ", "   ", " | ", "   ",
                  "---", "---", "---", "---", "---",
                  "   ", " | ", "   ", " | ", "   "]
    playboard = emptyboard
    create_board(playboard)

    i = 2
    while game_on:
      if i == 11:
        print("Nobody won")
        break
      userinput, turn = whose_turn(i)
      place_marker(markers, playboard, i, userinput, turn)
      create_board(playboard)
      if win_condition(playboard):
        print(f"{turn} won!")
        game_on = False
        # break
      print("\n")

      i += 1
    if not replay():
      break


board_generator = {1: 0, 2: 2, 3: 4,
                   4: 10, 5: 12, 6: 14,
                   7: 20, 8: 22, 9: 24}


play()
