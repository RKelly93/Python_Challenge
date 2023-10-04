import os
import csv
   
def extract_data_into_lists():

    election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

    # Open and read csv
    with open(election_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_file)
        print(f"Election Results")
        print("-------------------------")
        
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

def print_and_get_total_votes(candidates):
    total_votes = len(candidates)
    print(f'Total Votes: {total_votes}')
    print("----------------------------")

    return total_votes



def candidate_statistics(candidates, unique_candidates):
    count_total = []
    for candidate in unique_candidates:
        count = candidates.count(candidate)
        percent_vote = round((count/total_votes)*100,3)
        print(f'{candidate}: {percent_vote}% ({count})')
    print("----------------------")
    

#def find_winner(candidates, unique_candidates):
   # for candidate in unique_candidates:
    #    count = candidates.count(candidate)
    #    if count ==

candidates = extract_data_into_lists()
total_votes = print_and_get_total_votes(candidates)
unique_candidates = list(set(candidates))
candidate_statistics(candidates, unique_candidates)

with open('election_results.txt', 'w') as text:
    
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------