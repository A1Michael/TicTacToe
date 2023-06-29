import math
import time
from player import HumanPlayer, RandomComputerPlayer, ComputerSim
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # creat a single list to rep our board
        self.current_winner = None  # keep track of winner

    def print_board(self):
        # .board[i*3:(i+1)*3] means which group of 3 spaces are we choosing
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_num():
        # shows us what number corresponds to what box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]  # show the indecies of each of the rows
        for row in number_board:
            print('|' + ' | '.join(row) + ' |')

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]



    def make_move(self, square, letter):
        # if valid move then we make the move ( assign square to letter)
        # then return true if invalid
        if self.board[square] == ' ':  # if the board is empty
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):  # leaving this out to test if winner will run outside the class

        # check if any 3 rows == X or Y
        # first check the rows
        row_index = math.floor(square / 3)  # devide by 3 then round (//) it down
        row = self.board[row_index*3:(row_index+1)*3]  # given the row index , get the row
        if all([target_letter == letter for target_letter in row]):  # all if all statements evaluate to true
            return True
        # then check the collumns
        col_ind = square % 3  # returns the index of our square
        column = [self.board[col_ind+i*3] for i in range(3)]  # get everything in the column
        if all([target_letter == letter for target_letter in column]):
            return True
        # finally check the diagonals
        # check if the squares is an even number 0,2,4,6,8 as these are the only moves possible to win diagonally
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # first diagonal from the top left to the bottom right
            if all([target_letter == letter for target_letter in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to bottom left diagonal
            if all([target_letter == letter for target_letter in diagonal2]):
                return True
        # if all these fail
        return False

    def empty_squares(self):
        return ' ' in self.board  # returns True if the cell is empty

    def num_empty_squares(self):  # return the number of empty squares
        return self.board.count(' ')

    def available_moves(self):
        # using list comprehension to reduce the code
        return [i for i, spot in enumerate(self.board) if spot == ' ']


def playGame(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_num()
    letter = 'X'  # starting letter
    while game.empty_squares():
        print("empty squares passed")
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(1.0)


if __name__ == '__main__':
    player_x = HumanPlayer('X')
    player_o = ComputerSim('O')
    game = TicTacToe()
    playGame(game, player_x, player_o, print_game=True)


