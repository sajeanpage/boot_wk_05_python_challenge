'''
PyBank

In this Challenge, I was tasked with creating a Python script to analyze the financial records. 
I was given a financial dataset called budget_data.csv composed of two columns: "Date" and "Profit/Losses".

I was asked to analyze the records to calculate:
    The total number of months included in the dataset
    The net total amount of "Profit/Losses" over the entire period
    The changes in "Profit/Losses" over the entire period, and then the average of those changes
    The greatest increase in profits (date and amount) over the entire period
    The greatest decrease in profits (date and amount) over the entire period
'''
# module imports
import os
import csv
import sys

# variables 
total_months = 0
net_total = 0
pl_change_tot = 0.00

# initialaizations
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') # CSV reader 
    print(csvreader)

    csv_header = next(csvreader) # skip header row
    print(f"CSV Header: {csv_header}\n")

    # main loop
    for row in csvreader:
        pl = float(row[1])
        net_total = net_total + pl
        total_months = total_months + 1

        # no change month 1
        if total_months > 1: 
            pl_change = pl - pl_last
            pl_change_tot = pl_change_tot + pl_change

            # greatest incr and decr on month 2
            if total_months == 2:
                great_inc = pl_change
                great_inc_month = row[0]
                great_dec = pl_change
                great_dec_month = row[0]
            else:
                if pl_change > 0 and pl_change > great_inc:
                    great_inc = pl_change
                    great_inc_month = row[0]

                if pl_change < 0 and pl_change < great_dec:
                    great_dec = pl_change
                    great_dec_month = row[0]

        pl_last = pl

txtpath = os.path.join('Analysis', 'Analysis.txt')

# reference to the original standard output
original_stdout = sys.stdout 

# print to file
with open(txtpath, "w") as txtfile:
    sys.stdout = txtfile # Change the standard output to the file we created.
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")       
    print(f"Total: ${int(net_total)}")       
    print(f"Average Change: ${pl_change_tot / (total_months - 1):,.2f}")       
    print(f"Greatest Increase in Profits: {great_inc_month} (${int(great_inc)})")  
    print(f"Greatest Decrease in Profits: {great_dec_month} (${int(great_dec)})")
    sys.stdout = original_stdout 

# print to terminal
with open(txtpath, "r") as txtfile:
    txtfilecontent = txtfile.read()
    print(txtfilecontent)
