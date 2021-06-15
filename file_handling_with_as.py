"""
while reading or writing a file , file pointer is created
There is another approach of creating a file pointer by using with as
"""

with open("Ranjan1.txt") as f:
    print(f.read(5))
    #it does the same as opening file by open function.
    #this approach is more benificial as we donot need to close the file every time we open it.


f = open("Ranjan1.txt")
print(f.readlines())