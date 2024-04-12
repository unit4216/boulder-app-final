import datetime
import unittest
from unittest.mock import Mock

from backend.aqi import get_past_aqi_data, parse_aqi_data, get_predicted_aqi


class TestAqiIntegration(unittest.TestCase):

    def test_get_past_aqi_data(self):

        results = get_past_aqi_data('42.3601', '71.0589')

    # tests integration between `parse_aqi_data` and `get_predicted_aqi`
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

