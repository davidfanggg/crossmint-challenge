from src.models.astral_object import AstralObject
from src.models.enums.cometh_direction import ComethDirection
from src.services.megaverse_service import MegaverseService


class Cometh(AstralObject):
    def __init__(self, row: int, column: int, direction: ComethDirection):
        super().__init__(row, column)
        self.direction = direction

    def create(self, service: MegaverseService):
        service.create_cometh(self.row, self.column, self.direction)

    def delete(self, service: MegaverseService):
        service.delete_cometh(self.row, self.column)
