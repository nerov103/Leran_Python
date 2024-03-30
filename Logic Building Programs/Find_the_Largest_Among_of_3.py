message = "is largest"
A = int(input("Enter A value :"))
B = int(input("Enter B value :"))
C = int(input("Enter C value :"))

if A>B and A>C:
    print(A, message)
elif B>A and B>C:
    print(B, message)
else:
    print(C, message)