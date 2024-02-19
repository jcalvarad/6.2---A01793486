import json

# Utilidad para manejo de archivos
def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(filename):
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Clase Hotel
class Hotel:
    def __init__(self, hotel_id, name, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms  # Lista de diccionarios, cada uno representando una habitación

    @staticmethod
    def create_hotel(hotel_data):
        hotels = load_data('hotels.json')
        hotels.append(hotel_data)
        save_data('hotels.json', hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        hotels = load_data('hotels.json')
        hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
        save_data('hotels.json', hotels)

    @staticmethod
    def modify_hotel_info(hotel_id, updated_data):
        hotels = load_data('hotels.json')
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                hotel.update(updated_data)
                break
        save_data('hotels.json', hotels)

    @staticmethod
    def display_hotel_info(hotel_id):
        hotels = load_data('hotels.json')
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

# Clase Customer
class Customer:
    def __init__(self, customer_id, name, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.contact_info = contact_info

    @staticmethod
    def create_customer(customer_data):
        customers = load_data('customers.json')
        customers.append(customer_data)
        save_data('customers.json', customers)

    @staticmethod
    def delete_customer(customer_id):
        customers = load_data('customers.json')
        customers = [customer for customer in customers if customer['customer_id'] != customer_id]
        save_data('customers.json', customers)

    @staticmethod
    def modify_customer_info(customer_id, updated_data):
        customers = load_data('customers.json')
        for customer in customers:
            if customer['customer_id'] == customer_id:
                customer.update(updated_data)
                break
        save_data('customers.json', customers)

    @staticmethod
    def display_customer_info(customer_id):
        customers = load_data('customers.json')
        for customer in customers:
            if customer['customer_id'] == customer_id:
                return customer
        return None

# Clase Reservation
class Reservation:
    def __init__(self, reservation_id, hotel_id, customer_id, room, date_range):
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id
        self.room = room
        self.date_range = date_range

    @staticmethod
    def create_reservation(reservation_data):
        reservations = load_data('reservations.json')
        reservations.append(reservation_data)
        save_data('reservations.json', reservations)

    @staticmethod
    def cancel_reservation(reservation_id):
        reservations = load_data('reservations.json')
        reservations = [reservation for reservation in reservations if reservation['reservation_id'] != reservation_id]
        save_data('reservations.json', reservations)
