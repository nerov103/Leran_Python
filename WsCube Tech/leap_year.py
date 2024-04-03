one = 100
tow = 4 #leap year 4year por por akber asa
three = 400
massge = "is a leap year"
year = int(input("enter your year:"))

if (year%three==0) and (year%100==0):
    print(year,massge)

elif (year%4==0) and (year%100!=0):
    print(year,massge)
else:
    print(year,"Not Leap Year!") 