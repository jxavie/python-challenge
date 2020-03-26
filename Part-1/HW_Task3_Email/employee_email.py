# -*- coding: UTF-8 -*-
"""Employee Email Script.

This module allows us to create an email address using employee data from
a csv file.

Example:
    $ python employee_email.py

"""
import os
import csv

# Define file path 
filepath = os.path.join("Resources", "employees.csv")

# Initialize/declare list
new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row["first_name"] + "." + row["last_name"] + "@example.com"
        employee_data = {
        "first_name":row["first_name"],
        "last_name":row["last_name"],
        "ssn":row["ssn"],
        "email":email
        }
        new_employee_data.append(dict(employee_data))

for row in new_employee_data:
    print(row)

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)

with open(csvpath, "w",newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ["first_name","last_name","ssn","email"])
    
    writer.writeheader()
    writer.writerows(new_employee_data)