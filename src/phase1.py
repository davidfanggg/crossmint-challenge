import logging
from models.polyanet import Polyanet
from services.megaverse_service import MegaverseService
from src.clients.http_reliable_client import HttpReliableClient


GRID_SIZE = 11
SKIPPED_ROWS = {0, 1, 9, 10}


def run_phase_1(megaverse_service):
    try:
        for row in range(GRID_SIZE):
            for column in range(GRID_SIZE):
                if row not in SKIPPED_ROWS:
                    if row == column or row == (GRID_SIZE - 1 - column):
                        polyanet = Polyanet(row=row, column=column)
                        polyanet.create(megaverse_service)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    candidate_id = "9ef847a6-9142-4816-90a6-bfab7215d49c"
    http_client = HttpReliableClient(recovery_timeout=10)
    main_megaverse_service = MegaverseService(candidate_id, http_client)
    run_phase_1(main_megaverse_service)
