##################---FIlter Method---####################
"""
The filter() method filters the given sequence with
 the help of a function that tests each element in the
 sequence to be true or not.

 It takes two parameters: a function and a iterable
 function checks every element of iterable is true or not
 and finally  a filter object is created which contains the element
 that returns true after passing through the function.
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_greater_than_5(num):
    return num > 5


num_grtr_than_5 = list(filter(is_greater_than_5, list1))
'''
Here in filter method the function is_greater_than_5() and the iterable list1 is passed
This filter method returns true if the element of the iterable is greater than 5
and false else the element is smaller or equals to five...
since filter method creates a filter object that contains element that 
gives true while passing through the function, number greater than 5 is stored in filter object.
After converting the filter object to list, a list of element that is
greater than 5 is stored
'''
print(num_grtr_than_5)


########-------   Reduce   --------##########


'''
What is reduce and how it works?

The reduce(fun,seq) function is used to apply a particular function 
passed in its argument to all of the list elements mentioned 
in the sequence passed along.This function is defined in “functools” module.

Working :  

1.At first step, first two elements of sequence are 
picked and the result is obtained.
2.Next step is to apply the same function to the previously attained result 
and the number just succeeding the second element and 
the result is again stored.
3.This process continues till no more elements are left in the container.
4.The final returned result is returned and printed on console.
'''
import functools

result = functools.reduce(lambda x,y: x+y, list1)
print(result)