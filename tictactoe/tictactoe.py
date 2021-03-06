import random
import time

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'

        #set empty board at beginning
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def print_instructions(self):
        # TODO: Print the instructions to the game

        #print welcome message
        print("Welcome to TicTacToe! The first player to get 3 in a row wins. X will start!")

    def print_board(self):
        # TODO: Print the board

        #print empty board with row and col numbers
        print("\t0\t1\t2")
        counter = 0
        for a in self.board:
            print(counter, "\t", end="")
            counter = counter + 1
            for b in a:
                print(b, "\t", end="")
            print("")

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid

        #ensure move is within boundaries of the board
        if row > 2 or row < 0:
            return False
        if col > 2 or col < 0:
            return False
        #ensure move is in an empty spot on board
        if self.board[row][col] == '-':
            return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board

        #place player and inputted location on board
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot

        #get move from user input, confirm it is valid, and place player at inputted location
        isValid = False
        while True:
            r = int(input("Enter a row: "))
            c = int(input("Enter a column: "))
            isValid = self.is_valid_move(r, c)
            if isValid:
                break
            print("Please enter a valid move.")

        self.place_player(player, r, c)

    def take_turn(self, player, depth):
        # TODO: Simply call the take_manual_turn function

        if player == "O":
            #minimax player
            self.take_minimax_alpha_beta_turn(player, depth)
        else:
            #normal user player
            self.take_manual_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win

        #check 3 in a row of player (vertical win)
        for i in range(0,3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win

        #check 3 in a row of player (horizontal win)
        for r in self.board:
            if r == [player, player, player]:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win

        #check 3 in a row of player (diagonal left to right win)
        counter = 0
        for i in range(3):
            if self.board[i][i] == player:
                counter = counter + 1
        if counter == 3:
            return True
        counter = 0

        #check 3 in a row of player (diagonal right to left win)
        for a in range(3):
            if self.board[a][2-a] == player:
                counter = counter + 1
        if counter == 3:
            return True

        return False

    def check_win(self, player):
        # TODO: Check win

        #check all win cases
        if self.check_row_win(player):
            return True
        elif self.check_col_win(player):
            return True
        elif self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie

        #check tie
        if self.check_win("X") == True or self.check_win("O") == True:
            return False

        for i in self.board:
            for n in i:
                if n == '-':
                    return False
        return True

    #place player in a random, empty location on the board
    def take_random_turn(self, player):
        while True:
            row = random.randint(0,3)
            col = random.randint(0,3)
            isValid = self.is_valid_move(row, col)
            if isValid:
                break

        self.place_player(player, row, col)

    #place player according to minimax (AI) rules
    def take_minimax_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax(player, depth)
        end = time.time()
        print("This turn took:", end-start, "seconds.")
        self.place_player(player, row, col)

    def take_minimax_alpha_beta_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax_alpha_beta(player, depth, -100, 100)
        end = time.time()
        print("This turn took:", end-start, "seconds.")
        self.place_player(player, row, col)

    def minimax_alpha_beta(self, player, depth, alpha, beta):
        opt_row = -1
        opt_col = -1

        # base cases
        if self.check_win("O"):
            return (10, None, None)
        if self.check_tie():
            return (0, None, None)
        if self.check_win("X"):
            return (-10, None, None)
        if depth == 0:
            return (0, None, None)

        # find optimal move for player "O" - which move will make "O" win?
        if player == "O":
            best = -100
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == "-":
                        self.place_player("O", r, c)
                        score = self.minimax_alpha_beta("X", depth - 1, alpha, beta)[0]
                        alpha = max(alpha, score)
                        self.place_player("-", r, c)
                        if best < score:
                            best = score
                            opt_row = r
                            opt_col = c
                        if alpha >= beta:
                            return (best, opt_row, opt_col)


            return (best, opt_row, opt_col)

        # find optimal move for player "X" - which move will make "X" lose?
        if player == "X":
            worst = 100
            for a in range(3):
                for b in range(3):
                    if self.board[a][b] == "-":
                        self.place_player("X", a, b)
                        score = self.minimax_alpha_beta("O", depth - 1, alpha, beta)[0]
                        beta = min(beta, score)
                        self.place_player("-", a, b)

                        if worst > score:
                            worst = score
                            opt_row = a
                            opt_col = b
                        if beta <= alpha:
                            return (worst, opt_row, opt_col)


            return (worst, opt_row, opt_col)

    #optimize player move based on best outcome for player "O"
    def minimax(self, player, depth):
        opt_row = -1
        opt_col = -1

        #base cases
        if self.check_win("O"):
            return (10, None, None)
        if self.check_tie():
            return (0, None, None)
        if self.check_win("X"):
            return (-10, None, None)
        if depth == 0:
            return (0, None, None)

        #find optimal move for player "O" - which move will make "O" win?
        if player == "O":
            best = -100
            for r in range(3):
                for c in range(3):
                    if self.board[r][c] == "-":
                        self.place_player("O", r, c)
                        score = self.minimax("X", depth-1)[0]
                        if best < score:
                            best = score
                            opt_row = r
                            opt_col = c
                        self.place_player("-", r, c)
            return (best, opt_row, opt_col)

        #find optimal move for player "X" - which move will make "X" lose?
        if player == "X":
            worst = 100
            for a in range(3):
                for b in range(3):
                    if self.board[a][b] == "-":
                        self.place_player("X", a, b)
                        score = self.minimax("O", depth-1)[0]
                        if worst > score:
                            worst = score
                            opt_row = a
                            opt_col = b

                        self.place_player("-", a, b)
            return (worst, opt_row, opt_col)

    def play_game(self):
        # TODO: Play game

        #main game control
        gameOver = False
        player = "X"
        self.print_instructions()
        self.print_board()
        while gameOver is False:
            self.take_turn(player, 100)
            self.print_board()
            if self.check_win(player):
                print(player, " won!")
                break
            elif self.check_tie():
                print("You tied!")
                break
            if player == "X":
                player = "O"
                print("O's turn!")
            else:
                player = "X"
                print("X's turn!")
        print ("Game Over")

