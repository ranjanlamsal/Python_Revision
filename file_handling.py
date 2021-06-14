"""Basics of file handling in python"""

'''The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
open("filename", "mode")'''

'''
Modes
"r" - open file for reading, error if file doesnot exist
"w" - open file for writing, creates the file if doesnot exist
"x" - creates specified file if not exist. If file already exist then a error is shown
"a" - append a content to a file, creates the file if it doesnot exist
"t" - text mode (the file must be a text file to open in text mode)
"b" - binary mode (opening binary file)
"+" - read and write

NOTE: when mode is not specified then python by default takes mode as "rt" i.e read and text

'''

f = open("Ranjan.txt")
'''here the file is stored in a file pointer f
by default the mode is read + text mode in python
'''

# content = f.read()
'''.read() is a attribute for a file pointer that reads all the content of file.
And here it is stored in a object "content"
'''
# print(content)
#when the object is passed in print statement it print all the content in file

content = f.read(3)
'''.read() attribute takes an argument index . i.e if an integer is passed then the read attribute 
access the content in file upto that index only
Here the content of file is accessed upto 3 index
if nothing is passed in argument then by default the index is length upto last character
i.e all the content is accessed '''
print(content)

'''One thing to be noted is that along with the accessed content the file pointer is 
also moved to that index. i.e now my file pointer is at index 3. if file.read(x) with an index is stored 
in another object then the initial index will be where the pointer is automatically.
In this case pointer is at index 3.'''

next_content = f.read(4)
#now the pointer mover further 3 index i.e 6th place from begining
print(next_content)

# total = f.read()
# print(total)
'''first the pointer is moved to index 3 then again moveds further 3 index. so now if the
f.read is stored in another object then whole file content from where the pointer is to the
last indext of the file is printed. In this case from "e" to ".".'''




'''At this point the file pointer is at index 7 first 3 and the 4 = 7'''

for line in f:
    print("line : ",line)
'''Here line by line contents of the file are printed. since the pointer is initially at 7th index.
so from 7th index only line are printed one by one'''

f.seek(0)
'''.seek() attribute is used to reset the pointer at 
desired index.
Now the pointer is at 0 index'''

print(f.readline())
'''.readline() attribute read the content of the file line by line.
first first line is read then the pointer moves to the end of the first line.
Again if the radline() attribute is called, another line is read'''
#pOINTER IS AT THE END OF LINE1

print(f.readline(5))
#when argument (integer)

print(f.readlines())

f.close()
#closing a file is not compulsary but it is a good practice.

