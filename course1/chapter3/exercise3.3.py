#Exercise 3: Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table:
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Enter score: 0.95
#A
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5
#F
grade=''
score=input('Enter score: ')
try:
    sc=float(score)
except:
    print('Error! Enter valid score')
    quit()
if 0.0<=sc<=1.0:
    if sc >= 0.9: grade='A'
    elif sc>=0.8: grade='B'
    elif sc>=0.7: grade='C'
    elif sc>=0.6: grade='D'
    else: print('F')
else:
    grade='Error! Enter valid score'
print(grade)
