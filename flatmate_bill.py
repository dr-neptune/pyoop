from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill
    such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate who lives in the flat and
    pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        """
        Have a flatmate pay a bill
        """
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 2)


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
        pdf.image("house.png", w = 30, h = 30)

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

the_bill = Bill(amount = 120, period = "June 2021")
john = Flatmate(name = "John", days_in_house = 20)
mary = Flatmate(name = "Mary", days_in_house = 25)

# print(str(john.pays(bill = the_bill, flatmate2 = mary)))
# print(mary.pays(bill = the_bill, flatmate2 = john))

# print(the_bill.period)

pdf_report = PdfReport("Report1.pdf")

pdf_report.generate(flatmate1 = john,
                    flatmate2 = mary,
                    bill = the_bill)
