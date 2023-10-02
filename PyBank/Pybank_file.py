import os
import csv

def extract_data():

    budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

    # Open and read csv
    with open(budget_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)
        print(f"Header: {csv_header}")

        months = []
        values = []

        # Read through each row of data after the header
        for row in csv_reader:
            month = row[0]
            months.append(month)
            value = row[1]
            value = int(value)
            values.append(value)

    return months, values

def get_total_months(months):
    total_months= len(months)
    print(f'Total Months: {total_months}')

def get_total(values):
    total = sum(values)
    print(f'Total: ${total}')

def get_average_change(values):
    print("Hello")

def get_max_change(months, values):
    print("Hello")

def get_min_change(months, values):
    print("Hello")

months, values = extract_data()    
get_total_months(months)
get_total(values)
get_average_change(values)
get_max_change(months, values)
get_min_change(months, values)








# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)