"""Exercise 3: Encapsulate this code in a function named count, and generalize it
so that it accepts the string and the letter as arguments."""
def count(word,letter):
    count = 0
    for letters in word:
        if letters == letter:
             count = count + 1
    print(count)
count('gurubulu','u')
