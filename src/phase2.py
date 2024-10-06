import logging
from models.cometh import Cometh
from models.soloon import Soloon
from src.clients.http_reliable_client import HttpReliableClient
from services.megaverse_service import ComethDirection, MegaverseService, SoloonColor
from src.models.polyanet import Polyanet


def create_soloon_from_map(row, column, soloon_string):
    color = SoloonColor.from_api_string(soloon_string)
    soloon = Soloon(row=row, column=column, color=color)
    soloon.create(megaverse_service)


def create_cometh_from_map(row, column, cometh_string):
    direction = ComethDirection.from_api_string(cometh_string)
    cometh = Cometh(row=row, column=column, direction=direction)
    cometh.create(megaverse_service)


def create_polyanet_from_map(row, column):
    polyanet = Polyanet(row=row, column=column)
    polyanet.create(megaverse_service)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    candidate_id = "9ef847a6-9142-4816-90a6-bfab7215d49c"
    http_client = HttpReliableClient(recovery_timeout=10)
    megaverse_service = MegaverseService(candidate_id, http_client)

    goal_map = megaverse_service.get_goal_map()
    try:
        for row, row_content in enumerate(goal_map):
            for column, astral_object_string in enumerate(row_content):
                if "COMETH" in astral_object_string:
                    create_cometh_from_map(
                        row=row, column=column, cometh_string=astral_object_string
                    )
                if "SOLOON" in astral_object_string:
                    create_soloon_from_map(
                        row=row, column=column, soloon_string=astral_object_string
                    )
                if astral_object_string == "POLYANET":
                    create_polyanet_from_map(row=row, column=column)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
