greetings = "good morning"
a=4
if a<2:
    print("matched")
else:print("so bad")

print("finished")

#for loops : itterates loops on list
obj = [2,4,7,2,6]
for i in obj:
    print(i)

#sum of first 5 numbers
summ=0
for j in range(1,6):  #for(i=1;i<6;i++)
    summ=summ+j
print(summ)
print("PPPPPPPPPPPPPP")
for k in range(1,11,2):
    print(k)

#while loo
print("**************")
a = 10
while a>1:
    if a==9:
        a=a-1
        continue
    if a == 3:
        break
    print(a)
    a=a-1
print("finished")



