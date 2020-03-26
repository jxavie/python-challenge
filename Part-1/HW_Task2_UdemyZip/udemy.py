import os
import csv

# Define file path
udemy_csv = os.path.join("web_starter.csv")

# Initialize/declare lists
title = []
price = []
subscribers = []
reviews = []
length = []
percent_review = []

# Read csv file
with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        # Calculate percent of subscibers who left reviews
        percent = (int(row[6]) / int(row[5])) * 100
        
        # Remove time designation (i.e., hours and minutes) from course length
        length_split = row[9].split(" ")
        
        # Create lists of course titles, price, number of subscribers, number of reviews, and percent of subcribers who left reviews
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        percent_review.append(percent)
        
        # Convert course length to hours and create list
        if length_split[1] == "mins":
            length.append(str(round(int(length_split[0])/60,2)))
        else:
            length.append(length_split[0])

# Zip lists
zipped_data = zip(title, price, subscribers, reviews, percent_review, length) 

# Define output file path
output_file = os.path.join("web_modified.csv")

# Write results to csv file
with open(output_file, "w", newline='') as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Title","Price","Subscribers","Reviews","% of Subscribers who Left Reviews","Length (Hrs)"])
        writer.writerows(zipped_data)