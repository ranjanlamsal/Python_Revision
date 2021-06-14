# #operators in python
# Arthematic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

"""Arithmetic operator
The operators used to perform simple mathematics operations are arithmetic operators
+, -, /, *, **, %, // are arithmetic operatos in python"""

print(5 + 6)
print(5 - 6)
print(5 * 6)
print(5 / 6)
print(5 ** 6) #** means power
print(5 // 6) # // gives the quotent
print(5 % 6) # % gives reminder

"""Assignment operators
Operators used to assign the value to a variable
"""
x = 5 # '=' assign the value 5 to the variable x
print(x)

x+= 1 # x = x+1
print(x)
#now the value of x is 6

x -= 1 # x = x-1
print(x)
#now the value of x is 5

x *= 6 # x = x*6
print(x)
#now the value of x is 30

x /= 5 # x = x/5
print(x)
#now the value of x is 6

x %= 4 # x = x%4
print(x)
#now the value of x is 2

x **= 3 # x = x**3
print(x)
#now thhe value of x is 8

x //= 3 # x = x//3
print(x)
#now the value of x is 2


"""COMPARISION OPERATORS
compares the value of a variable with another"""
# comparision operators compares the two variable or one variable with a data type. If correct returns True else returns False
#It returs Boolean value only (True or False)

i = 6
j = 8
print(i == j) #compares the value of i and j . Since i not equal to j it gives false
print(i >= j) # retutrns False
print(i <= j) #returns True
print(i != j) # != means not equals to so returns True


"""Logical Operators
and, or & not are logical operators in python
Gives Boolean values (True and False)
Works on the basis of boolean algebra
"""
"""

Boolean Algebra:
True and True = True
True and False = False
False and False = False
T or T = T
T or F = T
F or T = T
F or F =  F
not (T and T ) = F 
not operator reverse the value
"""

a = True
b = False

print(a and b) #T and F = F
print(a or b) # T or F = T
print(a and not(b)) # T and not(F) = T and T = t
print(not(a or b)) # not ( T or F) = not(T) = F

"""Identity operators
Identity operators actually compares two variables or data types. Returns True if both are same object and false if are different object
The value of both variables must represent the same object to get true
Two variable can be identity if and only if they are reffered to same object in the memory"""

a = {1,2,3,4,5}
b = {1,2,3,4,5}
c = a
#If printed all a,b, and , gives same values but they are different objects

print(a is b) #it returns false because although the content of a and b is same, while a is created it is stored in memory as a object a and while b is created it is stored as different object b. So they have different identity
print(a is not b) #prints True
print(a is c) #returns True the value or the onject carried by a is assigned to c by '=' operators. They are same object stored in computer memory

print(a == b) # returns true because unlike the identity operator which chech the original identity of a object in the memory, comparision operator only compares the value contained by te objects


"""Membership operator
Operator that checks whether a element is present in a object or not. Especially in iterable objects such as lists, sets,etc

"""
li = [1,3,5,7,9]
print(12 in li) #returns false as 12 is not present in li
print(12 not in li) # Returns True as 12 is not in li
print(3 in li) # Returns True



"""
Bitwise operator in python (it is similar to bitwise operation in other language as well)
bitwise operators works with bits (binary values)
it is same like logical operator except o refers false and 1 refers true"""
'''
& (and) operaror gives 1 to the bit if both of the bits in variables are 1 else sets 0 to bit
| (or) sets bit value to 1 if any of the two bits are 1

~ (not) inverts all the bit values
<< (Left shift) shift all the bit values to bit left omiting the leftmost bit value and inserting 0 to rightmost bit value
>> (right shift) shifts all the bit values to a bit right omiting the rightmost bit value and inserting 0 in leftmost bit

'''

print( 0 | 1)
"""
| is or in bit level. Check al the bit values and if any of the two bit values of same bit position is 1 returns true.
0 in bits : 0
1 in bits: 1
so 0 or 1 = 1
This returns 1
"""
print(11 | 20)
'''
bit value of 11   =  00001011  
bit value of 20   =  00010100
bit value of (11|20)=00011111 = 31 in decimal
hence 11 | 20 is 31
'''

print(11 & 20)
'''
bit value of 11   =  00001011  
bit value of 20   =  00010100
bit value of (11&20)=00000000 = 0 in decimal
'''

print(11&12)
'''
bit value of 11   =  00001011  
bit value of 12   =  00001100
bit value of (11&12)=00001000 = 8 IN DECIMAL
'''



"""
X OR
gives true if both of the value of bit is different i.e 1 and 0
gives false if both value of bit is same i.e 1 ^ 1 = 0 / 0 ^ 0 = 0
"""
print(12 ^ 13)
'''
binary 12  =  00001100
binary 13  =  00001101
binary 12^13 =00000001 = 1 
'''
print(11 ^ 20)
'''
bit value of 11   =  00001011  
bit value of 20   =  00010100
bit value of (11^20)=00011111 = 31 in decimal
hence 11 ^ 20 is 31
'''



'''Bitwise not (~) also called compliment'''
#compliment of a number (not) is converting every bit value to negative i.e true to false and vise versa

'''finding the binary value of negative numbers
two's compliment of a number = negative of that number i.e
binary value of 13 = 00001101
first comliment = ~13 = 11110010
TWO'S compliment = first compliment + 1 
                 = 11110010 +1 = 11110011
     Hence , -13 = 11110011
'''

print(~1)
"""
binary value of 1 : 00000001
binary value of ~1: 11111110 which is two's compliment of 2
so ~1 = -2
"""
print(~12 & 11)
"""
binary value of 12 = 00001100
binary value of ~12= 11110011
binary value of 11 = 00001011
     ~12 & 11      = 00000011 which is equal to 3
"""




"""
BITWISE LEFT AND RIGHT SHIFT
takes two parameters first the value which is to be shifted bitwise and second the number of bits to be shifted 
"""

'''
BITWISE LEFT SHIFT
when a value is left shifted by x bits then all the bit values are shifted to left by x bits and the rightmost bit values upto x bits are replaced by 0's
so basically when you left shift 100111 by 2 bits you get 10011100
So extra x bits are gained when a value is left shifted by x bits
'''
print(11 << 2)
'''
11 binary : 1011
shifting letside by two bits = 101100 which is 44
'''

'''
BITWISE RIGHT SHIFT
when a value is right shifted by x bits then all the bit values are shifted to right by x bits and the leftmost bit values upto x bits are replaced by 0's
so basically when you right shift 100111 by 2 bits you get 1001
So extra x bits are lost when a value is right shifted by x bits
'''
print(11 >> 2)
'''
binary 11 : 1011
right shifted by 2 bits : 10 which is 2
'''
