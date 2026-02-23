import unittest
import sys
import os
sys.path.append(os.getenv('ROOT_PATH'))

from app.scripts.reserv_system import Hotel

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()

    def test_create_hotel_raises_typeerror_if_not_expected_schema(self):
        self.assertRaises(TypeError, self.hotel.create_hotel,
                          'a', 'b', 'c'
                         )
    def test_delete_hotel_raises_typeeror_if_not_int(self):
        self.assertRaises(TypeError, self.hotel.delete_hotel, 'a')


if __name__ == '__main__':
    unittest.main()