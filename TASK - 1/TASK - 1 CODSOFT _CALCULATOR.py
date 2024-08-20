def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
ch = input("Enter operation(1/2/3/4):")
n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
if ch=='1':
    print(n1,'+',n2,"=",add(n1,n2))
elif ch=='2':
    print(n1,'-',n2,'=',sub(n1,n2))
elif ch=='3':
    print(n1,'*',n2,"=",mul(n1,n2))
elif ch=='4':
    print(n1,'/',n2,'=',div(n1,n2))
else:
    print("Invalid Input")
