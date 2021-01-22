class test:
    def findsum(self,a,b):
        s=a+b
        return s


a = int(input("enter first number "))
b = int(input("enter second number "))

obj = test()
s = obj.findsum(a,b)
print("sum is:",s)
