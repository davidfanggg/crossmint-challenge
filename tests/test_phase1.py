import unittest
from unittest.mock import MagicMock, patch

from src.phase1 import run_phase_1


class TestRunPhase1(unittest.TestCase):

    def test_run_phase_1(self):
        mock_megaverse_service = MagicMock()
        run_phase_1(mock_megaverse_service)

        expected_calls = [
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (6, 4),
            (7, 3),
            (8, 2),
            (4, 6),
            (3, 7),
            (2, 8),
        ]

        self.assertEqual(
            len(expected_calls), mock_megaverse_service.create_polyanet.call_count
        )
        for row, column in expected_calls:
            mock_megaverse_service.create_polyanet.assert_any_call(row, column)

    @patch("logging.error")
    def test_run_polyanets_creation_failure(self, mock_logging):
        mock_megaverse_service = MagicMock()
        mock_megaverse_service.create_polyanet.side_effect = Exception("Test exception")
        run_phase_1(mock_megaverse_service)

        mock_logging.assert_called_once_with("An error occurred: Test exception")


if __name__ == "__main__":
    unittest.main()
