
lower = int(input("enter your lower number here:")) #exaple user type 0
upper = int(input("enter your upper number here:")) #example user type 10

for num in range(lower, upper+1): #start the 0 and end the 9 + 1 == to 10
    if num>1: 
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)

'''
this is output in this code

2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
'''