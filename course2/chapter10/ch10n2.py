#Exercise 2: This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.

filehandle=input('Enter a file name')
if len(filehandle)<1: filehandle='mbox-short.txt'
counts=dict()
lt=list()
hours=list()
fh=open(filehandle)
for line in fh:
    line=line.split()
    if len(line)<7: continue
    if line[0] != 'From': continue
    time=line[5].split(':')
    lt.append(time[0])
for hour in lt:
    if hour not in counts:
        counts[hour]=1
    else:
        counts[hour]=counts[hour]+1
for hour, time in counts.items():
    hours.append((hour, time))
hours.sort()
for hour, time in hours:
    print(hour,time)
