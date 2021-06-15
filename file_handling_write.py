 '''In write mode we have attributes such as :
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist
'''
'''
in write mode:
.write() : which creates the file is not existed . If existed then override the file content
and replace them with the content given in argument.
'''
f = open("Ranjan1.txt","w")
#Ranjan.txt file doesnot exist in the python folder. It is still not created

f.write("Ranjan is a good boy\n")
#now a new file named Ranjan.txt is created with content passed in argument

f.write("Ranjan is not a good boy\n")
'''
Point to be noted: write attribute create new file if not existed and replace the content of the file
if it is already present in project directory. But if you use .write() attribute again
in the same bunch of code i.e without once closing the file pointer, new contents are appended in the
file rather than replacing the old content.
Now when the program is closed and again the file pointer for the same file is opened in new program
then the write attribute override the old content and replace them
'''

f.close()

'''In append mode
.write() attribute is used to append the content given in argument in the file.
this also creates a file if not existed but if existed then append the content in old contents

'''
f = open("Ranjan1.txt", "a")
f.write("Ranjan is a handsome muscular man.\n")
'''
If the file pointer is closed and then again opened in apend mode then the contents are appended in the file
'''

a = f.write("Hey Buddy")
#if we store this attribute then the nukber of characted passed as argument is stored in object
print(a)
f.close()



