'''
This module is created to be imported in name__main.py module
'''

def testfunc(string):
    return f"This is a test function......{string}"


def tesfunc2(string):
    return f"This is another test function........{string}"


#
# print(testfunc('Hiiiiiiiiiiii'))
# print(tesfunc2("Just making my codes dirtyyyyyyyyyyy"))
# print("These lines should not be executed")


"""
Now we have to create this function if __name__ == '__main__' and 
write all the executable code inside this function..
So when this module is imported, python interpreter skips this
function and imports all the other function
"""

#Executable code starts here
name = __name__

if __name__ == '__main__':
    print(name) # name will be __main__
    print(testfunc('Hiiiiiiiiiiii'))
    print(tesfunc2("Just making my codes dirtyyyyyyyyyyy"))
    print("These lines should not be executed")


