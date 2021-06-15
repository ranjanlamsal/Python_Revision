a = 12
b = 11
print(sum((a,b)))
'''
here sum is built in function of python
Built in functions are predefined functions in python. They are defined in python as default and no need to redefine it
user can easily call the built-in function just by entering the name of function with parenthesis and parameters 
Parameters are the values that are to be passed in function to do the operation. Here sum function requires two parameters 
so if passed less then 2 parameters if shows errors
'''


#Defining your own function
'''
While defining a function we must define in a format : 
def function_name():
    code

#NOTE : a function once defined in a program can be called as many times as wanted hence 
makes the code effective and efficiency
'''

name = input("Enter your name: ")
def function1(name):

    '''This function takes name as parameter and
    returns a print statement as "Hi name"
    This is a doc string'''
    print("Hi", name)

function1(name)
'''When the function is called it goes into the function with given parameter and 
replace the parameter with the inputed parameter. here name is replaced by ranjan
Now print statement inside the function is executed and hence print the value.
This function have nothing to return i.s return is none'''
print(function1(name))
'''So when function is called inside the print statement , function is executed and the return of function is printed
since this function return none value "None" is printed'''


def function2(a,b):
    '''When this function is called , it must be called with two parameters.
    When called it first print the string as of print statement and the return the calue of average
    if the return of function is stored in a variable and then printed it gives the return value.
    Doc String: Defines a function, parameter, gives warning or any other usable notes
    '''
    average = (a+b)/2
    print("The average of function is ", end=" ")
    return average

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
x = function2(a,b) #Function is called so print statement is executed . and the return value is stored in the variable x
print(x)


print(function1.__doc__)
'''functionname.__doc__ gives the docstring in that function'''

