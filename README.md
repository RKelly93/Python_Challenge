# Python_Challenge

# For this challenge , I used the budget_data and election_results csv files to conduct a comprehensive analysis.

# PyBank

## Description

* For this challenge , I used the budget_data csv file to conduct a comprehensive analysis.

## Functions

* extract_months_and_values_into_lists()- Via the csvreader() function, I was able to loop through each row of data in the budget_data csv file.  I then appended the data into lists comprising of based on the column index in the csv file.

* get_total_months()- Using the len() function on the months list, I was able to provide a count of the months in the data set. 

* get_total()- After converting the value list to a list of integers, I used the sum() function to provide an end-of-list

* get_average_change()- Using a for-loop, I calculated all of the differences from month-to-month in the data set.  I then appended those differences into a differences[] list.  

* get_max_change()- Using the same for-loop to comprise the differences list, I then used the max() function to calculate the maximum difference in the list.  I then wrote another for-loop to locate the corresponding month from the months list, subtracting 1 from the index to get an exact match.

* get_min_change()- Same as get_max_change() but instead identifying minimum month and difference.

# PyPoll

## Description

* For this challenge, I used the election_results csv file to conduct a comprehensive analysis.

## Functions

* extract_data_into_lists()- Via the csvreader() function, I was able to loop through each row of data in the election_results csv file.  I then appended the data into lists comprising of based on the column index in the csv file.

* print_and_get_total_votes()- Using the len() function, I counted the length of the candidates[] list to determine how many votes were cast in total for the election.

* candidate_statistics()- First, I used the set() function on the candidates[] list in order to identify the 3 unique candidates in the list.  I then placed that set in a new list unique_candidates[].  Looping through the unique_candidates[] list, I then was able to count the votes for each candidate and calculate the percentage of the vote each of them won.

