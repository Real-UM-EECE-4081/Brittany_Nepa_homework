#Write a program that counts the frequency of words in a file
from collections import Counter

def num_words(fname):
    with open(fname) as f:
        return Counter(f.read().split())

print("The number of words found in file: ", num_words("test1.txt"))