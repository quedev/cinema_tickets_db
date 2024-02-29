import random
import string


class User:

    def __init__(self, name):
        self.name = name

    def buy(self):
        pass


class Seat:

    db = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        pass

    def is_free(self):
        pass

    def occupy(self):
        pass


class Card:

    db = 'banking.db'

    def __init__(self, type_, number, cvc, holder):
        self._type = type_
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        pass


class Ticket:

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number
        self.id = "".join(random.choice(string.ascii_letters) for i in range(8))

    def to_pdf(self):
        pass