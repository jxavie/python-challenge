# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:30:40 2019

@author: jnjav
"""

import os
import csv

# Initialize/declare variables and lists
totalrevenue = 0
months = []
revenue = []
change = []

# Define file path 
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header
    next(csvreader)
    
    # Create list of months and revenue; calculate total revenue
    for row in csvreader:
        months.append(row[0])
        totalrevenue += int(row[1])
        revenue.append(float(row[1]))
    
    # Determine index of last entry of revenue list
    lastrow = len(revenue)
    
    # Calculate month-to-month change in revenue and assign values to change list
    for i in range(1,lastrow):
        change.append(revenue[i]-revenue[i-1])

# Calculate length of period (i.e., number of months represented by the data)       
period = len(months)

# Calculate the average month-to-month revenue change
ave_change = round(sum(change) / len(change), 2)

# Calculate the maximum month-to-month revenue change
max_change = int(max(change))

# Calculate the minimum month-to-month revenue change
min_change = int(min(change))

# Determine the location of the maximum month-to-month revenue change within the revenue change list
max_loc = change.index(max(change)) + 1 

# Determine the location of the minimum month-to-month revenue change within the revenue change list
min_loc = change.index(min(change)) + 1

# Determine the date corresponding to the maximum month-to-month revenue change
max_date = months[max_loc]

# Determine the date corresponding to the minimum month-to-month revenue change
min_date = months[min_loc]
 
# Print results    
line1 = "Financial Analysis"
line2 = "------------------------------"
line3 = f"Total Months: {period}"
line4 = f"Total: ${totalrevenue}"
line5 = f"Average Change: ${ave_change}"
line6 = f"Greatest Increase in Profits: {max_date} (${max_change})"
line7 = f"Greatest Decrease in Profits: {min_date} (${min_change})"
  
print(f"\n{line1}")
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

# Print results to txt file
with open('outputfile.txt', 'w') as txtfile:
    print(line1, file = txtfile)
    print(line2, file = txtfile)
    print(line3, file = txtfile)
    print(line4, file = txtfile)
    print(line5, file = txtfile)
    print(line6, file = txtfile)
    print(line7, file = txtfile)