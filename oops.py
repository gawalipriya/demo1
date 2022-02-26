#class is a user defined blueprint or prototype amd having the class variable and class mmethoda .

class cal:
    num1=10

    def __init__(self):
        print("i,ll come frist")


    def getdata(self):
        print("class si created")


obj1=cal()
obj1.getdata()
print(obj1.num1)

print("*********************")

"""class child(cal):
    num2=20

    def add(self):

        return self.num1  +  self.num2

obj2=child()
print(obj2.add())
print(obj2.num2)"""
