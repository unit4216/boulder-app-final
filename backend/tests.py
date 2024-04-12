import datetime
import unittest

from backend.aqi import get_predicted_aqi, get_past_aqi_data, get_next_hour


class TestAqi(unittest.TestCase):

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



