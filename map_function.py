#map(func, iter)
'''
map is basically a way to pass every element of given iterable into
the given function and get the result again an iterable.
map(func,list) = [func(list[0]), func(list[1]), func(list[2]), func(list[3])..)



fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)
'''

def addition_(num ):
    return num + num

numberss = [1,2,3,4,5]

result = list(map(addition_, numberss))
print(result)

result1 = list(map(lambda x : x + x, numberss))
print(result1)


def sq(a):
    return a*a

def cub(a):
    return a*a*a


func_list = [sq, cub]

for i in range(5):
    res = list(map(lambda x: x(i), func_list))
    print(res)
'''
Here lambda function takes an argument and returns argument(i),
that is it takes function as argument and then gives argument i 
to that function. adn we mapped it to the iterables func_list which
again is a list of functions. so when these functions are given to lambda as argument
 then it gives i as argument to the functions again.
 so .. [sq(i), cub(i)]
 in first iteration of for loop i = 1
 and then for second iteration i.e when i = 2, again a new list is formed as
 [sq(2), cub(2)], and soo on
'''


 