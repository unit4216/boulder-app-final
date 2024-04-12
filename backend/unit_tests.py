import datetime
import unittest

from backend.aqi import get_predicted_aqi, get_next_hour, parse_aqi_data
from unittest.mock import Mock


class TestAqiUnit(unittest.TestCase):

    def test_get_predicted_aqi_mock(self):
        mock_return = {
            "hourly": {
                "time": [
                    '2024-01-01T11:00',
                    '2024-01-02T11:00',
                    '2024-01-03T11:00',
                    '2024-01-04T11:00',
                    '2024-01-05T11:00',
                    '2024-01-06T11:00',
                    '2024-01-07T11:00',
                    '2024-01-07T13:00'
                ],
                "us_aqi": [
                    10, 10, 10, 20, 20, 30, 40, 999
                ]
            }
        }
        mock_aqi_api = Mock()
        mock_aqi_api.return_value = mock_return
        api_return = mock_aqi_api()

        parsed_data = parse_aqi_data(api_return)
        aqi = get_predicted_aqi(parsed_data, 11)

        self.assertEqual(aqi, '20.0')

    def test_get_predicted_aqi(self):
        sample_data = [
            {"time": "2022-01-01T11:00", "aqi": 8},
            {"time": "2022-01-01T11:00", "aqi": 8},
            {"time": "2022-01-01T11:00", "aqi": 10},
            {"time": "2022-01-01T11:00", "aqi": 10},
            {"time": "2022-01-01T11:00", "aqi": 10},
            {"time": "2022-01-01T11:00", "aqi": 12},
            {"time": "2022-01-01T11:00", "aqi": 12},
            {"time": "2022-01-01T14:00", "aqi": 900},
        ]
        hour = 11
        results = get_predicted_aqi(sample_data, hour)
        self.assertEqual(results, '10.0')

    def test_get_next_hour_normal(self):
        test_date = datetime.datetime(2024, 11, 6, 12, 0, 0)
        results = get_next_hour(test_date)
        self.assertEqual(results, 13)

    def test_get_next_hour_edge(self):
        test_date = datetime.datetime(2024, 11, 6, 23, 0, 0)
        results = get_next_hour(test_date)
        self.assertEqual(results, 0)



