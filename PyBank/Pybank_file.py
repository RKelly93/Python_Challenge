# Import Dependencies
import os
import csv

# Extract data in the budget_data.csv into lists.
def extract_months_and_values_into_lists():

    # Locate and extract budget_data.csv.
    budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

    # Open and read csv
    with open(budget_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)
        print(f"Financial Analysis")
        print("-------------------------")

        # Assign list to months and values to capture respective values in the 
        # budget_data.csv
        months = []
        values = []

        # Read through each row of data after the header and fill lists
        for row in csv_reader:
            month = row[0]
            months.append(month)
            value = row[1]
            value = int(value)
            values.append(value)

    return months, values

# Set function to calculate the number of months
# for which data has been collected.
def get_total_months(months):
    total_months= len(months)
    print(f'Total Months: {total_months}')

    return total_months

# Set function in order to calculate sum of all integers in the dataset.
def get_total(values):
    total = sum(values)
    print(f'Total: ${total}')
    
    return total

# Set function to calculate the average change from month-to-month
# in the dataset.
def get_average_change(values):
    # Create a list to store differences calculated from month-to-month
    # in the values list.
    differences = []
    for i in range(1, len(values)):
        previous_value = values[i-1]
        current_value = values[i]
        #Calculate difference between each value in the values list.
        difference = current_value - previous_value
        # append all differences calculated into differencces[].
        differences.append(difference)
    # Calculate the average difference in the values list.
    average_difference = round((sum(differences) / len(differences)),2)
    # Test
    print(f'Average Change: ${average_difference}')

    return average_difference

# Set function to calculate the highest positive change from month-to-month
# in the values list.
def get_max_change(months, values):
    # Create a list to store differences calculated from month-to-month
    # in the values list.
    differences = []
    # Loop created in values list to calculate the differences in the values
    # list from one value to the next that are stored in the values list.
    for i in range(1, len(values)):
        previous_value = values[i-1]
        current_value = values[i]
        difference = current_value - previous_value
        differences.append(difference)
    # Find the maximum value in the differences list and assign it to max_change.
    max_change = max(differences)
    for i in range(1, len(differences)):
        if differences[i] == max_change:
            # Find the month correlated with the maximum value in the 
            # differences list.
            max_month = months[i+1]
            # Test
            print(f'Greatest Increase in Profits: {max_month} (${max_change})')

    return max_month, max_change

# Set function to locate the minimum change from month-to-month and the 
# corresponding month.
def get_min_change(months, values):
    differences = []
    # Same for-loop to populate differences list.
    for i in range(1, len(values)):
        previous_value = values[i-1]
        current_value = values[i]
        difference = current_value - previous_value
        differences.append(difference)
    # Find the minimum value in the differences list and assign it to min_change.
    min_change = min(differences)
    # same for-loop used to find the maximum month will be used here to find the 
    # month correlated to the minimum value in the differences list.
    for i in range(1, len(differences)):
        if differences[i] == min_change:
            min_month = months[i+1]
            # Test
            print(f'Greatest Decrease in Profits: {min_month} (${min_change})')
    return min_month, min_change

# Call functions
months, values = extract_months_and_values_into_lists()    
total_months = get_total_months(months)
total = get_total(values)
average_difference = get_average_change(values)
get_max_change(months, values,)
get_min_change(months, values,)

# Set output path for which the budget results text is to be placed.
output_path = os.path.join("..", "output", "budget_results.txt")

# Define new text file to be written.
with open('budget_results.txt', 'w') as text:

    # Write rows of text file
    text.write("Financial Analysis\n")
    text.write("--------------------------------\n")
    text.write(f'Total Months: {total_months}\n')
    text.write(f'Total: ${total}\n')
    text.write(f'Average Change: ${average_difference}\n')
                # Attempt at rest of challenge 
    # for i in range(1, len()):
    #     if differences[i] == max_change:
    #         max_month = months[i+1]
    #         text.write(f'Greatest Increase in Profits: {max_month} (${max_change})')
    # for i in range(1, len(differences)):
    #     if differences[i] == min_change:
    #         min_month = months[i+1]
    #         text.write(f'Greatest Decrease in Profits: {min_month} (${min_change})')