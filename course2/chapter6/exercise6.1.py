"""Exercise 1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards."""
thing='chair'
prefix=len(thing)-1
while prefix>=0:
    print (thing[prefix])
    prefix-=1
