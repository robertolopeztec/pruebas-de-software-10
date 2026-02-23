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

    def test_modify_hotel_information_raises_valueerror_if_not_in_valid_hotel_attrs(self):
        valid_hotel_attrs = ['id', 'name', 'rooms']
        self.assertRaises(ValueError, self.hotel.modify_hotel_information,
                          123, 'foo', 'var')

    def test_reserve_a_room_hotel_doesnt_exists(self):
        self.assertRaises(ValueError, self.hotel.reserve_a_room, -1, 1, 'anon')


    def test_cancel_a_reservation_raises_indexerror_if_reservation_id_doesnt_exists(self):
        self.assertRaises(IndexError, self.hotel.cancel_a_reservation, -1)


if __name__ == '__main__':
    unittest.main()