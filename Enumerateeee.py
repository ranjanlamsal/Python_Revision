list1 = ["Ran", "Jan", "lam", "azure", "soWhat?"]

#to print the items in odd position

i = 1

for item in list1:
    if i%2 != 0:
        print(item)

    i += 1


for index, item in enumerate(list1):
    if index%2 == 0:
        print(item)

'''Enumerate function does nothing but takes iterables and creates an object
which list of tuple containing index of element 
of iterable and element of corresponding index
..
So iterating the enumerate object can be benificial while
iterating objects on the bases of their index'''
