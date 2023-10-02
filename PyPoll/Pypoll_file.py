import os
import csv

    budget_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

    # Open and read csv
    with open(budget_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)
        