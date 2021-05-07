from db_ops import Card, Ticket

# read in name
# preferred seat number
# card type
# card number
# card cvc
# card holder name

# get input information without any authentication whatsoever
c_name = input("What is your name?\n\t➔  ")
pref_seat = input("What is your preferred seat?\n\t➔  ")
card_type = input("What is your card type?\n\t➔  ")
card_num = input("What is your card number?\n\t➔  ")
card_cvc = input("What is your card's cvc?\n\t➔  ")
card_hname = input("What is the cardholder's name?\n\t➔  ")

# instantiate objects
card = Card(card_hname)
ticket = Ticket(pref_seat)

# check that seat is available
seat_available = ticket.get_seat_status()

# check that cc info is correct
correct_info = card.check_cc_info_correct(
    ch_name=card_hname, card_type=card_type, card_num=card_num, card_cvc=card_cvc
)

# if correct, charge the account for the ticket
if correct_info and seat_available:
    print(f"The price of the seat is ${ticket.get_seat_cost()}.")
    choice = input("Do you still wish to purchase it? (y / n)\n\t➔  ")
    if choice == "y":
        card.buy_seat(ticket.get_seat_cost())
        ticket.change_seat_status("1")
        print(f"Fantastic! You have purchased a ticket for seat {pref_seat}")
    else:
        print("Ah well, perhaps another seat")
else:
    if correct_info:
        print(
            "Unfortunately, that seat is not available at this time. Please try again."
        )
    else:
        print("Unfortunately, we could not validate your card. Please try again.")
