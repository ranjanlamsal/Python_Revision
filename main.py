'''I commented everything because nothing here gives a useful meaning. Just a bunch of code done for revision'''

#comment
'''multi
line
comment
'''
'''
multi 
line 
comment
'''
# print("Hello world")
# print("Hello","World")
# print("Hello",end = " ")
# print("World")
# print("Hello ",end = "World,")
# print("I am ranjan.")
#
# #escape sequences
#
# print("Hello \n World") #\n for a new line
# print("He said,\"I am fine.\"") # \" to escape "
# print('He said,"I am fine"') # '' can also be used to print statements
# print("Hello \t World") #ecsape a tab
# print("Hello",end="\t")
#print("World")


# var1 = "Ranjan"
# var2 = "Lamsal"
# var3 = 1
# var4 = 1.2
# var5 = var4 + var3
# var6 = "2"
# print(var3 + var4)
# print(type(var5)) # float + int = float
# print(var3 + int(var6))  # manual typecasting
# print(str(var3)) #typecasting

# print("Enter num1")
# n1 = input()
# print("enter num2")
# n2 = input()
# sum = int(n1) + int(n2)
# print(sum)

# #string slicing tut-8
# mystr = "My name is Ranjan"
# print(mystr[0]) #0th index if fof the first char of str
# print(mystr[1]) #1th index is 2nd char and soo on
# print(mystr[0:6]) #from 0th index to (n-1)th index. here "e" is in 6th index
# print(mystr[:6]) # if we wanna print from the 0th index to nth index then no need to write 0 . a blank index(pre) is 0 by default
# print(mystr[1:6])
# # space is also a character so is counted while indexing
# print(len(mystr))
# print(mystr[2:len(mystr)])
# print(mystr[:17])
# print(mystr[:]) #not inputing index defaultly set the index from 0 to last
#
# print(mystr[0:8:2]) #from 0th index to 7th index with a gap of 1 index,
#
# print(mystr[::])
# print(mystr[::2])
#
# print(mystr[::100]) #from first to last index wit gap of 99 indexes. if len is less than 99 100 then only first character is printed
#
# print(mystr[-2:-4]) # negative index start from last . last index is -1 and sooo on in left direction
#
# print(mystr[::-1]) #first string is flipped from last to forst and then indexed
#
# print(mystr.isalnum()) #check whether the string is alpha numeric i.e containing alphabets and numbers
#
# print(mystr.count("a")) #count the number of "a" in string
# print(mystr.capitalize()) #first letter is capitalized
# print(mystr.lower()) #conver to lowercase
# print(mystr.upper()) #convert to uppercase
# print(mystr.find("is"))  #gives index from where the first "is" starts in a string
# print(mystr.replace("is", "are")) #"is" is replaced by "are"



"""LIsts and list funtions tut-9"""
#
# name = ["Ranjan", "Abhi", "sim", "Sid", "1", 42, 4.4] # list may contain string int or float type data
# #INDEX:    0         1       2      3    4    5    6
# print(name)
#
# numbers = [2,4,3,9,5,0]
# print(numbers[2])
# # numbers.sort() #sort the list in ascending order
# # print(numbers)
# #
# # numbers.reverse() #reverse te list
# # print(numbers)
#
# print(numbers[:5])
# print(numbers[:])
#
# #note slicing doesnot change the original list or string but functions can change . sort and reverse chnage the original list
#
# print(numbers[::]) #index 0 to last with the multiple of 1 index
# print(numbers[::2])
#
# print(numbers[::-2]) #index 0- last with negative 2 multiple of index i.e reverse the list and then index of multiple 2 is printed
#
# print(len(numbers)) #length of list
# print(max(numbers)) #max value in list
# print(min(numbers)) #min value of list
#
#
# numbers.append(99) #add an element 99 to the list at end
# print(numbers)
#
# numbers.insert(3, 98) #insert an element 98 to the list at the index 2
# print(numbers)
#
# numbers.remove(2) #remove 2 from the list
# #numbers.remove(1000) #shows a error if value doesnot belong to the list
# print(numbers)
#
# numbers.pop() # remove the last element ftom the list
# print(numbers)
#
# numbers[4] = 97 #4th index of list changes to 97
# print(numbers)
#
# # lists are mutable i.e can be changed
# #tuple are immutable i.e cannot be changed
#
# tp = (1,2,3) # this is a tuple
# print(tp)
#
# t2 = (1,) #to create a tuple of 1 element we must put a comma after the element
#
# a = 1
# b = 3
# a,b = b,a # a simple way to swap value
# print(a,b)

