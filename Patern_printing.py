#Exercise 4

'''
Input = integer n
input = Boolean variable
for true
*
**
***
****...n

for false
*
**
***
****...n
'''

n = int(input("Enter the number of rows in patern: "))
p = input("Enter T for straight pattern. F for inverted pattern: ")

i = n

if p == "T":
    is_straight= True
else:
    is_straight = False

while(is_straight and n>=0):
    print((i-n)*"*")
    n-=1
while(not is_straight and i>0):
    print(i * "*")
    i -= 1