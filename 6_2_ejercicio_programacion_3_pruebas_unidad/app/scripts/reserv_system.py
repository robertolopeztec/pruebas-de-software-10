"""
This file contains the core objects for the reservation system.
"""
import os


def read_content_from_file(file: str):
    """
    This function takes a filepath as input and opens a data file.
    """

    with open(file, 'r', encoding='utf8') as f:
        content = f.readlines()
        f.close()
    return content


class Hotel(object):
    def create_hotel(self, hotel_id: str, hotel_name: str):
        """
        Generate a new record within the hotel catalogue.
        """


if __name__ == '__main__':
    x = read_content_from_file('/data/hotels.csv')
    

    
    

        
        
    