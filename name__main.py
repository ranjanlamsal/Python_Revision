'''
We have file name__main.py and name__main2.py to discuss the importance of
__name__ == '__main__' in python
'''

"""
SO basically when we import a module in python then all the functions, objects ,
sub-modules , attributes , variables are imported from that module...
Along with these, the code of that module is also executed and return if there
is any executable code that returns something.

"""

import name__main2

'''
There are 2 functions in name__main2.py module.
'''

test = name__main2.testfunc("New File New Content")
print(test)
test1 = name__main2.tesfunc2("Another new content")
print(test1)

"""
Here when this program is executed , it imports module name__main2.py
So its functions are imported and TO BE NOTED its executable codes 
are also executed so the returns from the execution
 of name__main.py is also returned in this program
"""


"""
Now to remove this anguish if__name__ == __main__ function is used 
Go to file : name__main2.py to see the method to use that function
"""


'''
So what happened here ??
when the __name__ of file is executed in the same file 
where __name__ = __main__ is defined and executable code is 
under this function then the return will be "__main__"

and when __name__ of the same file is executed and that file is imported in 
another program..... in such case __name__ == name of the file ..

So the condition if __name__ == '__main__' is true.. i.e in the same file where 
main is defined... the code under it will be executed.. And incase of the program
were the module (the module containing main) is imported the code 
under __main__ is not executed because __name__ = name of module. 
'''

print(name__main2.name)
#here __name__ will be name__main2 (name of file)