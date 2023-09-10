#!/usr/bin/python

# read file from the command line
import sys
with open(sys.argv[1], 'r') as f:
    filename = f.read()

# create a list of strings from filename
lines = filename.split('\n')

def sortVowels(lines):
    sortVow = []   # create list
    for word in lines:  
        sortVow.append((word, getVowels(word)))   
    sortVow.sort(key=lambda x: (x[1], x[0]))   # sort the list 
    return [word[0] for word in sortVow]   

# function to the get the vowels from each word
def getVowels(word):
    vowels = "aeiou"
    return "".join([char for char in word if char in vowels])  

 # sort the list of strings
sorted = sortVowels(lines) 

# print list
for word in sorted:   
        print(word)



