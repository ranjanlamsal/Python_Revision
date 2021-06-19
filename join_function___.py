list1 = ["Ran", "jan", "Heyy", "soooo", "Chowchow", "chinese"]

for item in list1:
    print(item, "and", end = " ")

print("nothing. Okay byeeeeee")


'''
string.join() function takes iterable as argument
and returns a single string joining every item of iterable 
with the string passed

'''

join = " and ".join(list1)
print(join)

print(", ".join(list1)) #joining iterables with a comma and space