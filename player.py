import math
import random

class Player:
    def __init__(self,letter):
        #letter is X or O could be whatever based on the input
        self.letter = letter
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    # initialize the super class
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # check that this is a correct value by trying to cast
            # it to an integer, anf if it's invalid
            # if that spot is no longer available on the board , we also say its invalid
            try:
                val = int(square)  # cast the value inserted into a string for try
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if it passes it
            except ValueError:
                print('invalid square. try again')
        return val  # return once we have a valid square
class ComputerSim(Player):
    def _init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #  using the minimax algorithm get the square
            square = self.minimax(game, self.letter)['Position']
        return square

    def minimax(self, game, player):
        max_player = self.letter  # set the player as the maximum
        min_payer = 'O' if player == 'X' else 'X'  # set the PC to be the min

        # check if the previous move was a winning move to begin with
        if game.current_winner == min_payer:
            # return the score and position to keep track of
            return {'Position': None,
                    'Score': 1 * (game.num_empty_squares() + 1) if min_payer == max_player
                    else -1 * (game.num_empty_squares() + 1)}
        elif not game.empty_squares():  # if there are no empty sqaures its a tie
            return {'Position': None, 'Score': 0}

        if player == max_player:
            best_result = {'Position': None, 'Score': -math.inf}
        else:
            best_result = {'Position': None, 'Score': math.inf}
        for possible_moves in game.available_moves():
            # make a move , try a spot
            game.make_move(possible_moves, player)

            # recurse using minimax to simulate a game after making the move
            simulated_score = self.minimax(game, min_payer)

            #  undo the previous move so we can try again in the next iteration
            game.board[possible_moves] = ' '
            game.current_winner = None
            simulated_score['Position'] = possible_moves  # prevents recursion from errors

            #  update the dictionaries if the move beats the current best score
            if player == max_player:
                if simulated_score['Score'] > best_result['Score']:
                    best_result = simulated_score  # this becomes the new best move
            else:
                if simulated_score['Score'] < best_result['Score']:
                    best_result = simulated_score  # this becomes the new best move
        return best_result  # return a dic of best possible move and score