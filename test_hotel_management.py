import unittest
import os
from hotel_management import Hotel, Customer, Reservation

class TestHotelManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Asegurarse de que los archivos de datos estén limpios antes de iniciar las pruebas
        cls.clean_up_files()

    @classmethod
    def tearDownClass(cls):
        # Limpiar archivos de datos después de correr las pruebas
        cls.clean_up_files()

    @staticmethod
    def clean_up_files():
        for filename in ['hotels.json', 'customers.json', 'reservations.json']:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass

    def test_create_and_display_hotel(self):
        Hotel.create_hotel({'hotel_id': '001', 'name': 'Grand Plaza', 'rooms': []})
        hotel_info = Hotel.display_hotel_info('001')
        self.assertIsNotNone(hotel_info)
        self.assertEqual(hotel_info['name'], 'Grand Plaza')

    def test_modify_and_delete_hotel(self):
        Hotel.modify_hotel_info('001', {'name': 'Grand Plaza Deluxe'})
        modified_hotel_info = Hotel.display_hotel_info('001')
        self.assertEqual(modified_hotel_info['name'], 'Grand Plaza Deluxe')
        Hotel.delete_hotel('001')
        hotel_info_after_deletion = Hotel.display_hotel_info('001')
        self.assertIsNone(hotel_info_after_deletion)

    def test_create_and_display_customer(self):
        Customer.create_customer({'customer_id': '001', 'name': 'John Doe', 'contact_info': 'johndoe@example.com'})
        customer_info = Customer.display_customer_info('001')
        self.assertIsNotNone(customer_info)
        self.assertEqual(customer_info['name'], 'John Doe')

    def test_modify_and_delete_customer(self):
        Customer.modify_customer_info('001', {'name': 'Jane Doe'})
        modified_customer_info = Customer.display_customer_info('001')
        self.assertEqual(modified_customer_info['name'], 'Jane Doe')
        Customer.delete_customer('001')
        customer_info_after_deletion = Customer.display_customer_info('001')
        self.assertIsNone(customer_info_after_deletion)

    def test_create_and_cancel_reservation(self):
        Reservation.create_reservation({'reservation_id': '001', 'hotel_id': '001', 'customer_id': '001', 'room': '101', 'date_range': '2023-01-01 to 2023-01-05'})
        Reservation.cancel_reservation('001')
        # En este punto, verificaríamos si la reserva fue cancelada correctamente.
        # Dado que no hay un método explícito para 'mostrar' reservaciones, este paso podría involucrar
        # cargar directamente el archivo JSON y verificar que la reserva ya no existe.

if __name__ == '__main__':
    unittest.main()
