years = int(input("enter a year to check:"))

leap = "leap Year!"
Notleap = "Not a leap year!"

if (years%4==0 and years %100!=0) or (years%400==0):
    print(leap)
else:
    print(Notleap)