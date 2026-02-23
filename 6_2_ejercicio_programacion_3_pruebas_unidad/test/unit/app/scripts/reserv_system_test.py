import unittest
from app.scripts.reserv_system import Hotel


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()

    def test_create_hotel_raises_typeerror_if_not_expected_schema(self):
        self.assertRaises(TypeError, self.hotel.create_hotel,
                          'a', 'b', 'c'
                         )

    