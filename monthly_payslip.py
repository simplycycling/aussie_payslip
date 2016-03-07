import csv


"""This script starts out by asking for a csv file to be entered. Included in the repo is a csv file named
"monthly_payslip.csv". It can use this csv, or any other csv file, so long as it's in the following format:

first name,last name,yearly gross pay,super,pay period

with the pay period being in the format of:

01 March – 31 March

or

March 01 - March 31

Pretty simple, I'm sure you get the picture."""
with open(input('Please enter the csv filename: ')) as csvfile:
    pay = csv.reader(csvfile)

    # Ranges = Lower end of tax bracket, higher end of tax bracket, super, deductable
    def monthly_payroll():
        ranges = [(0, 18200, 0, 0), (18201, 37000, .19, 0), (37001, 80000, .325, 3572),
                  (80001, 180000, .37, 17547), (180001, 2**1000, .45, 54547)]

        def check_taxes(value, value2, gross_income):
            for rng in ranges:
                minimum = rng[0]
                maximum = rng[1]
                rate = rng[2]
                base_tax = rng[3]
                if minimum < value < maximum:
                    if base_tax == 0:
                        income_tax = round(((value - minimum - 1) * rate) / 12)
                    else:
                        income_tax = round((base_tax + (value - minimum - 1) * rate) / 12)
                    net_income = gross_income - income_tax
                    _super = round(gross_income * value2)
                    return net_income, _super
        for item in pay:
            a = item[0]
            b = item[1]
            name = a + " " + b
            c = int(item[2])
            d = int(item[3].rstrip('%')) * 0.001
            e = item[4]
            gross_income = round(c / 12)
            net_income, _super = check_taxes(c, d, gross_income)
            if net_income:
                print(name + "," + e + "," + str(gross_income) + "," + str(net_income) + "," + str(_super))

    if __name__ == '__main__':
        monthly_payroll()
