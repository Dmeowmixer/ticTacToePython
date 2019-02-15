from IPython.display import clear_output

def display_board(board):
  print( board[7] + '|' + board[8] + '|' + board[9])
  print( board[4] + '|' + board[5] + '|' + board[6])
  print( board[1] + '|' + board[2] + '|' + board[3])

# test_board = ['#', 'X','O','X','O','X','O','X','O','X']
game_board = ['', '', '','','','','','','','']
display_board(game_board)

playerOne = ''
playerTwo = ''

playerWon = false



def player_input():
  print('Player One Choose X or O')
  inputString = ''
  inputString = input().upper()
  print('Player One has chosen '+ inputString)

  if inputString == 'X':
    playerTwo = 'O'

  else: playerTwo = 'X'
  print('Player Two is '+ playerTwo)

player_input()

while not playerWon:
  # Play/Continue the game



def place_marker(board, marker, position):
  board[position] = marker
place_marker(game_board, playerOne, 1)
display_board(game_board)


def win_check(board, mark):
   if ((board[0] == mark and board[1] == mark and board[2] == mark) or
        (board[3] == mark and board[4] == mark and  board[5] == mark) or
        (board[6] == mark and board[7] == mark and board[8] == mark) or
        (board[5] == mark and board[3] == mark and board[0] == mark) or
        (board[7] == mark and board[4] == mark and board[1] == mark) or
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        (board[0] == mark and board[4] == mark and board[9] == mark) or
        (board[2] == mark and board[4] == mark and board[6] == mark)):
        playerWon = true
        return 'Player '  + mark + ' has won!'

win_check(game_board, 'O')