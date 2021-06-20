def printer(a,b,c,d):
    '''
    This function takes four arguments and return a print statement
    '''
    print("inputed arguments are : ", a, b, c, d)

printer(1,2,3,4)

#now if we need to pass five arguments in the same function then it will throw error

def use_of_args(normal, *args, **kwargs):
    '''
    If we dont know want to limit the no of arguments in a function, then
    we create a function with parameter = *parameter eg: *args or *names
    This way we can pass as many arguments as we want in the function
    and the function takes those arguments as tuple and returns appropriate result
    as a tuple with no error
    *args must be a iterable i.e list, tuple,set...wict is finally converted into
    a tuple

    normal argument also can be passed in the function.
    First normal argument must be passed and only *argument must be passed

    FInally third argument must be **kwargs.
    if we pass arguments after ** then it is **kwargs
    **kwargs must be a mapping i.e a dictionary
    (normal, *args, **kwargs ) this is a convention and we must follow
    '''
    global a
    print(normal)

    for items in args:
        print(items)
    print(type(args))

    # print(args[2])
    print(args)

    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

argument2 = (1,2,3,4,5)
normal_arg = "This is a normal argument"
argument3 = {"a":"A", "b":"B", "c":"C", "d":"D"}

use_of_args(*argument2)
'''
while passing the argument we must pass it as 
*name_of_argument (if the no of argument is unknown.

Normal argument is not compulsion 
kwargs is also not compulsion


'''

use_of_args(normal_arg)
'''If we only pass a normal argument then , by default *args = []
so a empty tuple is returned'''


use_of_args(normal_arg, *argument2)
'''
kwargs by default = {}
'''

use_of_args(normal_arg, *argument2, **argument3)
'''
When all three arguments are passed then also function runs well
'''

"""
NOTE: 
when we pass normal argument only then *args argument is defaultly
taken as []. **kwargs is taken as {}
If we pass *args argument only, normal is not a necessity, while *kwargs 
by default is {}
But we cannot take kwargs only it returns error...
either normal argument or *args must be passed

"""

use_of_args(normal_arg)
'''
in return we can see 
class tuple for args and dict for kwargs which are not even passed in the function.
which means if not passed then args = ()
and kwargs = {}
'''


argument2 = [1,2,3,4,5,6,7,8,9]
use_of_args(*argument2)
'''
even after adding further elements in argument2 the function runs perfectly
'''
