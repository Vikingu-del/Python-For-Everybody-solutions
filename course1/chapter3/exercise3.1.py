#Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.

hours=float(input('Enter hours: '))
rate=float(input('Enter rate: '))

if hours<=40:
    pay=hours*rate
else:
    pay=(40*rate)+(hours-40)*(1.5*rate)

print(pay)
