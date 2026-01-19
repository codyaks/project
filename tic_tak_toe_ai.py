import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def coloured_cell(cell):
        if cell=='X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell=='O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + coloured_cell(board[0]) + ' | ' + coloured_cell(board[1]) + ' | ' + coloured_cell(board[2]) )
    print(Fore.CYAN + '-----------')
    print(' ' + coloured_cell(board[3]) + ' | ' + coloured_cell(board[4]) + ' | ' + coloured_cell(board[5]) )
    print(Fore.CYAN + '-----------')
    print(' ' + coloured_cell(board[6]) + ' | ' + coloured_cell(board[7]) + ' | ' + coloured_cell(board[8]) )
    print()
def player_choice():
    symbol=""
    while symbol not in ['X','O']:
        symbol=input(Fore.GREEN + "Choose your symbol (X/O): " + Style.RESET_ALL).upper()
    if symbol=='X':
        return ('X','O')
    else:
        return ('O','X')
def player_move(board, symbol):
    move=-1
    while move not in range(1,10) or not board[move-1].isdigit():
        try:
            move=int(input(Fore.GREEN + "please enter the position of your move (1-9)"))
            if move not in range(1,10) or not board[move-1].isdigit():
                print(Fore.RED + "Invalid move. Try again." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 9." + Style.RESET_ALL)
    board[move-1]=symbol
def check_win(board, symbol):
    win_conditions=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for cond in win_conditions:
        if board[cond[0]]==board[cond[1]]==board[cond[2]]==symbol:
            return True
    return False

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy=board.copy()
            board_copy[i]=ai_symbol
            if check_win(board_copy,ai_symbol):
                board[i]=ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
           board_copy=board.copy()
           board_copy[i]=player_symbol
           if check_win(board_copy,player_symbol):
                 board[i]=ai_symbol
                 return   
    possible_moves=[i for i in range(9) if board[i].isdigit()]
    move=random.choice(possible_moves)
    board[move]=ai_symbol
def check_full(board):
    for cell in board:
        if cell.isdigit():
            return False
    return True
def tic_tac_toe():
    print(Fore.MAGENTA + "Welcome to Tic Tac Toe!" + Style.RESET_ALL)
    name=input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
      board=['1','2','3','4','5','6','7','8','9']
      player_symbol, ai_symbol=player_choice()
      turn='player'
      game_on=True
      while game_on:
        display_board(board)
        if turn=='player':
            player_move(board,player_symbol)
            if check_win(board,player_symbol):
                display_board(board)
                print(Fore.GREEN + f"Congratulations {name}, you won!"+ Style.RESET_ALL)
                game_on=False
            else:
                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                    game_on=False
                else:
                    turn='ai'
        else:
            ai_move(board,ai_symbol,player_symbol)
            if check_win(board,ai_symbol):
                display_board(board)
                print(Fore.RED + "AI wins! Better luck next time." + Style.RESET_ALL)
                game_on=False
            else:
                if check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                    game_on=False
                else:
                    turn='player'
      replay=input(Fore.GREEN + "Do you want to play again? (y/n): " + Style.RESET_ALL).lower()
      if replay!='y':
            print(Fore.MAGENTA + "Thanks for playing Tic Tac Toe!" + Style.RESET_ALL)
            break
if __name__=="__main__":
    tic_tac_toe()

