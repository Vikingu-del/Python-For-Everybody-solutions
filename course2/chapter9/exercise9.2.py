#Exercise 2: Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter)

filehandle=input('Enter file: ')
days=list()
count=dict()
try:
    fh=open(filehandle)
except:
    print('File doesnt exist!')
    exit()
for line in fh:
    line = line.split()
    if len(line) < 3 or line[0]!='From': continue
    days.append(line[2])
for day in days:
    if day not in count:
        count[day]=1
    else: count[day]+=1
print (count)
