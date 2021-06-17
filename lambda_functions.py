#lambda functions also known as anonymous function

def add(a, b):
    return a + b

addd = lambda a,b : a+b

print(add(4, 5))
print(addd(4, 5))


#So basically lambda functions are the one liner function.
#lambda function can be essential while passing a function as an argument in any attribute
#for example in sort functiom

a = [[1,2],[0, 5], [5, 3]]

a.sort(key= lambda x: x[1])
'''
sort attribute takes an argument key = function which takes a function only
Here to make code time efficient lambda function is essential
lambda function just returns the index 1 of the list a
'''
print(a)