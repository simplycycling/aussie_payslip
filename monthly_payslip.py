import csv


with open('monthly_payslip.csv') as csvfile:
    pay = csv.reader(csvfile)


    def monthly_payroll():
        ranges = [(0, 18200, 0, 0), (182001, 37000, .19, 0), (37001, 80000, .325, 3572),
                  (80001, 180000, .37, 17547), (180001, 1000000, .45, 54547)]

        def check_taxes(value, value2, gross_income):
            for rng in ranges:
                minimum = rng[0]
                maximum = rng[1]
                rate = rng[2]
                base_tax = rng[3]
                if value in range(minimum, maximum):
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
