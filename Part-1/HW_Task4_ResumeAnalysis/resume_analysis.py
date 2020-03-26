# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = os.path.join(".", "Resources", 'resume.md')

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)

resume = resume - punctuation
print(f"\n{resume}")

# Calculate the Required Skills Match using Set Intersection
print("\nREQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("\nDESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)

# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(f"\n{word_count}")

# Using collections.Counter
word_counter = Counter(word_list)
print(f"\n{word_counter}")

# Comparing both word count solutions
print(f"\n{word_count == word_counter}")


# Top 10 Words
# ==========================

# Initialize list for words in resume
word_raw = []

# Remove trailing punctuation and add to list
for word in word_list:
    word_raw.append(word.split(",")[0].split(".")[0])

# Convert punctuation set into a list
punctuation = list(punctuation)

# Remove punctuations
for entry in punctuation:
    for row in word_raw:
        if entry == row:
            word_raw.remove(row)  

# Create list with stop words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]

# Remove stop words
for entry in stop_words:
    for row in word_raw:
        if entry == row:
            word_raw.remove(row)

# Initialize dictionary that will be used to count the number of times a word appears in resume
word_counter = dict.fromkeys (word_raw, 0)

for word in word_raw:
    word_counter[word] += 1

# Sort words by count and print the top 10 words
sorted_words = sorted(word_counter, key = word_counter.get, reverse = True)


print("\nTop 10 Words")
print("=============")
for word in sorted_words[:10]:
    print(f"Word: {word:20} Count: {word_counter[word]}")