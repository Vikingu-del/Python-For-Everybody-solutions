#Exercise 1: Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the number of
#messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits.

import string
filehandle=input('Enter file: ')
if len(filehandle)<1: filehandle='mbox-short.txt'
fh=open(filehandle)
mails=list()
counts=dict()
for line in fh:
    if line.startswith('From'):
        line=line.split()
        if line[1] not in counts:
            counts[line[1]]=1
        else: counts[line[1]]=counts[line[1]]+1
for mail, numb in counts.items():
    mails.append((numb, mail))
mails.sort(reverse=True)
print (mails)
print('The person with the most commits is:',mails[0])
