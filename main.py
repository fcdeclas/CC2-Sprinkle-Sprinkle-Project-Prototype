import curses
import random
from prompt import prompt
from combat import combat
from boss import boss_fight


def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    stack = [(1, 1)]

    while stack:
        current_cell = stack[-1]
        maze[current_cell[0]][current_cell[1]] = ' '

        neighbors = [
            (current_cell[0] - 2, current_cell[1]),
            (current_cell[0] + 2, current_cell[1]),
            (current_cell[0], current_cell[1] - 2),
            (current_cell[0], current_cell[1] + 2),
        ]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 < neighbor[0] < rows and 0 < neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == '#']

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            maze[(current_cell[0] + next_cell[0]) // 2][(current_cell[1] + next_cell[1]) // 2] = ' '
            stack.append(next_cell)
        else:
            stack.pop()

    place_treasures(maze, rows, cols)
    return maze

def place_treasures(maze, rows, cols):
    treasures = 0
    min_distance_between_treasures = 4  # Adjust this value based on your preference

    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    while treasures < 3:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)

        if maze[row][col] == ' ' and (row, col) != (1, 1):  # Ensure it's not the starting position
            # Check proximity with existing treasures
            too_close = any(distance((row, col), treasure) < min_distance_between_treasures for treasure in [(i, j) for i in range(rows) for j in range(cols) if maze[i][j] == 'T'])

            if not too_close:
                maze[row][col] = 'T'
                treasures += 1


def print_maze(stdscr, maze, player_pos):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                stdscr.addch(i, j * 2, 'P')
            else:
                stdscr.addch(i, j * 2, cell)


def move_player(player_pos, key):
    row, col = player_pos
    if key == curses.KEY_UP:
        return row - 1, col
    elif key == curses.KEY_DOWN:
        return row + 1, col
    elif key == curses.KEY_LEFT:
        return row, col - 1
    elif key == curses.KEY_RIGHT:
        return row, col + 1
    else:
        return player_pos

class Treasures:
    def __init__(self, name):
        self.name = name

    # INSTANCES OF TREASURES CLASS
Dragon_Tear = Treasures("Solidified Dragon's Tear")
Dragon_Heart = Treasures("Encased Dragon Heart")
Blood_Vessels = Treasures("Clumpt Blood Vessels of a Dragon")


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    rows = 11
    cols = 21
    maze = generate_maze(rows, cols)
    player_pos = (1, 1)

    uncollected_treasures = [Dragon_Tear.name, Dragon_Heart.name, Blood_Vessels.name]
    inventory = []

    while True:
        stdscr.clear()
        stdscr.addstr(5, 45, f"  Bag of Holding: {inventory}", curses.A_BOLD)

        if maze[player_pos[0]][player_pos[1]] == 'T':
            stdscr.addstr(7, 45, f"You have found something eerie.")
            stdscr.addstr(8, 45, "To place in your bag press the Spacebar")
            if key == ord(' '):
                maze[player_pos[0]][player_pos[1]] = ' '
                found_treasures = uncollected_treasures.pop()
                inventory.append(found_treasures)
            stdscr.refresh()

        stdscr.addstr(4, 45, f" Player moved to position: {player_pos}",curses.A_BOLD)
        stdscr.refresh()
        print_maze(stdscr, maze, player_pos)
        stdscr.addstr(11, 0, "Move with arrow keys. Press Esc to exit. ", curses.A_REVERSE)
 
        key = stdscr.getch()

        chance_of_encounter = random.randint(1,100)
        if chance_of_encounter <= 60:
            stdscr.addstr(20, 45, "You are not found.")
            stdscr.refresh()
        else:
            combat(stdscr)
            stdscr.refresh()


        if len(inventory) == 3:
            boss_fight(stdscr)

        if key == 27:
            break

        new_pos = move_player(player_pos, key)
        if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] != '#':
            player_pos = new_pos


prompt()
curses.wrapper(main)