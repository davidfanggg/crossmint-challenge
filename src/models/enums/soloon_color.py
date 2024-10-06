from enum import Enum


class SoloonColor(Enum):
    BLUE = "blue"
    RED = "red"
    PURPLE = "purple"
    WHITE = "white"

    @classmethod
    def from_api_string(cls, soloon_string: str):
        direction_str = soloon_string.split("_")[0].lower()
        return cls(direction_str)
