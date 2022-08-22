class Player:
  def __init__(self, name, player_board=[], attacks_history=[]):
    self.name = name
    self.player_board = player_board
    self.attacks_history = attacks_history
  
  def board_creation(self):
    board = [['o','o','o','o','o','o'],
             ['o','o','o','o','o','o'],
             ['o','o','o','o','o','o'],
             ['o','o','o','o','o','o'],
             ['o','o','o','o','o','o'],
             ['o','o','o','o','o','o']]

    print('''Each one of the players has a board of 6x6 where they will have to position 3 ships, with a size of 1, 2 and 3 spaces respectively \n''')
    print('''Next, the acommodation of each player ship will be done. For this, the home position and orientation of the ship will be asked.  ''')
    print('--------------------------------------------------------------------------------------------------------------------\n')
    print('-----------------------------------------------PLAYER ', self.name,('-----------------------------------------------\n'))
    print('--------------------------------------------------------------------------------------------------------------------\n')
    l=0
    while l <= 2:
        control = 0
        try:
          while control == 0:
              row = int(input('Introduce the # of the row (1-6) where you want to locate the ship: '))
              column = int(input('Introduce the # of the column (1-6) where you want to locate the ship: '))
              orientation = input ('Introduce the letter of the orientation of the ship. UP (U), DOWN (D), LEFT (L), RIGHT (R):  ')
              print('\n')
              current_ship = Ship(l+1)
              final_column = column
              final_row = row
              if (orientation.upper() == 'U'):
                  final_row = row - (current_ship.size - 1)
              elif (orientation.upper() == 'D'):
                  final_row = row + (current_ship.size - 1)
              elif (orientation.upper() == 'L'):
                  final_column = column - (current_ship.size - 1)
              elif (orientation.upper() == 'R'):
                  final_column = column + (current_ship.size - 1)

              if (orientation.upper() == 'U' or orientation.upper() == 'D' or orientation.upper() == 'L' or orientation.upper() == 'R') and (row >= 1 and row <= 6) and (column >= 1 and column <= 6) and (final_row >= 1 and final_row <= 6) and (final_column >= 1 and final_column <= 6):
                  control = 1
                  board_ready = current_ship.ship_location(row, column, final_row, final_column, orientation, board)
                  l = l + 1
              else: 
                  print ('The information is out of boundaries. Please try again.')
                  print('--------------------------------------------------------------------------------------------------------------------\n')
        except:
          print('--------------------------------------------------------------------------------------------------------------------\n')
          print ('The information was not introduced in the specified format. Try again.\n')
          print('--------------------------------------------------------------------------------------------------------------------\n')
    return board_ready  
  

  def attack(self,rival_board, your_board, attacks_board):
    attack_control = 0
    win_condition = 0
    print('------------------------------------------------TURN--------------------------------------------------------------\n')
    print('-----------------------------------------------PLAYER ', self.name,('-----------------------------------------------\n'))
    print('--------------------------------------------------------------------------------------------------------------------\n')
    print('This is how your board looks: \n')
    print('* = sank; x = alive; o = empty')
    print_board(your_board)
    print('This is how your attacks history board looks. Check it out so you can define your next attack. \n')
    print('* = on target; o = missed; ' ' = not explored')
    print_board(attacks_board)

    
    while attack_control == 0:
      try:
        att_row = int(input('Introduce the # of the row (1-6) that you want to attack: '))
        att_column = int(input('Introduce the # of the row (1-6) that you want to attack: '))
        clear()
        if att_row >= 1 and att_row <= 6 and att_column >= 1 and att_column <= 6:
          attack_control = 1
          if rival_board[att_row-1][att_column-1] == 'x':
            rival_board[att_row-1][att_column-1] = '*'
            attacks_board[att_row-1][att_column-1] = '*'
            print('NICE SHOT!  YOUR ATTACK WAS SUCCESSFUL! YOU HIT A SHIP!')
            print('''
                      ██████╗░░█████╗░░█████╗░███╗░░░███╗
                      ██╔══██╗██╔══██╗██╔══██╗████╗░████║
                      ██████╦╝██║░░██║██║░░██║██╔████╔██║
                      ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
                      ██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║
                      ╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝ \n''')
            counter =  0
            its_here = 0
            while win_condition == 0 and counter <= 5 and its_here == 0:
              if 'x' in rival_board[counter]:
                its_here = 1
              elif (counter == 5):
                win_condition = 1
              counter = counter + 1
          elif rival_board[att_row-1][att_column-1] == 'o':
            attacks_board[att_row-1][att_column-1] = 'o'
            print('You did not hit any ship. Nice try.')
          else:
            print('You did not hit any new ship. That was a repeated attack :(.')

          if win_condition == 0:
            print('This is how your attacks history board looks. After your attack. \n')
            print_board(attacks_board)
        else:
          print ('The information is out of boundaries. Please try again.')
          print('--------------------------------------------------------------------------------------------------------------------\n')
      except:
        print('--------------------------------------------------------------------------------------------------------------------\n')
        print ('The information was not introduced in the specified format. Try again.\n')
        print('--------------------------------------------------------------------------------------------------------------------\n')

    return win_condition


