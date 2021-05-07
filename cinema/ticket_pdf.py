from fpdf import FPDF
from webbrowser import open
from os import path
from filestack import Client
import random
from string import ascii_letters, digits


class Ticket:
    """
    Creates a pdf report with billing information
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_ticket_number(self):
        return "".join(
            random.SystemRandom().choice(ascii_letters + digits) for _ in range(10)
        )

    def generate(self, name, price, seat_number):
        """
        Generates a pdf given the bill and the two flatmates
        """

        def gen_cell(pdf_obj, name, value, family="Helvetica", style="", size=14):
            pdf_obj.set_font(family=family, style=style, size=size)
            pdf_obj.cell(w=100, h=25, txt=name, align="C", border=1)
            pdf_obj.cell(w=0, h=25, txt=value, align="C", ln=1, border=1)

        # instantiate the pdf and add a page
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # add icon
        pdf.image("cartoon_ticket.jpg", w=30, h=30)

        # add some text
        pdf.set_font(family="Times", size=24, style="B")

        # insert title
        pdf.cell(w=0, h=80, txt="Your Digital Ticket", align="C", ln=1, border=1)

        # insert information
        gen_cell(pdf, "Name:", name)
        gen_cell(pdf, "Ticket ID:", self.generate_ticket_number())
        gen_cell(pdf, "Price:", "${:.2f}".format(price))
        gen_cell(pdf, "Seat Number:", seat_number)

        # output the pdf file
        pdf.output(self.filename)

        # open the generated pdf
        open("file://" + path.realpath(self.filename))


class FileSharer:
    def __init__(self, filepath, api_key="AViVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        print(f"Here is a link to your ticket:\n\t➔  {new_filelink.url}")
