from fpdf import FPDF
from webbrowser import open
from os import path
from filestack import Client

class PdfReport:
    """
    Creates a pdf report with billing information
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """
        Generates a pdf given the bill and the two flatmates
        """

        def gen_cell(pdf_obj, name, value, family = "Helvetica", style = "B", size = 24):
            pdf_obj.set_font(family = family, style = style, size = size)
            pdf_obj.cell(w = 100, h = 25,
                         txt = name, align = "C")
            pdf_obj.cell(w = 150, h = 25,
                     txt = value, align = "C", ln = 1)

        # instantiate the pdf and add a page
        pdf = FPDF(orientation = "P",
                   unit = "pt",
                   format = "A4")
        pdf.add_page()

        ## add icon
        pdf.image("files/house.png", w = 30, h = 30)

        # add some text
        pdf.set_font(family = "Times", size = 24, style = "B")

        # insert title
        pdf.cell(w = 0, h = 80,
                 txt = "Flatmate's Bill",
                 align = "C", ln = 1)

        # insert period label and value
        gen_cell(pdf, "Period:", bill.period, size = 14)

        # insert name and due amount of the flatmates
        gen_cell(pdf, flatmate1.name, "$" + str(flatmate1.pays(bill, flatmate2)), size = 14, style = "")
        gen_cell(pdf, flatmate2.name, "$" + str(flatmate2.pays(bill, flatmate1)), size = 14, style = "")

        # output the pdf file
        pdf.output(self.filename)

        # open the generated pdf
        open("file://" + path.realpath(self.filename))

class FileSharer:
    def __init__(self, filepath, api_key = "AViVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath = self.filepath)
        return new_filelink.url
