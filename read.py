import fileinput
#with open ('test.txt') as fp:      #alternate way to open file where you need not to close file manually
fp = open('test.txt')           #file opened

# print(fp.read())                #read whole contents of the file

# print(fp.read(2))                 #read perticular number of characters


print(fp.readline())               #read single line content

print(fp.readline())

print(fp.readline())

#read all the conternts line by line

"""line = fp.readline()          #using while loop
while line!= "": 
    print(line)
    line = fp.readline()"""

for line in fp.readlines():       #readlines convet the whole file into list
    print (line)


fp.close

