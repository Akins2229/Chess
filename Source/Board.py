import colors
from pieces import *
import typing

from errors import *
import players

ranks = {
    'a': 0,
    'b': 1,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7
}

class Move:
    def __init__(
        self,
        rank: typing.Union(str, int),
        file: int,
        new_rank: typing.Union(str, int),
        new_file: int
    ) -> None:
        if isinstance(rank, str):
            try:
                rank=ranks[rank]
            except KeyError:
                raise InvalidRankError(rank)
        self.pos=(rank, file)
        self.new_pos(new_rank, new_file)

class Board:
    def __init__(
        self,
        white: players.White,
        black: players.Black,
        board_state: typing.Union(
            str,
            typing.List(
                typing.Union(
                    Knight,
                    Rook,
                    Bishop,
                    King,
                    Queen,
                    Pawn
                )
            )
        )=[
            [
                Rook(
                    colors.Black(),
                    (0, 0)
                ),
                Knight(
                    colors.Black(),
                    (1, 0)
                ),
                Bishop(
                    colors.Black(),
                    (2, 0)
                ),
                Queen(
                    colors.Black(),
                    (3, 0)
                ),
                King(
                    colors.Black(),
                    (4, 0)
                ),
                Bishop(
                    colors.Black(),
                    (5, 0)
                ),
                Knight(
                    colors.Black(),
                    (6, 0)
                ),
                Rook(
                    colors.Black(),
                    (7, 0)
                )
            ],
            [
                Pawn(
                    colors.Black(),
                    (0, 1)
                ),
                Pawn(
                    colors.Black(),
                    (1, 1)
                ),
                Pawn(
                    colors.Black(),
                    (2, 1)
                ),
                Pawn(
                    colors.Black(),
                    (3, 1)
                ),
                Pawn(
                    colors.Black(),
                    (4, 1)
                ),
                Pawn(
                    colors.Black(),
                    (5, 1)
                ),
                Pawn(
                    colors.Black(),
                    (6, 1)
                ),
                Pawn(
                    colors.Black(),
                    (7, 1)
                )
            ],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [
                Pawn(
                    colors.White(),
                    (0, 6)
                ),
                Pawn(
                    colors.White(),
                    (1, 6)
                ),
                Pawn(
                    colors.White(),
                    (2, 6)
                ),
                Pawn(
                    colors.White(),
                    (3, 6)
                ),
                Pawn(
                    colors.White(),
                    (4, 6)
                ),
                Pawn(
                    colors.White(),
                    (5, 6)
                ),
                Pawn(
                    colors.White(),
                    (6, 6)
                ),
                Pawn(
                    colors.White(),
                    (7, 6)
                )
            ],
            [
                Rook(
                    colors.White(),
                    (0, 7)
                ),
                Knight(
                    colors.White(),
                    (1, 7)
                ),
                Bishop(
                    colors.White(),
                    (2, 7)
                ),
                King(
                    colors.White(),
                    (3, 7)
                ),
                Queen(
                    colors.White(),
                    (4, 7)
                ),
                Bishop(
                    colors.White(),
                    (5, 7)
                ),
                Knight(
                    colors.White(),
                    (6, 7)
                ),
                Rook(
                    colors.White(),
                    (7, 7)
                )
            ]
        ]
    ) -> None:
        self.board=board_state
        self.white=white
        self.black=black

    def make_move(
        self,
        move: Move,
    ) -> bool:
        piece = self.board[move.pos[0]][move.pos[1]]
        if piece.is_legal(move.new_pos):
            self.board[move.pos[0]][move.pos[1]] = 0
            self.board[move.new_pos[0]][move.pos[1]] = piece
            piece.rank = move.new_pos[0]
            piece.file = move.new_pos[1]
            piece.pos = (move.new_pos[0], piece.new_pos[1])
            return True
        else:
            return False