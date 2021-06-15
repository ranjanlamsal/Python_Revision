'''While opening the file pointer in read mode then the initial index of the file pointer is 0
When you access further content of the file using .read(n) attribute the argument n
is up to where the file is to be accessed . Then the file pointer is moved to that index position
After a bunch of read attribute file pointer may be somewhere else'''


# .tell() attribute is used to find out the current index of file pointer

f = open("Ranjan1.txt")
print(f.tell())
#initially at 0

print(f.read(5))
#reading up to 5 further index

print(f.tell())
#now at index 5

print(f.read(6))
#reading further 6 indexes

print(f.tell())
#now at index 11

'''
.seek() attribute reset the file pointer to desired index
'''
f.seek(0)
#file pointer at 0 now
print(f.tell())