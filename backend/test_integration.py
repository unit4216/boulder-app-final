import datetime
import unittest
from unittest.mock import Mock

from aqi import get_past_aqi_data, parse_aqi_data, get_predicted_aqi, get_next_hour


class TestAqiIntegration(unittest.TestCase):

    def test_get_past_aqi_data(self):
        aqi_data = get_past_aqi_data('42.3601', '71.0589')
        parsed_data = parse_aqi_data(aqi_data)
        now = datetime.datetime.now()
        next_hour = get_next_hour(now)
        predicted_aqi = get_predicted_aqi(parsed_data, next_hour)
        # we can't test the exact AQI since the API call gets the last 7 days from the current day,
        # but we can verify that the predicted AQI is in a valid range
        assert 0 < float(predicted_aqi) < 500

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

