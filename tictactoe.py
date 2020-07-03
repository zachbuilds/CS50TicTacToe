"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    num_empty = board.count("EMPTY")

    if num_empty % 2 == 0:
        return "O"
    else:
        return "X"

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    available = set()
    for i in board:
        for j in board:
            if board[i][j] == "EMPTY":
                available.add(i, j)

    return available

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    newBoard = copy.deepcopy(board)
    i, j = action

    if (player(board) == "X"):
        newBoard[i][j] = "X"
    else:
        newBoard[i][j] = "O"

    return newBoard

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(0, len(board)):
        if board[i].contains("X") == 3:
            return "X"
        elif board[i].contains("O") == 3:
            return "O"

        for j in range(0, len(board)):
            if board[j][i].contains("X") == 3:
                return "X"
            elif board[j][i].contains("O") == 3:
                return "O"

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[]

    for col in 
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
