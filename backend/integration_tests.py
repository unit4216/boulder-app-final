import datetime
import unittest
from unittest.mock import Mock

from backend.aqi import get_past_aqi_data


class TestAqiIntegration(unittest.TestCase):

    def test_get_past_aqi_data(self):

        results = get_past_aqi_data('42.3601', '71.0589')