"""Dictionary"""
#
# d1 = {"Ranjan":"Lamsal", "sim":"mis", "num":[1,2,3,4], "dd":{"Q":"q","R":"r","S":"s"}}
# #a dictonary is a key valur pair.key can be either num or str,  value can be a list , tuple or a another dictionary
# print(d1)
# print(d1["Ranjan"]) #to give the value for the given key in dict
#
# d1[122] = "new" #add a ney key value in dict
# print(d1)
# d1.update({"Ran":"Jan"}) #this approach can also be used to add a new key value in a dict
#
# print(d1.keys()) #print keys of dictionary
# print(d1.items()) #print itsma of dict
# print(d1.values()) #print values
#
# del d1["sim"] #deleating the key sim and its vakue from dict
#
# d2 = d1
# del d2[122]
# #after deleting the key in newly maid dict (d2=d1), the key is also deleated in original dict
# print(d1)
# # this means d2 is not a new dictionary. change in any of the dict changes in the original dict
# # to avoid this problem we can use .copy() funtion
#
# d3 = d1.copy()
# del d3["Ranjan"]
# print(d3) #key value for Ranjan is deleted in d3 but not in original dict d1
# print(d1)
#


#exercise 1
#
# mydic = {"A":"a", "B":"b", "C":"c","D":"d"}
#
# print("Enter a word")
# print(mydic[input()])
#


"""Set"""
#
# s = set()
# l = [1,2,3,4]
# s_from_list = set(l) #we can have int, string, list or dict in a set
#
# #set functions
#
# s.add(1) #adding 1 in set s
# s.add(1) #again after adding 1 in set s there only be one 1 in the set because set in group of uniquly defined objects
# s1 = s.union({2,3,4})
# print(s1)
# s2 = s.intersection({2,3,4}) #gives intersection
# print(s2)
# print(s.isdisjoint(s2)) #if sets are disjoint or not
# s1.remove(2) #removing an element from set
# print(s1)
# print(len(s1))


"""If else elif conditions"""

#we can use as many is statements as we can but while executing the code it goes to every if statements and so may takes time
#so it is better to use elif if there are more than two conditions

# li = [1,2,3,4,]
# if 5 in li:   #if statement to check if an element is in list or not
#     print("True")
# else:
#     print("false")


#Exercise 2
"""Faulty calculator
45*3 = 145, 56+9 = 77, 56/6= 4"""

# print("Welcome to faulty calcultor.\n Use the following sign for operations:\n '+' : for addition\n '-': for subtraction\n '*' : for multiplication\n '/' : for devision\n '%' : for modulo\n '**' : for power")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# oprtr = input("Enter your operator")

# if num1 == 45 and num2 == 3 and oprtr == "*":
#     print("145")
# elif num1 == 56 and num2 == 9 and oprtr == "+":
#     print("77")
# elif num1 == 56 and num2 == 6 and oprtr == "/":
#     print("4")

# if oprtr == "+":
#     print(num1 + num2)
# elif oprtr == "-":
#     print(num1 - num2)
# elif oprtr == "*":
#     print(num1 * num2)
# elif oprtr == "/":
#     print(num1 / num2)
# elif oprtr == "%":
#     print(num1 % num2)
# elif oprtr == "**":
#     print(num1 ** num2)
#
#

"""For loop
for loop in python is used to iterate over a sequence (list,tuple,string or other iterable objects)
 for value in sequence: (here value is variable that takes the value of the item inside the sequence on each iteration
 Body of for"""

# list1 = ["1","2","3","4"]
# print(list1[0],list1[1],list1[2],list1[3])
#
# for item in list1:
#     print(item) #instead of writing item we can use any word for refrence

# list2 = [["Ran","jan"],["lam","sal"],["sim","mis"]]
# for name, nickname in list2:
#     print(name, nickname)

# dict1 = dict(list2) #typecasting list to dict
# for name, nickname in dict1.items(): #to iterate every items in dict then we must use attribute .items()
#     print(name,"and nickname is",nickname)
#
# for item in dict1: #simply calling dict one iterates over the keys
#     print(item)
# for item in dict1.values(): #whereas to iterate over values we must call the values of the dict
#     print(item)

#quiz
# items = ["A","B",4,5,9,66,"C",0]
# for item in items:
#     if str(item).isnumeric() and item >6:
#         print(item)

"""While loop
for loop iterates over a terable value and runs until the last item of a iterable
 while loop runs until a condition is true"""


# while True:
#     num = int(input("Enter a number: "))
#     if num <= 100:
#         print("try again!!!")
#         continue #goes back to the starting of loop. further lines after continue is not executed
#     else:
#         print("COngoooooooooo")
#         break #breaks the loop

#Exercise 3
''' Guess the number'''
# lucky_num = 41
# no_of_guess = 5
# while (no_of_guess > 0):
#     num = int(input("Enter a number.\n"))
#     no_of_guess -= 1
#     if num > lucky_num:
#         print("Lower the number ")
#         print("no of gueses left :",(no_of_guess) )
#         continue
#     elif num < lucky_num:
#         print("Higher the number",)
#         print("no of gueses left :", (no_of_guess))
#         continue
#     else:
#         print("Congoooooooo")
#         break
#
# if (num == lucky_num):
#     print("You win")
#     print("no of guesses left:",(no_of_guess))
# else:
#     print("You loose")
#     print("you have no guess left")
#



