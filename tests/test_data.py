import os
import unittest
from stestdata import TestData


class Test(unittest.TestCase):

    def setUp(self):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'stestdata'))

    def test_list_sensors(self):
        self.assertEquals(TestData.sensors, ['landsat8', 'sentinel2'])

    def test_sensor_path(self):
        # test with all flag
        t = TestData('landsat8')
        self.assertTrue(isinstance(t.examples, dict))
        self.assertTrue('small_full_data_cloudy' in t.examples)
        self.assertEquals(t.examples['small_full_data_cloudy']['B1']['filename'], 'test_B1.tif')
