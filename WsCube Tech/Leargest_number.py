a = int(input("Type Number (A):"))
b = int(input("Type Number (B):"))
c = int(input("Type Number (C):"))

if (a>b) and (a>c):
    print("Largest Number is: ",a)
elif (b>a) and (b>c):
    print("Largest Number is: ",b)
else:
    print("Largest Number is: ",c)