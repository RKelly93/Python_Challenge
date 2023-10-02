import os
import csv

def extract_months_and_values_into_lists():

    budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

    # Open and read csv
    with open(budget_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)
        print(f"Financial Analysis")
        print("-------------------------")

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
    differences = []
    for i in range(1, len(values)):
        previous_value = values[i-1]
        current_value = values[i]
        difference = current_value - previous_value
        differences.append(difference)
    average_difference = sum(differences) / len(differences)
    print(f'Average Change: ${round(average_difference, 2)}')

def get_max_change(months, values):
    differences = []
    for i in range(1, len(values)):
        previous_value = values[i-1]
        current_value = values[i]
        difference = current_value - previous_value
        differences.append(difference)
    max_change = max(differences)
    for i in range(1, len(differences)):
        if differences[i] == max_change:
            max_month = months[i+1]
            print(f'Greatest Increase in Profits: {max_month} (${max_change})')

def get_min_change(months, values):
    differences = []
    for i in range(1, len(values)):
        previous_value = values[i-1]
        current_value = values[i]
        difference = current_value - previous_value
        differences.append(difference)
    min_change = min(differences)
    for i in range(1, len(differences)):
        if differences[i] == min_change:
            min_month = months[i+1]
            print(f'Greatest Decrease in Profits: {min_month} (${min_change})')

months, values = extract_months_and_values_into_lists()    
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