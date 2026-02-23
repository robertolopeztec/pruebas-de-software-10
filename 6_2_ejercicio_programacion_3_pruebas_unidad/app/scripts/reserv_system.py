"""
This file contains the core objects for the reservation system.
> Assumes that the core script is run from the root path.
"""
import os
import json

CATALOGUE_DIR = 'app/data/'


def read_content_from_file(file: str):
    """
    This function takes a filepath as input and opens a data file.
    """

    with open(file, 'r', encoding='utf8') as f:
        content = json.load(f)
        f.close()
    return content


class Hotel():
    """
    The core Hotel class
    """
    def __init__(self):
        self.hotel_file = os.path.join(CATALOGUE_DIR, 'hotels.json')
    
    def create_hotel(self, hotel_id: int, hotel_name: str, hotel_rooms: int):
        """
        Generate a new record within the hotel catalogue.
        """

        # Validate if the schema for creating a hotel is valid
        if (
            isinstance(hotel_id, int)
            and isinstance(hotel_name, str)
            and isinstance(hotel_rooms, int)
        ):
            raise TypeError('Invalid type: {}, {}, {}'.format(type(hotel_id),
                                                              type(hotel_name),
                                                              type(hotel_rooms)
                                                             )
                           )

        # content = read_content_from_file(self.hotel_file)

if __name__ == '__main__':

    h = Hotel()
    print(h.hotel_file)
    h.create_hotel('s', 's', 2)

    
    

        
        
    