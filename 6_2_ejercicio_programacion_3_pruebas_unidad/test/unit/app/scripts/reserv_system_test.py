"""
This script contains the unittests for some of
the source code.
"""
import unittest
import os
import sys
sys.path.append(os.getenv('ROOT_PATH'))
from app.scripts.reserv_system import Hotel


class TestHotel(unittest.TestCase):
    """
    These are the test cases for Hotel
    """
    def setUp(self):
        """
        Set up variables so that we don't repeat it over each test case.
        """
        self.hotel = Hotel()

    def test_create_hotel_raises_typeerror_if_not_expected_schema(self):
        """
        Validate if an error araise if the variables don't
        comply with the schema
        """
        self.assertRaises(TypeError, self.hotel.create_hotel,
                          'a', 'b', 'c')

    def test_delete_hotel_raises_typeeror_if_not_int(self):
        """
        Validates if a TypeError is raised if the hotel id is not an integer.
        """
        self.assertRaises(TypeError, self.hotel.delete_hotel, 'a')

    def test_modify_hotel_information_raises_not_valid_hotel_attrs(self):
        """
        Validates if a ValueError raises if the attribute to be
        changed for a hotel, doesn't exist in the current catalogue.
        """
        self.assertRaises(ValueError, self.hotel.modify_hotel_information,
                          123, 'foo', 'var')

    def test_reserve_a_room_hotel_doesnt_exists(self):
        """
        Tests if a ValueError raises if the hotel doesn't exist in
        the current catalogue.
        """
        self.assertRaises(ValueError, self.hotel.reserve_a_room, -1, 1, 'anon')

    def test_cancel_a_reservation_raises_if_reservation_no_exists(self):
        """
        Tests if a IndexError is raised if the reservation id
        doesn't exists
        """
        self.assertRaises(IndexError, self.hotel.cancel_a_reservation, -1)


if __name__ == '__main__':
    unittest.main()