class Ship:
  def __init__(self, size):
    self.size = size

  def ship_location(self, in_row, in_column, fin_row, fin_column, orientation, board):
    if (orientation.upper() == 'D'): 
      for m in range(in_row-1,fin_row):
        board[m][in_column-1]  = 'x'
    if (orientation.upper() == 'U'):
      for m in range(fin_row-1, in_row):
        board[m][in_column-1]  = 'x'
    elif (orientation.upper() == 'R'):
      for m in range(in_column-1,fin_column):
        board[in_row-1][m]  = 'x'
    elif (orientation.upper() == 'L'):
      for m in range(fin_column-1,in_column):
        board[in_row-1][m]  = 'x'
    return board

def att_hist_board():
    att_hist=[[' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ']]
    return att_hist

def print_board(board):
    for j in range (6):
      print(board[j])
    print('--------------------------------------------------------------------------------------------------------------------\n')
    print('--------------------------------------------------------------------------------------------------------------------\n')
    input('Press enter to continue.')
    clear()    

def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
    _ = system('clear')

#MAIN CODE
from os import system, name

print ('''
          BBBBBB       AAAA       TTTTTT      TTTTTT      LL          EEEEEE      SSSSSS      HH  HH      II      PPPPPP
          BB  BB      AA  AA        TT          TT        LL          EE          SS          HH  HH      II      PP  PP
          BBBBBB      AAAAAA        TT          TT        LL          EEEE        SSSSSS      HHHHHH      II      PPPPPP
          BB  BB      AA  AA        TT          TT        LL          EE              SS      HH  HH      II      PP
          BBBBBB      AA  AA        TT          TT        LLLLLL      EEEEEE      SSSSSS      HH  HH      II      PP\n''')
name1 = input('Introduce the name of player 1: ')
name2 = input('Introduce the name of player 2: ')
if name1 == name2:
  name2+='2'
player1 = Player(name1)
player2 = Player(name2)

player1.player_board = player1.board_creation()
print_board(player1.player_board)

player2.player_board = player2.board_creation()
print_board(player2.player_board)

player1.attacks_history = att_hist_board()
player2.attacks_history = att_hist_board()

end_game = 0 
turn = 0

while end_game == 0:
  turn = turn + 1
  if (turn%2) != 0:
    end_game = player1.attack(player2.player_board, player1.player_board, player1.attacks_history)
    winner = player1.name
  else:
    end_game = player2.attack(player1.player_board, player2.player_board, player2.attacks_history)
    winner = player2.name
clear()
print ('''
          CCCCCC      OOOOOO      NN   NN      GGGGGG      RRRRRR       AAAA       TTTTTT      SSSSSS      !!
          CC          OO  OO      NNN  NN      GG          RR  RR      AA  AA        TT        SS          !!
          CC          OO  OO      NN N NN      GGGGGG      RRRRRR      AAAAAA        TT        SSSSSS      !!
          CC          OO  OO      NN  NNN      GG  GG      RRRR        AA  AA        TT            SS
          CCCCCC      OOOOOO      NN   NN      GGGGGG      RR  RR      AA  AA        TT        SSSSSS      !! \n''')
print(winner, '!')
print('AMAZING PERFORMANCE!')
print('YOU WON!')