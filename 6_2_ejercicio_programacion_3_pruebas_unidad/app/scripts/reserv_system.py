"""
This file contains the core objects for the reservation system.
> Assumes that the core script is run from the root path.
"""
import os
import json

CATALOGUE_DIR = 'app/data/'

def read_content_from_file(file: str) -> None:
    """
    This function takes a filepath as input and opens a data file.
    """

    with open(file, 'r', encoding='utf8') as f:
        content = json.load(f)
        f.close()
    return content


def write_content_to_file(content: dict, file: str) -> None:
    """
    This function takes a .JSON-like content and writes it into a file.
    """

    with open(file, 'w', encoding='utf8') as f:
        json.dump(content, f, indent=4)
    f.close()


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
        if not (
            isinstance(hotel_id, int)
            and isinstance(hotel_name, str)
            and isinstance(hotel_rooms, int)
        ):
            vars_ = [hotel_id, hotel_name, hotel_rooms]
            vars_ = [str(type(var)) for var in vars_]
            vars_ = ', '.join(vars_)

            type_error_message = f'Expected types: {int}, {str}, {str}\n'
            type_error_message += 'Found instead:'
            type_error_message += vars_

            raise TypeError(type_error_message)

        # Take the current hotel attributes and append it into content
        hotel = {'id': hotel_id, 'name': hotel_name, 'rooms': hotel_rooms}
        content = read_content_from_file(self.hotel_file)
        content.append(hotel)
        write_content_to_file(content, self.hotel_file)

    def delete_hotel(self, hotel_id: int):
        """
        Given a hotel id, then remove it from the hotels catalogue.
        """

        if not isinstance(hotel_id, int):
            raise TypeError(f'hotel_id {type(hotel_id)}; expected {str(int)}')

        content = read_content_from_file(self.hotel_file)
        cleaned_content = [
                            hotel for hotel in content
                            if hotel['id'] != hotel_id
                          ]
        write_content_to_file(cleaned_content, self.hotel_file)

    
    def display_hotel_information(self, hotel_id: int):
        """
        Given a hotel id, then display its information.
        """
        content = read_content_from_file(self.hotel_file)
        hotel = [hotel for hotel in content
                 if hotel['id'] == hotel_id
                ][0]

        print(hotel)

if __name__ == '__main__':
    h = Hotel()
    print(h.hotel_file)
    # print(h.create_hotel(2, 'Mexicanito', 10))
    # h.delete_hotel('s')
    # print(h.delete_hotel(2))
    print(h.display_hotel_information(123))

    
