"""Exercise 7: Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string."""

def computegrade(sc):
    if 0.0<=sc<=1.0:
        if sc >= 0.9: return 'A'
        if sc>=0.8: return 'B'
        if sc>=0.7: return 'C'
        if sc>=0.6: return 'D'
        return 'F'
    return 'Error! Enter valid score'
score=input('Enter score: ')
try: sc=float(score)
except ValueError:
    print('Error! Enter valid score')
    quit()
grade=computegrade(sc)
print(grade)
