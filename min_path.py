"""Coding Problem #23

Given an M by N matrix consisting of booleans representing a board:
    Each True boolean represents a wall
    Each False boolean represents a tile to walk on

Given this matrix, a start coordinate and a end coordinate:
    return the minimum number of steps to reach the end coordinate
    If there's no possible path, return null

Can move Up, Down, Left or Right
Not allowed: jump through walls or wrap around the edges of the board
"""
from typing import Dict, List, NamedTuple

class BoardSize(NamedTuple):
    rows: int
    columns: int

    def __str__(self):
        return f'{self.rows}x{self.columns}'
    
    def __repr__(self):
        return f'BoardSize(rows={self.rows}, columns={self.columns})'


class Position(NamedTuple):
    row: int
    column: int

    def __str__(self):
        return f'({self.row}, {self.column})'
    
    def __repr__(self):
        return f'Position(row={self.row}, column={self.column})'


class Path(NamedTuple):
    steps: int
    path: List[str]

    def __str__(self):
        path: str = ' -> '.join(self.path)
        return f'{self.steps} steps: {path})'
    
    def __repr__(self):
        return f'Path(steps={self.steps}, path={self.path})'


board: List[List[bool]] = [
    [False, False, False, False],
    [False, True, False, True],
    [False, True, False, False],
    [False, False, True, False],
    [False, True, False, False],
    [True, True, False, True],
    [False, False, False, False],
]

"""Builds a list of possible positions to go from the current position

If a given position corresponds to a wall ('True' in the board),
    it will not be added to the neighbours list
"""
def get_neighbours(row: int, column: int, board: List[List[bool]]) -> List[Position]:
    board_size = BoardSize(rows=len(board), columns=len(board[0]))
    neighbours: List[Position] = []

    positions = [
        Position(row + 1, column),
        Position(row - 1, column),
        Position(row, column + 1),
        Position(row, column - 1),
    ]

    """Checks if positon is a wall
    If a board has a different definition of a wall, only this method
    should be modified accordingly
    """
    def a_wall(position: Position) -> bool:
        return board[position.row][position.column]

    # Verifies if the position is valid (not a wall and not out of board range)
    for pos in positions:
        # If it is valid, appends it to the neighbours list:
        if (
            0 <= pos.row < board_size.rows
            and 0 <= pos.column < board_size.columns
            and not a_wall(Position(pos.row, pos.column))
        ):
            neighbours.append(Position(pos.row, pos.column))

    return neighbours


"""Builds an adjacency list with valid positions to go from a given position"""
def adjacency_list(board: List[List[bool]]) -> Dict[Position, List[Position]]:
    adjacency_list: Dict[Position, List[Position]] = {}
    # Iterates through every row and column of the board:
    for row in range(len(board)):
        for column in range(len(board[row])):
            # If current position is not a wall:
            if board[row][column] != True:
                # Inserts it in the adjacency list with all its valid moves
                adjacency_list[(row, column)] = get_neighbours(row, column, board)
    return adjacency_list


"""Builds a list with all the positions in the path from the start to the end position"""
def get_path(previous_pos: Dict[Position, Position], end: Position) -> Path:
    # Traverses the path list from the end position back to the start
    position: Position = end
    path: List[str] = []
    # If start == end, zero steps are needed, so steps is initialized with -1
    steps: int = -1
    # The previous position of the start point is (-1, -1)
    while position != Position(-1, -1):
        path.insert(0, str(position))
        position = previous_pos[position]
        steps += 1
    return Path(steps, path)


"""Finds the path with the minimun number of steps, from start to end position"""
def min_path(board: List[List[bool]], start: Position, end: Position) -> Path:
    neighbours_of = adjacency_list(board)
    # Tracks the already checked positions:
    checked: Dict[Position, bool] = {}
    queue = [start]
    # Tracks the previous step of a given position:
    previous_steps = {start: Position(-1, -1)}
    # Default value if no path is found:
    path: str = f"There is no path between {start} and {end}"

    while queue != []:
        current_pos = queue.pop(0)

        if current_pos == end:
            checked[current_pos] = True
            path = get_path(previous_steps, end)
            break

        # Gets every possible move from current_pos:
        for position in neighbours_of[current_pos]:
            if not position in checked:
                # Marks current_pos as previous_step of position:
                previous_steps[position] = current_pos
                # Appends it to the queue to contiue searching for the end position
                queue.append(position)
        checked[current_pos] = True

    return path


result = min_path(board, (6, 0), (3, 0))
print(f'{result}')
