

def factorial_iterative(num):
    """
    Creating factorial function that takes iterative approach

    :param num: Integer
    :return: factorial of number
    """
    fac = 1
    for i in range(num):
        fac = fac* (i+1)
    return fac


def factorial_recursive(num):
    """
    Creating factorial function that takes recursive approach
    :param num: Integer
    :return: factorial of number
    """
    if num == 1:
        return 1
    else:
        return num * factorial_iterative((num - 1))

"""
Recursive working in this case:
return num * factorial_recursive(num-1)
5 * factorial_recursive(4)
5 * 4 * factorial_recursive(3)
5 * 4 * 3 * factorial_recursive(2)
5 * 4 * 3 * 2 * factorial_recursive(1)
5 * 4 * 3 * 2 * 1
"""

number = int(input("Enter a number: "))

print(factorial_iterative(number))

print(factorial_recursive(number))


#Fibonacci sequence

def fibo(num):
    if (num == 1):
        return 0
    elif (num == 2):
        return 1
    else:
        return (fibo(num - 1) + fibo(num - 2))

num = int(input("Enter how long do you want the sequence?"))
if (num < 0):
        printf("Invalid number!! Input positive integer.")
else:
    result = fibo(num)
    print(f"The {num}th fibonacci sequence is {result}")
