# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:47:36 2019

@author: jnjav
"""

import os

# Import module to allow data splitting using multiple delimiters
import re

# Define file path  
inputpath = os.path.join("raw_data","test.txt")

# Initialize/declare variables and lists
words_list =[]
letters = 0

# Read txt file
with open(inputpath, "rt") as inputfile:
    passage = inputfile.read()
    
    # Split read passage and assign to list
    words_raw = passage.split()
    
    # Calcuate approximate word count of passage
    word_count = len(words_raw)

    # Remove trailing punctuation from words and assign to list
    for word in words_raw:
        words_list.append(word.split(",")[0].split(".")[0])
    
    # Split read package using regular expression operation to determine approximate sentence count
    sentences = re.split(r"\.\s", passage)
    sentence_count = len(sentences)
    
    # Split read package using regular expression operation to remove all punctuation including possessive apostrophes and hypens
    letters_list = re.split(r"\. |, | |-|\'|\.", passage)
    
    # Calculate total letter count of passage
    for entry in letters_list:
        letters += len(entry)
    
    # Calculate average length of words used
    letters_count = format((letters / word_count), '.1f')
    
    # Calculate average length of sentences in the passage
    sentence_length = format((word_count / sentence_count), '.1f')

# Print results
print("\nParagraph Analysis")
print("-----------------------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {letters_count}")
print(f"Average Sentence Length: {sentence_length}")