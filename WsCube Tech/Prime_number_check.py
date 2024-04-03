number = int(input("Check Prime Or Not:"))

if number==0:
    print("Not Prime Number!")

if number > 1:
    for i in range(2, number):
        if number%i==0:
            print("This not Prime Number!")
            break
    else:
        print(i, "Prime Number!")