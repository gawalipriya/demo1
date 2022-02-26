#open an dread all the comtent of the file
#make convert it into list
#reversed that list
#write back to the file
with open ('test.txt', 'r') as fp:
    content = fp.readlines()          # stored the contents tn the llist
    rev= reversed(content)                 #reserved the list
    with open ('test.txt','w')as fp1:
        for line in rev:
            fp1.write(line)





