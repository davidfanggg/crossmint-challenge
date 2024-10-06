import logging
from enum import Enum

from src.models.enums.cometh_direction import ComethDirection
from src.models.enums.soloon_color import SoloonColor
from src.clients.http_reliable_client import HttpReliableClient


class AstralObjectEndpoint(Enum):
    POLYANETS = "polyanets"
    SOLOONS = "soloons"
    COMETHS = "comeths"


class MegaverseService:
    BASE_URL = "https://challenge.crossmint.io/api"

    def __init__(self, candidate_id: str, http_client: HttpReliableClient):
        self.candidate_id = candidate_id
        self.http_client = http_client

    def get_goal_map(self):
        return self.http_client.get(
            f"{self.BASE_URL}/map/{self.candidate_id}/goal"
        ).json()["goal"]

    def delete_astral_object(
        self, row: int, column: int, astral_object_type: AstralObjectEndpoint
    ):
        logging.info(f"Deleting {astral_object_type.value} [{row}, {column}]")
        return self.http_client.delete(
            f"{self.BASE_URL}/{get_endpoint_for_astral_object(astral_object_type)}",
            json=create_payload(self.candidate_id, row, column),
        )

    # Polyanets
    def create_polyanet(self, row: int, column: int):
        logging.info(f"Creating Polyanet [{row}, {column}]")
        endpoint = get_endpoint_for_astral_object(AstralObjectEndpoint.POLYANETS)
        return self.http_client.post(
            f"{self.BASE_URL}/{endpoint}",
            json=create_payload(self.candidate_id, row, column),
        )

    def delete_polyanet(self, row: int, column: int):
        return self.delete_astral_object(row, column, AstralObjectEndpoint.POLYANETS)

    # Soloons
    def create_soloon(self, row: int, column: int, color: SoloonColor):
        logging.info(f"Creating soloon [{row}, {column}, {color.value}]")
        endpoint = get_endpoint_for_astral_object(AstralObjectEndpoint.SOLOONS)
        payload = create_payload(self.candidate_id, row, column)
        payload["color"] = color.value
        return self.http_client.post(f"{self.BASE_URL}/{endpoint}", json=payload)

    def delete_soloon(self, row: int, column: int):
        return self.delete_astral_object(row, column, AstralObjectEndpoint.SOLOONS)

    # Comeths
    def create_cometh(self, row: int, column: int, direction: ComethDirection):
        logging.info(f"Creating Cometh [{row}, {column}, {direction.value}]")
        endpoint = get_endpoint_for_astral_object(AstralObjectEndpoint.COMETHS)
        payload = create_payload(self.candidate_id, row, column)
        payload["direction"] = direction.value
        return self.http_client.post(f"{self.BASE_URL}/{endpoint}", json=payload)

    def delete_cometh(self, row: int, column: int):
        return self.delete_astral_object(row, column, AstralObjectEndpoint.COMETHS)


def create_payload(candidate_id: str, row: int, column: int):
    return {"row": row, "column": column, "candidateId": candidate_id}


def get_endpoint_for_astral_object(astral_object_endpoint: AstralObjectEndpoint):
    return astral_object_endpoint.value
