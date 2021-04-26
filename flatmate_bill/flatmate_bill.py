from re import sub
from flat import Bill, Flatmate
from reports import PdfReport

# CLI prompts
amount = float(sub("[^0-9+]", "", input("Hey user, enter the bill amount:\n")))
period = input("What is the bill period? E.g. April 2021\n")
name1 = input("What is your name?\n")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period?\n"))
name2 = input("What is your flatmate's name?\n")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period?\n"))

# instantiate the objects
the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

# print results
print(f"{flatmate1.name} pays:\t", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays:\t", flatmate2.pays(the_bill, flatmate1))

# generate pdf report
pdf_report = PdfReport(f"{the_bill.period}.pdf")

# open the pdf report
pdf_report.generate(flatmate1, flatmate2, the_bill)
