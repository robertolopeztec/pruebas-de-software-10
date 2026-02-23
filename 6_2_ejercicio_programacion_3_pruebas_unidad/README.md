## Diseños de Prueba

Estas pruebas estan dentro de `test/unit/app/scripts/reserv_system_test.py`

1. `test_create_hotel_raises_typeerror_if_not_expected_schema()`: Valida si las variables utilizadas para crear un nuevo hotel coinciden con el schema predefinido.
2. `test_delete_hotel_raises_typeeror_if_not_int()`: Valida si se genera un error si el tipo del `hotel_id` no es un `int`.
3. `test_modify_hotel_information_raises_valueerror_if_not_in_valid_hotel_attrs()`: Valida si se genera un error si el atributo a modificr no es uno dentro del schema.
4. `test_reserve_a_room_hotel_doesnt_exists()`: Valida si se genera un error en caso de que no exista un hotel, basado en su hotel_id.
5. `test_cancel_a_reservation_raises_indexerror_if_reservation_id_doesnt_exists()`: Valida si se gneera un error de tipo IndexError si no existe el id de reservacion.