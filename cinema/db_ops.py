import sqlite3


class DBAccessor:
    def __init__(self, db_name):
        self.db_name = db_name
        # initialize the connection
        self.con = sqlite3.connect(self.db_name)


class Card(DBAccessor):
    def __init__(self, card_holder, db_name):
        super().__init__(db_name)
        self.card_holder = card_holder

    def get_cc_info(self):
        cursor = self.con.cursor()
        cursor.execute(
            f"""
            SELECT type, number, cvc, holder FROM "Card" WHERE holder = "{self.card_holder}"
            """
        )
        return cursor.fetchall()

    def buy_seat(self, seat_price):
        self.con.execute(
            f"""
            UPDATE "Card" SET balance = balance - {seat_price} WHERE holder = "{self.card_holder}"
            """
        )
        self.con.commit()
        self.con.close()


# card = Card(card_holder="Marry Smith", db_name="banking.db")
# print(card.con)
# print(card.get_cc_info())
# print(card.buy_seat(100))


class Ticket(DBAccessor):
    def __init__(self, seat_id, db_name):
        super().__init__(db_name)
        self.seat_id = seat_id

    def get_seat_status(self):
        cursor = self.con.cursor()
        cursor.execute(
            f"""
            SELECT taken FROM "Seat" WHERE seat_id = "{self.seat_id}"
            """
        )

        # the [0][0] accesses the result as a single character
        seat_status = int(cursor.fetchall()[0][0])

        # if seat open, return True, ow False
        return True if seat_status == 0 else False


# new_seat = Ticket("A3", "cinema.db")
# print(new_seat)
# print(new_seat.get_seat_status())
