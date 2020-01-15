import random


def display_board(board):

    temp_board = []
    for i in range(0, 10):
        temp_board.append(board[i])
    adder = 3
    index = 1

    for looper in range(0, 3):
        if temp_board[index] == 0:
            temp_board[index] = ' '
        if temp_board[index+1] == 0:
            temp_board[index+1] = ' '
        if temp_board[index+2] == 0:
            temp_board[index+2] = ' '
        print(' {} | {} | {}'.format(temp_board[index], temp_board[index+1],
                                     temp_board[index+2]))
        if looper == 0 or looper == 1:
            print("----------")
        index += adder


def player_input(mark_p1, mark_p2):
    mark_p1 = input('First player, please pick a marker "X" or "O" : ').upper()
    mark_p2 = ''
    while mark_p1 != "X" and mark_p1 != "O":
        mark_p1 = input('First player, please\
             pick a marker "X" or "O" : ').upper()
    if mark_p1 == 'X':
        mark_p2 = 'O'
    else:
        mark_p2 = 'X'
    print("1st Player is : {} and 2nd Player is : {}".format(mark_p1, mark_p2))
    return mark_p1, mark_p2


def place_marker(board, marker, position):
    board[int(position)] = marker


def win_check(board, mark):
    base = 1
    win = False
    if win is False:
        base = 1
        for i in range(0, 3):
            if (board[base] == board[base+1] == board[base+2] == mark):
                print("{} Wins! Congratulations!".format(mark))
                win = True
                break
            else:
                base += 3
    if win is False:
        base = 1
        for i in range(0, 3):
            if (board[base] == board[base+3] == board[base+6] == mark):
                print("{} Wins! Congratulations!".format(mark))
                win = True
                break
            else:
                base += 1
    if win is False:
        if (board[1] == board[5] == board[9] == mark
           or board[3] == board[5] == board[7] == mark):
            print("{} Wins! Congratulations!".format(mark))
            win = True
    return win


def choose_first():
    player_list = ['Player 1', 'Player 2']
    chosen_one = player_list[random.randint(0, 1)]
    print("{} goes first!".format(chosen_one))
    return chosen_one


def space_check(board, position):
    if board[int(position)] == 0:
        return True
    else:
        return False


def full_board_check(board):
    count = 9
    for i in range(1, 10):
        if board[i] != 0:
            count -= 1
        else:
            continue
    return count == 0


def player_choice(board):
    choice = input("Which position do you want to make your move on? : ")
    if space_check(board, choice):
        return choice
    else:
        print("Position {} is already full.".format(choice))
        return player_choice(board)


def replay():
    again = input("Do you want to play again? (Y/N)").upper()
    return again == "Y"


while True:
    board = ['#', 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_player = choose_first()
    if first_player == "Player 2":
        second_player = "Player 1"
    else:
        second_player = "Player 2"

    mark_p1 = ''
    mark_p2 = ''
    mark_p1, mark_p2 = player_input(mark_p1, mark_p2)
    game_on = True

    while game_on:
        if full_board_check(board):
            break

        # Player 1 Turn
        print("Current Board\n-----------")
        display_board(board)
        print("-----------\nYour turn, {}.\n".format(first_player))
        position_choice = player_choice(board)
        place_marker(board, mark_p1, position_choice)
        winOrNot = win_check(board, mark_p1)
        if winOrNot:
            break

        if full_board_check(board):
            break

        # Player 2 Turn
        print("Current Board\n-----------")
        display_board(board)
        print("-----------\nYour turn, {}.\n".format(second_player))
        position_choice = player_choice(board)
        place_marker(board, mark_p2, position_choice)
        winOrNot = win_check(board, mark_p2)
        if winOrNot:
            break

    if not replay():
        game_on = False
    if not game_on:
        print("See you later!")
        break
