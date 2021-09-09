import typing

class InvalidRankError(Exception):
    def __init__(
        self,
        rank: str
    ) -> None:
        self.exc = "Rank must be of one of values ['a', 'b', 'c', 'd', 'e', 'f', 'g'], not {}".format(rank)

    def __repr__(
        self
    ) -> str:
        return self.exc
