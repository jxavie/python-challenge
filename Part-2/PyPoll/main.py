# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:00:50 2019

@author: jnjav
"""

import os
import csv

# Use to sort through values in a list
from operator import itemgetter

# Initialize/declare variables, lists, and sets 
vote_total = 0
set_candidates = set()
vote_count = []
vote_percentage = []
print_result = []
 
# Define file path       
csvpath = os.path.join("Resources","election_data.csv")

# Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header
    next(csvreader)
    
    # Count total number of votes and create a unique set of candidates
    for row in csvreader:
        vote_total += 1
        set_candidates.add(row[2])
    
    # Create list of candidates from set
    list_candidates = list(set_candidates)
    
    # Determine index of last entry in list of candidates
    lastentry_candidates = len(list_candidates)
    
    # Assign an initial vote count value of zero for each candidate
    for candidate in range(0, lastentry_candidates):
        vote_count.append(0)
    
    # Reset csv file to the beginning (i.e., first entry below the header)
    csvfile.seek(1)
    
    # Calculate the vote count for each candidate
    for row in csvreader:
        for candidate in range(0, lastentry_candidates):
            if row[2] == list_candidates[candidate]:
                vote_count[candidate] += 1

# Calculate the percentage of the vote received by each candidate    
for candidate in range(0, lastentry_candidates):
    vote_percentage.append(format((vote_count[candidate]/vote_total)*100, '.3f'))

# Zip individual lists and sort candidates in descending order based on vote received
results = list(zip(list_candidates, vote_percentage, vote_count))
results = sorted(results, key = itemgetter(2), reverse = True)

# Unzip results back to individual lists
list_candidates, vote_percentage, vote_count = zip(*results)

# Determine winner based on max vote count
winner = list_candidates[vote_count.index(max(vote_count))]
  
# Print results  
print("\n------------------------------")
print(f"Total Votes: {vote_total}")
print("------------------------------")

for candidate in range(0, lastentry_candidates):
    print(f"{list_candidates[candidate]}: {vote_percentage[candidate]}% ({vote_count[candidate]})") 

print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

# Print results to txt file
with open('outputfile.txt', 'w') as txtfile:
    print("------------------------------", file = txtfile)
    print(f"Total Votes: {vote_total}", file = txtfile)
    print("------------------------------", file = txtfile)
    
    for candidate in range(0, lastentry_candidates):
        print(f"{list_candidates[candidate]}: {vote_percentage[candidate]}% ({vote_count[candidate]})", file = txtfile)
    
    print("------------------------------", file = txtfile)
    print(f"Winner: {winner}", file = txtfile)
    print("------------------------------", file = txtfile)