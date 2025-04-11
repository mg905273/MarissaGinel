import copy
import heapq
import time

class Puzzle:
    """A sliding-block puzzle."""

    def __init__(self, grid):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number, end="")
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        # YOU FILL THIS IN
        moves = []

        if self.grid[0][0] == ' ':
            return ['S', 'E']
        if self.grid[0][1] == ' ':
            return (['S', 'E', 'W'])
        if self.grid[0][2] == ' ':
            return ['S', 'W']
        if self.grid[1][0] == ' ':
            return ['N', 'S', 'E']
        if self.grid[1][1] == ' ':
            return ['N', 'S', 'E', 'W']
        if self.grid[1][2] == ' ':
            return ['N', 'S', 'W']
        if self.grid[2][0] == ' ':
            return ['N', 'E']
        if self.grid[2][1] == ' ':
            return ['N', 'E', 'W']
        if self.grid[2][2] == ' ':
            return ['N', 'W']
        return moves

    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""
        # YOU FILL THIS IN

        for x in range(len(self.grid)):  # x is index
            triggered = False
            for y in range(len(self.grid[x])):  # y is val
                if self.grid[x][y] == ' ':
                    triggered = True
                    break
            if triggered:
                break
        grid2 = copy.deepcopy(self.grid)
        if move == 'N':
            grid2[x][y] = self.grid[x - 1][y]
            grid2[x - 1][y] = ' '
        elif move == 'S':
            grid2[x][y] = self.grid[x + 1][y]
            grid2[x + 1][y] = ' '
        elif move == 'E':
            grid2[x][y] = self.grid[x][y + 1]
            grid2[x][y + 1] = ' '
        elif move == 'W':
            grid2[x][y] = self.grid[x][y - 1]
            grid2[x][y - 1] = ' '
        return Puzzle(grid2)

    def h(self, goal):
        """Compute the distance heuristic from this instance to the goal."""
        # YOU FILL THIS IN
        count = 0

        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y] != goal.grid[x][y]:
                    count += 1
        return count

    def h2(self, goal):
        distance = 0
        proper = {' ': (0, 0), 1:(0,1),2:(0,2),3:(1,0),4:(1,1),5:(1,2),6:(2,0),7:(2,1),8:(2,2)}

        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                # proper[1] -> (0, 1)
                # proper[2] -> (0, 2)
                # [[0, 1],
                #  [2, 3]]

                # proper[3][1]
                # proper[6][0]
                # x = [1, 2, 3]
                # x[1]
                value = self.grid[y][x] # 1
                desired_pos = proper[value] # (0, 1)
                diff_x = abs(desired_pos[0] - x)
                diff_y = abs(desired_pos[1] - y)
                distance += diff_x + diff_y
                # abs(difference between x and goal x) + abs(difference between y and goal y)
        return distance


class Node:

    def __init__(self, puzzle, moves, g, h):
        self.puzzle = copy.deepcopy(puzzle)
        self.moves = moves
        self.g = g
        self.h = h

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h

    def __eq__(self, other):
        return self.puzzle.grid == other.puzzle.grid

class Agent:
    """Knows how to solve a sliding-block puzzle with A* search."""

    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        # YOU FILL THIS IN
        # make finished an empty set
        finished = []
        # make frontier an empty priority queue add to start
        frontier = [Node(puzzle, [], 0, puzzle.h2(goal))]
        goal_node = Node(goal, [], 0, 0)
        # until frontier is empty
        while len(frontier) > 0:
            # take the min-priority parent off the frontier
            parent_node = heapq.heappop(frontier)
            if parent_node == goal_node:
                return parent_node.moves # Moves used to get to goal
            # 1. Add the parent node to finished
            # 2. Find possibles moves of the parent
            # 3. Go through moves and create children and add them to the frontier based off the moves (using a for loop)
            finished.append(parent_node)
            parent_puzzle = parent_node.puzzle
            # xs = [0, 1, 2, 3]
            # for x in xs:
            print(parent_puzzle)
            for m in parent_puzzle.moves():
                child_puzzle = parent_puzzle.neighbor(m)
                # [1, 2, 3] + [4] --> [1, 2, 3, 4]
                # [1, 2, 3] + [4. 5] --> [1, 2, 3, 4, 5]
                # parent_node.moves
                # m
                # parent_node.g
                child_node = Node(child_puzzle, parent_node.moves + [m], parent_node.g + 1, child_puzzle.h2(goal))
                # check that child is not in the frontier or the finished
                if child_node in frontier or child_node in finished:
                    continue
                heapq.heappush(frontier, child_node)






def main():
    """Create a puzzle, solve it with A*, and console-animate."""

    puzzle = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
    puzzle.display()

    agent = Agent()
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    path = agent.astar(puzzle, goal)

    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()


if __name__ == '__main__':
    main()