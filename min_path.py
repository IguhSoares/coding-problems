# Coding Problem #23
# Given an M by N matrix consisting of booleans representing a board
# Each True boolean represents a wall
# Each False boolean represents a tile to walk on
# Given this matrix, a start coordinate and a end coordinate:
# return the minimum number of steps to reach the end coordinate
# If there's no possible path, return null
# Can move Up, Down, Left or Right
# Not allowed: jump through walls or wrap around the edges of the board
from collections import namedtuple

board = [
    [False, False, False, False],
    [False, True, False, True],
    [False, True, False, False],
    [False, False, True, False],
    [False, True, False, False],
    [True, True, False, True],
    [False, False, False, False],
]


def get_neighbours(row, column, board):
    BoardSize = namedtuple("BoardSize", "rows columns")
    Position = namedtuple("Position", "row column")
    board_size = BoardSize(rows=len(board), columns=len(board[0]))
    neighbours = []

    positions = [
        Position(row + 1, column),
        Position(row - 1, column),
        Position(row, column + 1),
        Position(row, column - 1),
    ]

    for pos in positions:
        if (
            0 <= pos.row < board_size.rows
            and 0 <= pos.column < board_size.columns
            and board[pos.row][pos.column] != True
        ):
            neighbours.append((pos.row, pos.column))

    return neighbours


def adjacency_list(board):
    adjacency_list = {}
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != True:
                adjacency_list[(row, column)] = get_neighbours(row, column, board)
    return adjacency_list


def get_path(previous_pos, end):
    position = end
    path = []
    steps = -1
    while position != (-1, -1):
        path.insert(0, str(position))
        position = previous_pos[position]
        steps += 1
    Path = namedtuple("Path", "steps path")
    return Path(steps, path)


def min_path(board, start, end):
    neighbours_of = adjacency_list(board)
    checked = {}
    queue = [start]
    previous_step = {start: (-1, -1)}
    Path = namedtuple("Path", "steps path")
    path = Path(-1, [])
    # i = 0
    while queue != []:
        # while i < 10:
        current_pos = queue.pop(0)

        if current_pos == end:
            checked[current_pos] = True
            path = get_path(previous_step, end)
            break

        for position in neighbours_of[current_pos]:
            if not position in checked:
                previous_step[position] = current_pos
                queue.append(position)
        checked[current_pos] = True
        # i += 1

    return path


# print(adjacency_list(board))
result = min_path(board, (6, 0), (3, 0))
print(f"{result.steps} steps: " + " -> ".join(result.path))
