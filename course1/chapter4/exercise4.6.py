"""Exercise 6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters
(hours and rate)."""

def computepay(hour,rate):
    if hour<=40:
        return rate*hour
    return (rate*40)+((1.5*rate)*(hour-40))
def check_float(inp):
    try:
        val=float(inp)
        return val
    except ValueError:
        print('Error, enter a numeric imput')
        quit()
inphours=input('Enter hours: ')
hour = check_float(inphours)
inprate=input('Enter rate: ')
rate = check_float(inprate)
pay=computepay(hour,rate)
print('The salary is:',pay)
