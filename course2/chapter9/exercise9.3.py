#Exercise 3: Write a program to read through a mail log, build a histogram
#using a dictionary to count how many messages have come from
#each email address, and print the dictionary.

filehandle=input('Enter file: ')
cm=dict()
lm=list()
try:
    fh=open(filehandle)
except:
    print('File doesnt exist!')
    exit()
for line in fh:
    line=line.split()
    if len(line) < 3  or line[0] != 'From' :
        continue
    lm.append(line[1])
for m in lm:
    cm[m]=cm.get(m,0)+1

for keys in cm:
    print (keys,cm[keys])
print (cm)
