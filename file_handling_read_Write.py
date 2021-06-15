'''r+ mode is used while both reading and writing the file content'''

f = open("Ranjan1.txt","r+")
print(f.read())
#the point about the file pointer is again the same. Indexing is same as discussed in read mode

f.write("\nHeyyyyyyyyyyyyyyyy")
#now this allows us to write in the file. here write attribute append the content in file

print(f.read())