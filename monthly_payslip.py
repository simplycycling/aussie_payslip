import csv


with open('monthly_payslip.csv') as csvfile:
    pay = csv.reader(csvfile)
    for item in pay:
        a = item[0]
        b = item[1]
        name = a + " " + b
        c = int(item[2])
        d = int(item[3].rstrip('%')) * 0.001
        e = item[4]
        grossIncome = round(c / 12)
        incomeTax = round((3572 + (c - 37000) * 0.325) / 12)
        netIncome = grossIncome - incomeTax
        _super = round(grossIncome * d)
        print(name + "," + e + "," + str(grossIncome) + "," + str(netIncome) + "," + str(_super))
