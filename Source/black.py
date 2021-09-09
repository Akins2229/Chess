import typing
import colors

#import pieces
from pieces import *

class Black:
    def __init__(
        self,
        pieces: typing.List(typing.Union(
            Knight,
            Bishop,
            King,
            Queen,
            Pawn,
            Rook
        ))=[
            Knight,
            Knight,
            Bishop,
            Bishop,
            King,
            Queen,
            Pawn,
            Pawn,
            Pawn,
            Pawn,
            Pawn,
            Pawn,
            Pawn,
            Pawn,
            Rook,
            Rook
        ] # set to default list config
    ) -> None:
        
        self.pieces=[pieces]
        self.color=colors.Black().__str__()
