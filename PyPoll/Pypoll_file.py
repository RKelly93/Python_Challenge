# Import Dependencies
import os
import csv

# Extract data in the budget_data.csv into lists.
def extract_data_into_lists():

    # Locate and extract election_data.csv.
    election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

    # Open and read csv
    with open(election_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_file)
        # Test
        print(f"Election Results")
        print("-------------------------")
        
        # Set lists to be filled.
        ballots = []
        candidates = []
        unique_name = []

        # Read through each row of data after the header
        for row in csv_reader:
            ballot_num = row[0]
            ballots.append(ballot_num)
            candidate_name = row[2]
            candidates.append(candidate_name)
        
    return candidates

# Set function to count all of the ballots submitted in the election
def print_and_get_total_votes(candidates):
    total_votes = len(candidates)
    print(f'Total Votes: {total_votes}')
    print("----------------------------")

    return total_votes


# Set function to calculate how many votes each candidate received. 
def candidate_statistics(candidates, unique_candidates):
    # Collect all votes submitted.
    count_total = []
    # Set list to collect the percentage of the vote each candidate received.
    percent_vote_list = []
    # Loop through the three candidates in the unique_candidates list.
    for candidate in unique_candidates:
        # count the number of votes submitted for each candidate in the
        # candidates list.
        count = candidates.count(candidate)
        # Calculate the percentage of the vote each candidate received rounding
        # to 3 decimal points.
        percent_vote = round((count/total_votes)*100,3)
        # Enter percent_vote into the percent_vote_list.
        percent_vote_list.append(percent_vote)
        # Test
        print(f'{candidate}: {percent_vote}% ({count})')
    print("----------------------")

# Call all functions that were defined
candidates = extract_data_into_lists()
total_votes = print_and_get_total_votes(candidates)
unique_candidates = list(set(candidates))
candidate_statistics(candidates, unique_candidates)

# Set output path for with the election_results text file is to be placed.
output_path = os.path.join("..", "output", "election_results.txt")

# Define new text file to be written.
with open('election_results.txt', 'w') as text:
    
    # Write rows of text file.
    text.write("Election Results\n")
    text.write("--------------------------------\n")
    text.write(f'Total Votes: {total_votes}\n')
    text.write("--------------------------------\n")
        