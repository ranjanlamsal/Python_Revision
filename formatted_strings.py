#string formatting



var1 = 23
var2 = 23.55


a = "I have %d rupees"%var1
'''This is an old approach of string formatting where 
you pass %operator in strings and then %variable to replace the value
in the string
'''
'''
%d converts the value of variable var1 to decimal format and
pass it in string 
'''
print(a)

b = "I have %o rupees"%var1
print(b)
'''
%o operator gives octal value of var1 and pass it to string
'''

c = "I have %u rupees"%var2
print(c)
'''
%u operator gives obsolete value of var1 and pass it to string
'''

d = "I have %x rupees"%var1
print(d)
'''
%x operator gives signed hexadecimal(lowercase) value of var1 and pass it to string
'''

e = "I have %X rupees"%var1
print(e)
'''
%X operator gives signed Hexadecimal (uppercase) value of var1 and pass it to string
'''

f = "I have %o rupees"%var1
print(f)
'''
%f operator gives floating point in exponential form
 of var1 and pass it to string
'''

g = "I have %F rupees"%var2
print(g)
'''
%F operator gives floating point in decimal format
 of var1 and pass it to string
'''

h = "I have %c rupees"%var1
print(h)
'''
%c operator single character (accepts integers or single character)
 of var1 and pass it to string
'''

i = "I have %s rupees"%var1
print(i)
'''
%s operator convert var1 to string using str() and pass it to string
'''

j = "I have %a rupees"%var2
print(j)
'''
%j operator convert var1 to ascii value using ascii() and pass it to string
'''

me = "Ranjan"
var = 19

a = "This is %s %s"%(me,var)
print(a)

#formating also can be done using .format() attribute
b = "this is {} {}"
print(b.format(me,var))
'''
.format attribute can be called to the string type such as b and passing
the variables as the arguments
'''

print(b.format(var,me))
'''
exchanging the position of variables while passing in .format() argument also
exchanges the output
'''

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
'''
here the index is used. index 0 is the first argument in .format() attribute 
and so on
'''



####---   F-strings   ----#####

c = f"This is {me} {var}"
print(c)

print(f"2 + 2 = {2 + 2}")

import math
print(f"cos65 = {math.cos(65)}")