#Exercise 3: Write a program that reads a file and prints the letters
#in decreasing order of frequency. Your program should convert all the
#input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters
#a-z. Find text samples from several different languages and see how
#letter frequency varies between languages. Compare your results with
#the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

counts = 0                          # Initialize variables
dictionary_counts = dict()
relative_list = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    line=line.translate(str.maketrans('','',string.digits))
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.lower()
    # Removes numbers and punctuation then sets all letters to lower case
    words = line.split()
    for word in words:
        for letter in word:
            # Count each letter for relative frequencies
            counts += 1
            if letter not in dictionary_counts:
                dictionary_counts[letter] = 1
            else:
                dictionary_counts[letter] += 1

for key, val in list(dictionary_counts.items()):
    relative_list.append((val / counts, key))  # Computes the relative frequency
relative_list.sort(reverse=True)         # Sorts from highest rel freq
for fr, key in relative_list:
    print(key,fr)
