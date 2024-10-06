from src.models.astral_object import AstralObject
from src.services.megaverse_service import MegaverseService


class Polyanet(AstralObject):
    def __init__(self, row: int, column: int):
        super().__init__(row, column)

    def create(self, service: MegaverseService):
        service.create_polyanet(self.row, self.column)

    def delete(self, service: MegaverseService):
        service.delete_polyanet(self.row, self.column)
