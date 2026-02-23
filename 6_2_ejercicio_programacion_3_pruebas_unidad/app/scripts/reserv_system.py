"""
This file contains the core objects for the reservation system.
> Assumes that the core script is run from the root path.
"""
import os
import json
import random

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
        self.reservation_file = os.path.join(CATALOGUE_DIR, 'reservations.json')

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

    def modify_hotel_information(self, hotel_id: int, hotel_attr: str, hotel_val: [str, int]):
        """
        This function modifies the information for a single attribute for a hotel, given its id,
        the attribute and the actual value to modify.
        """
        content = read_content_from_file(self.hotel_file)

        # Validate if the hotel attribute to modify is available within the schema
        valid_hotel_attrs = ['id', 'name', 'rooms']
        if hotel_attr not in valid_hotel_attrs:
            raise ValueError(f'{hotel_attr} not in {valid_hotel_attrs}')

        # Find the hotel to change, modify its attribute, replace it in its original index
        # and then overwrite the catalogue with the new information
        ix, hotel_to_change = [(i, hotel) for i, hotel in enumerate(content)
                              if hotel['id'] == hotel_id][0]
        
        hotel_to_change[hotel_attr] = hotel_val
        content[ix] = hotel_to_change

        write_content_to_file(content, self.hotel_file)

    
    def reserve_a_room(self, hotel_id: int,
                       hotel_room_number: int,
                       guest: str = 'anon'
                      ):
        """
        Reserve a room given hotel_id, the room number and the guest.
        The guest can be anonymous, it's the default.
        """

        # Get the reservation id
        hotel_content = read_content_from_file(self.hotel_file)
        hotel_ids = list({hotel['id'] for hotel in hotel_content})

        # Validate if the hotel exists.
        if hotel_id not in hotel_ids:
            raise ValueError(f'hotel_id={hotel_id} NOT in catalogue!')

        # If the validation passes, then consolidate the attributes and
        # update the reservations data
        reservation_id = random.randint(1, 999)
        reservation_content = read_content_from_file(self.reservation_file)
        
        reservation_attrs = {
            'id': reservation_id,
            'hotel_id': hotel_id,
            'hotel_room_number': hotel_room_number,
            'guest': guest
        }
        
        reservation_content.append(reservation_attrs)
        write_content_to_file(reservation_content, self.reservation_file)

    
    def cancel_a_reservation(self, reservation_id: int):
        """
        Given a reservation id, then remove it from the reservations data.
        """

        reservation_content = read_content_from_file(self.reservation_file)
        
        # Find the id for the reservation
        i = [i for i, reservation in enumerate(reservation_content)
             if reservation['id'] == reservation_id][0]

        del reservation_content[i]

        # Now, rewrite the reservation without the cancelled one.
        write_content_to_file(reservation_content, self.reservation_file)


class Customer():
    """
    This is the core customer object.
    """
    def __init__(self):
        self.customer_file = os.path.join(CATALOGUE_DIR, 'customers.json')

    def create_customer(self, customer_name: str, customer_email: str):
        """
        Create a new customer
        """

        # Get the current information on customers and add the new customer attributes
        customer_content = read_content_from_file(self.customer_file)

        customer_id = random.randint(1, 999)
        customer_attrs = {
            'id': customer_id,
            'name': customer_name,
            'email': customer_email,
        }

        customer_content.append(customer_attrs)
        write_content_to_file(customer_content, self.customer_file)

    def delete_customer(self, customer_id: int):
        """
        Given a customer id, then remove it from the catalogue.
        """
        customer_content = read_content_from_file(self.customer_file)

        # Get the index of the customer with the specified id
        i = [i for i, customer in enumerate(customer_content)
            if customer['id'] == customer_id][0]
        del customer_content[i]

        write_content_to_file(customer_content, self.customer_file)

    def display_customer_information(self, customer_id: int):
        """
        Given a customer id, then display its information.
        """

        customer_content = read_content_from_file(self.customer_file)
        customer = [customer for customer in customer_content
                    if customer['id'] == customer_id][0]

        print(customer)

    def modify_customer_information(self, customer_id: str, customer_attr: str, customer_value: [str, int]):
        """
        Given a customer id, then modify its attribute with the new customer value.
        """

        customer_content = read_content_from_file(self.customer_file)
        i, customer = [(i, customer) for i, customer in enumerate(customer_content)
                        if customer['id'] == customer_id][0]

        customer[customer_attr] = customer_value
        customer_content[i] = customer
        write_content_to_file(customer_content, self.customer_file)
        

if __name__ == '__main__':
    h = Hotel()
    # print(h.hotel_file)
    # print(h.create_hotel(2, 'Mexicanito', 10))
    # h.delete_hotel('s')
    # print(h.delete_hotel(2))
    # print(h.display_hotel_information(123))
    # print(h.modify_hotel_information(123, 'rooms', 100))
    # print(h.reserve_a_room(123, 11,))
    # print(h.cancel_a_reservation(957))

    #---
    c = Customer()
    # print(c.create_customer('Luffy', 'Luffy@pirates.mx'))
    # print(c.delete_customer(48))
    # print(c.display_customer_information(123))
    # print(c.modify_customer_information(123, 'email', 'roger@outlook.es'))

    
