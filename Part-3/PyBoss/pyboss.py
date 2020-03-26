# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:27:39 2019

@author: jnjav
"""

import os
import csv

# Import dictionary of state abbreviations
from us_state_abbrev import us_state_abbrev

# Import module to convert string to datetime and vice versa
from datetime import datetime

# Initialize/declare lists
empID = []
name = []
firstname = []
lastname = []
dob = []
ssn = []
state = []
reformatted = []

# Define file path  
inputpath = os.path.join("employee_data.csv")

# Read csv file
with open(inputpath) as inputfile:
    inputreader = csv.reader(inputfile, delimiter=",")
    
    # Skip header
    next(inputreader)
    
    
    for emp in inputreader:
        
        #Create list of employee IDs
        empID.append(emp[0])
        
        # Split names into first and last name and assign to separate lists
        name_split = emp[1].split(" ")
        firstname.append(name_split[0])
        lastname.append(name_split[1])
        
        # Reformat dates by converting from string to datetime and from datetime back to string.  Assign dates to list
        date = emp[2]
        date = datetime.strptime(date, '%Y-%m-%d').date()
        dob.append(date.strftime('%m/%d/%Y'))
        
        # Replace portion of social security number with *'s and assign values to list
        ssn_split = emp[3].split("-")
        ssn.append(f"***-**-{ssn_split[2]}")
        
        # Replace state names with abbreviations and assign to list
        for key in us_state_abbrev:
            if key == emp[4]:
                state.append(us_state_abbrev[key])

# Zip individual lists
reformatted = zip(empID, firstname, lastname, dob, ssn, state)

# Define output file path 
outputpath = os.path.join("reformatted_employee_data.csv")

# Write reformatted data to a csv file
with open(outputpath, "w", newline = '') as outputfile:
    writer = csv.writer(outputfile)
    
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(reformatted)