import sqlite3


class DBAccessor:
    def __init__(self, db_name):
        self.db_name = db_name
        # initialize the connection
        self.con = sqlite3.connect(self.db_name)


class Card(DBAccessor):
    """
    Represents a customer's credit card information
    """

    def __init__(self, card_holder, db_name="banking.db"):
        super().__init__(db_name)
        self.card_holder = card_holder

    def get_cc_info(self):
        cursor = self.con.cursor()
        cursor.execute(
            f"""
            SELECT type, number, cvc, holder FROM "Card" WHERE holder = "{self.card_holder}"
            """
        )
        results = cursor.fetchall()[0]
        return {
            "type": results[0],
            "num": results[1],
            "cvc": results[2],
            "name": results[3],
        }

    def buy_seat(self, seat_price):
        self.con.execute(
            f"""
            UPDATE "Card" SET balance = balance - {seat_price} WHERE holder = "{self.card_holder}"
            """
        )
        self.con.commit()
        self.con.close()

    def check_cc_info_correct(self, ch_name, card_type, card_num, card_cvc):
        # get cardholder info by name
        cc_info = self.get_cc_info()
        return all(
            [
                cc_info["name"] == ch_name,
                cc_info["type"] == card_type,
                cc_info["num"] == card_num,
                cc_info["cvc"] == card_cvc,
            ]
        )


# card = Card(card_holder="Marry Smith", db_name="banking.db")
# print(card.get_cc_info())
# print(card.check_cc_info_correct("Marry Smith", "Master Card", "23456789", "234"))
# print(card.buy_seat(100))


class Seat(DBAccessor):
    """
    Represents a ticket for a seat
    """

    def __init__(self, seat_id, db_name="cinema.db"):
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

    def get_seat_cost(self):
        cursor = self.con.cursor()
        cursor.execute(
            f"""
            SELECT price FROM "Seat" WHERE seat_id = "{self.seat_id}"
            """
        )

        return float(cursor.fetchall()[0][0])

    def change_seat_status(self, new_status):
        self.con.execute(
            f"""
            UPDATE "Seat" SET taken = {new_status} WHERE seat_id = "{self.seat_id}"
            """
        )
        self.con.commit()
        self.con.close()


# new_seat = Seat("A3", "cinema.db")
# print(new_seat)
# print(new_seat.get_seat_status())
# print(new_seat.generate_ticket_number())
