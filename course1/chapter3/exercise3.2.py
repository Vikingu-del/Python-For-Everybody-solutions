#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

hinp=input('Enter hours: ')
try:
    hours=float(hinp)
except:
    print('Error! Enter a numeric input')
    quit()
rinp=input('Enter rate: ')
try:
    rate=float(rinp)
except:
    print('Error! Enter a numeric input')
    quit()

if hours<=40:
    pay=hours*rate
else:
    pay=(40*rate)+(hours-40)*(1.5*rate)
print(pay)
