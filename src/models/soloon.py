from src.models.astral_object import AstralObject
from src.models.enums.soloon_color import SoloonColor
from src.services.megaverse_service import MegaverseService


class Soloon(AstralObject):
    def __init__(self, row: int, column: int, color: SoloonColor):
        super().__init__(row, column)
        self.color = color

    def create(self, service: MegaverseService):
        service.create_soloon(self.row, self.column, self.color)

    def delete(self, service: MegaverseService):
        service.delete_soloon(self.row, self.column)
