"""Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.
Test your file on the mbox.txt and mbox-short.txt files."""


fname = input("Enter file name: ")
fh = open(fname)
add=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos=line.find(':')
    num=float(line[pos+2:])
    add+=num
    count+=1
print('Average spam confidence:',add/count)
