#Exercise 4: Add code to the program in ch9n3 to figure out who has the
#most messages in the file. After all the data has been read and the dictionary
#has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.


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


#for keys in cm:
    #print (keys,cm[keys])
#print (cm)
maximum=None
theone=None
for m, count in cm.items():
    if maximum is None or count>maximum:
        maximum=count
        theone=m
print('The most receiving addres is:', theone, 'with', maximum, 'emails')
