from IPython.display import clear_output

def display_board(board):
  print( board[7] + '|' + board[8] + '|' + board[9])
  print( board[4] + '|' + board[5] + '|' + board[6])
  print( board[1] + '|' + board[2] + '|' + board[3])

test_board = ['#', 'X','O','X','O','X','O','X','O','X']
game_board = ['', '', '','','','','','','','']
display_board(game_board)

playerOne = ''
playerTwo = ''

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

def place_marker(board, marker, position):
  board[position] = marker
place_marker(game_board, playerOne, 1)
display_board(game_board)

def win_check(board, mark):
  if board[2] == mark and board[5] == mark and board[8] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[1] == mark and board[4] == mark and board[7] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[3] == mark and board[6] == mark and board[9] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[1] == mark and board[5] == mark and board[9] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[3] == mark and board[5] == mark and board[7] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[1] == mark and board[2] == mark and board[3] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[4] == mark and board[5] == mark and board[6] == mark:
    print(mark + 'Wins THE GAME!')
  elif board[7] == mark and board[8] == mark and board[9] == mark:
    print(mark + 'Wins THE GAME!')

win_check(game_board, 'O')