import copy
import time
import abc
import random


class Game(object):
    """A connect four game."""

    def __init__(self, grid):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()

    def possible_moves(self):
        """Return a list of possible moves given the current board."""
        # YOU FILL THIS IN
        moves = []
        for row in range(7,-1,-1):
            for col in range(8):
                if self.grid[row][col] == '-' and col not in moves:
                    moves.append((col))
        return moves

    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        # YOU FILL THIS IN
        for row in range(7, -1, -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = color
                break
        return Game(self.grid)

    def utility(self):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN
        # similar to h - check all

        # i_look = [] #indexes looked at
        #red 3 in a row vertically
        utility_value = 0

        for row in range(8):
            for col in range(5):
                one = self.grid[row][col]
                two = self.grid[row][col + 1]
                three = self.grid[row][col + 2]
                four = self.grid[row][col + 3]
                if one == two and one == three and one == four:
                    if one == 'R' and two == 'R' and three == 'R' and four == '-':
                        utility_value += 10
                    elif one == 'B' and two == 'B' and three == 'B' and four == '-':
                        utility_value += 10
                    elif one == 'R' and two == 'R' and three == '-' and four == '-':
                        utility_value += 4
                    elif one == 'B' and two == 'B' and three == '-' and four == '-':
                        utility_value += 4
                    elif one == 'R' and two == '-' and three == '-' and four == '-':
                        utility_value += 1
                    elif one == 'B' and two == '-' and three == '-' and four == '-':
                        utility_value += 1


        # Check cols
        for col in range(8):
            for row in range(5):
                one = self.grid[row][col]
                two = self.grid[row + 1][col]
                three = self.grid[row + 2][col]
                four = self.grid[row + 3][col]
                if one == two and one == three and one == four:
                    if one == 'R' and two == 'R' and three == 'R' and four == '-':
                        utility_value += 10
                    elif one == 'B' and two == 'B' and three == 'B' and four == '-':
                        utility_value += 10
                    elif one == 'R' and two == 'R' and three == '-' and four == '-':
                        utility_value += 4
                    elif one == 'B' and two == 'B' and three == '-' and four == '-':
                        utility_value += 4
                    elif one == 'R' and two == '-' and three == '-' and four == '-':
                        utility_value += 1
                    elif one == 'B' and two == '-' and three == '-' and four == '-':
                        utility_value += 1
        return utility_value




    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins; #literal
           0 if board full; None if not full and no winner"""
        # YOU FILL THIS IN
        # Check rows
        for row in range(8):
            for col in range(5):
                one = self.grid[row][col]
                two = self.grid[row][col + 1]
                three = self.grid[row][col + 2]
                four = self.grid[row][col + 3]
                if one == two and one == three and one == four:
                    if one == 'R' and two == 'R' and three == 'R' and four == 'R':
                        return float("inf")
                    elif one == 'B' and two == 'B' and three == 'B' and four == 'B':
                        return float("-inf")

        # Check cols
        for col in range(8):
            for row in range(5):
                one = self.grid[row][col]
                two = self.grid[row + 1][col]
                three = self.grid[row + 2][col]
                four = self.grid[row + 3][col]
                if one == two and one == three and one == four:
                    if one == 'R' and two == 'R' and three == 'R' and four == 'R':
                        return float("inf")
                    elif one == 'B' and two == 'B' and three == 'B' and four == 'B':
                        return float("-inf")

        # Check diags
        # Check way one diags
        for row in range(5):
            for col in range(5):
                one = self.grid[row][col]
                two = self.grid[row + 1][col + 1]
                three = self.grid[row + 2][col + 2]
                four = self.grid[row + 3][col + 3]
                if one == two and one == three and one == four:
                    if one == 'R' and two == 'R' and three == 'R' and four == 'R':
                        return float("inf")
                    elif one == 'B' and two == 'B' and three == 'B' and four == 'B':
                        return float("-inf")

        # Check way two diags
        for row in range(5):
            for col in range(5):
                one = self.grid[row + 3][col]
                two = self.grid[row + 2][col + 1]
                three = self.grid[row + 1][col + 2]
                four = self.grid[row][col + 3]
                if one == two and one == three and one == four:
                    if one == 'R' and two == 'R' and three == 'R' and four == 'R':
                        return float("inf")
                    elif one == 'B' and two == 'B' and three == 'B' and four == 'B':
                        return float("-inf")

        if "-" in self.grid[0] or "-" in self.grid[1] or "-" in self.grid[2] or "-" in self.grid[3] or "-" in self.grid[
            4] or "-" in self.grid[5] or "-" in self.grid[6] or "-" in self.grid[7]:
            return None
        else:
            return 0

class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass


class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        # YOU FILL THIS IN
        # think possible moves using random object return random move
        move_native = False
        while not move_native :
            move_rand = random.randint(0,7)
            for m in Game.possible_moves(game):
                if m == move_rand:
                    move_native = True
        return move_rand


class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""

    def move(self, game):
        """Returns the first possible move"""
        # YOU FILL THIS IN
        # call moves and then pick the first move
        moves_poss = game.possible_moves()
        return moves_poss[0]


class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""

    def move(self, game):
        """Returns the best move using minimax"""
        minimax_move = self.min_value(game, 4, -1)
        utility = [minimax_move[0]]
        col = minimax_move[1]
        utility.append(float('-inf'))
        best_util = max(utility)
        # print('UTILITY:', best_util, 'COLUMN:', col)
        return col

    def max_value(self, game, depth, col):
        val = []
        # if a state is a completed game, return its utility
        if depth == 1 or game.winning_state() is not None:
            x = (game.utility(), col)
            return x
        # calculate max of min value children
        else:
            x = float('-inf')
            for c in game.possible_moves():
                game1 = Game(game.grid.copy())
                game1.neighbor(c, 'R')
                val.append(self.min_value(game1, depth - 1, c))
            utility_values = [i[0] for i in val]
            utility_values.append(x)
            new_score = max(utility_values)
            col = val[utility_values.index(new_score)][1]
            return [new_score, col]

    def min_value(self, game, depth, col):
        # if a state is a completed game, return its utility
        val = []
        if depth == 1 or game.winning_state() is not None:
            y = (game.utility(), col)
            return y
        # calculate min of max value children
        else:
            y = float('inf')
            for c in game.possible_moves():
                game1 = Game(game.grid.copy())
                game1.neighbor(c, 'B')
                val.append(self.max_value(game1, depth - 1, c))
            utility_values = [i[0] for i in val]
            utility_values.append(y)
            new_score = min(utility_values)
            col = val[utility_values.index(new_score)][1]
            return [new_score, col]

def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0,0,0
    for i in range(simulations):

        game = single_game(io=False)

        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1

    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" % (redwin,redwin/simulations*100,blackwin,blackwin/simulations*100,tie))

    return redwin/simulations


def single_game(io=True):
    """Create a game and have two agents play it."""

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = MinimaxAgent('R')
    minplayer = RandomAgent('B')

    while True:

        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game


if __name__ == '__main__':
    single_game(io=True)
    #tournament(simulations=50)