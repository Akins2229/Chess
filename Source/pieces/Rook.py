import typing

from colors import White
from colors import Black

class Rook:
    def __init__(
        self,
        color: typing.Union(White, Black),
        pos: typing.Tuple[int, int]
    ) -> None:
        self.color=color
        self.rank=pos[0]
        self.file=pos[1]
        self.pos=pos

    def __str__(self) -> str:
        return "Rook"
