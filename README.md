## Running instructions

From the command line, run the following command, with `monthly_payslip.csv` in the same directory as `monthly_payslip.py`

    python3 monthly_payslip.py
    
### Pseudocode

Hopefully, this will give some insight into my thought process as I broke this task down.

1. Open csv file
2. parse the first row, using the comma as a delineator
    1. split up and enter into a list
    2. assign each slice of the list to a variable
    3. convert strings to integers, as necessary
        a. strip '%' from super rate
3. Do the following calculations:
    1. Define the pay period
    2. Divide yearly salary by 12 to determine monthly gross salary
    3. Determine the taxes owed for the month
    4. Subtract taxes from gross to determine net pay for the month
    5. Determine the super rate
4. Format the output
5. Move on to the next row

### TODO

1. Too much repeated code - turn that into a function
2. Write a Django front-end, so that .csv files can be uploaded
3. Learn how to write a Django front-end.