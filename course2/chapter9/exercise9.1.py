#Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. Then you
#can use the in operator as a fast way to check whether a string is in the
#dictionary
fh=open('words.txt')
words=dict()
key=list()
value=0
for line in fh:
    line=line.rstrip()
    fjalet=line.split()
    for fjale in fjalet:
        #debug
        #print (fjale)
        if fjale in key : continue
        else:
            key.append(fjale)
            value+=1
            words[key[len(key)-1]]=value
print (words)
