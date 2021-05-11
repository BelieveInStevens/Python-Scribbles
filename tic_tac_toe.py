the_board = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ',
             'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ',
             'Bot-L': ' ', 'Bot-M': ' ', 'Bot-R': ' '}

def board_printer(board):
    print(str(board['Top-L']) + '|' + str(board['Top-M']) + '|' + str(board['Top-R']))
    print('-+-+-')
    print(str(board['Mid-L']) + '|' + str(board['Mid-M']) + '|' + str(board['Mid-R']))
    print('-+-+-')
    print(str(board['Bot-L']) + '|' + str(board['Bot-M']) + '|' + str(board['Bot-R']))

turn = 'X'
for i in range(9):
    board_printer(the_board)
    print('It\'s ' + turn + '\'s turn! Which space do you want to mark?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
board_printer(the_board)
