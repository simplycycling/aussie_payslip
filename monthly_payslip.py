import csv

def monthly_payroll():
    ranges = [(0, 18200, 0), (182001, 37000, .19), (37001, 80000, .325), (80001, 180000, .37), (180001,)]


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
        if c <= 18200:
            incomeTax = 0
        elif 18201 <= c <= 37000:
            incomeTax = round(((c - 18200) * 0.19) / 12)
            netIncome = grossIncome - incomeTax
            _super = round(grossIncome * d)
            print(name + "," + e + "," + str(grossIncome) + "," + str(netIncome) + "," + str(_super))
        elif 37001 <= c <= 80000:
            incomeTax = round((3572 + (c - 37000) * 0.325) / 12)
            netIncome = grossIncome - incomeTax
            _super = round(grossIncome * d)
            print(name + "," + e + "," + str(grossIncome) + "," + str(netIncome) + "," + str(_super))
        elif 80001 <= c <= 180000:
            incomeTax = round((17547 + (c - 80000) * 0.37) / 12)
            netIncome = grossIncome - incomeTax
            _super = round(grossIncome * d)
            print(name + "," + e + "," + str(grossIncome) + "," + str(netIncome) + "," + str(_super))
        elif c >= 180001:
            incomeTax = round((54547 + (c - 180000) * 0.45) / 12)
            netIncome = grossIncome - incomeTax
            _super = round(grossIncome * d)
            print(name + "," + e + "," + str(grossIncome) + "," + str(netIncome) + "," + str(_super))
