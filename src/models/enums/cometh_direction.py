from enum import Enum


class ComethDirection(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    @classmethod
    def from_api_string(cls, cometh: str):
        direction_str = cometh.split("_")[0].lower()
        return cls(direction_str)
