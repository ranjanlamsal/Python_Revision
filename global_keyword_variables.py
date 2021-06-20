var1 = 55
var2 = 100
var3 = 111
#These are global variable. i.e any function can access this variable if var1 is called

def normal_func(r):
    var_local = 40
    """
    This is a local variable. Its scope is withing this function only.
    """
    var1 = 50
    """
    Although var1 is a global variable, we can redifine it in a local scope.
    """

    print("This function does nothing.", r)

    print(f"var1 = {var1}")
    '''when var1 is called first it is searched in its local scope
    If it is present in local scope then that value is used. If not then 
    the program search for var1 in global scope and the value of global scope is used.
    if it is absent in global scope then error is thrown
    '''
    print(f"var2 = {var2}")
    #present in global scope
    print(f"var_local = {var_local}")
    #present in only local scope

    var1 += 4
    #since var1 is present in local scope it can be changed in the function
    print(var1)

    #var2 += 44
    '''
    The above line shows error because we cannot change the global variable in local level
    '''

    var_local += 111
    #we van modify local variable
    print(var_local)

    global var3
    """
    after using global inside a function we can modify global or set any new variables 
    inside the local scope. these modifications can be experienced in global scope as well
    """
    var3 += 20
    print(var3)

normal_func("ok Bye")

print(var3)
#var3 becomes 131

#print(var_local)
'''
Although the variable var_local is defined inside the function normal_func()
the above line shows error because var_local is a local variable and can be accessed 
only inside its scope .
'''

def func1():
    x = 30
    #this variable has scope with this function

    def func2():
        #x can be called in this function as well because it is inside func1
        #but we cannot modify x inside this function because x is not a local var of this function


        global x, y
        '''after declearing global, either the value of var can be accessed and modified
        or new variable is created in global scope is initially absent
        '''
        '''
        POINT TO BE NOTED: global scope means outside any function, in the main program
        so after declearing global x program search for x in global scope(even outside func1)
        since there is no var named x , a new global variable is created 
        '''
        x = 88
        y = 99
        # x is 88 in global scope

        print(f"x in func2 = {x}")
        #it returns 88 because x is globally defined and is defined in this function as 88
    print(f"before calling func2 x = {x}")
    #returns 30 because when var x is called it first search in loal scope where x = 30

    # print(f"before calling func2 y = {y}")
    '''
    This line shows error because global y is decleared inside func2 but the func2 
    hasnot been yet called and executed . so still there is no global y = 99 variable
    '''

    func2()
    print(f"after calling func2 x = {x}")
    '''
    after callinf func2() global variable x is decleared as x = 88 but since the scope of
    this command is inside the func1, first x is searched in local scope i.e in func1
    where x =30 
    '''

    print(f"after calling func2 y = {y}")
    '''
    After calling func2 global variable y is defined and set, so calling y first search in local
    scope , if not found then search in global scope and returns y = 99
    '''

func1()
print(f"x in global scope = {x}")
#in global scope x = 88


