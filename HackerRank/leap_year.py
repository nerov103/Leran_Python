def is_leap(ys):

    if ys%100==0:
        return True
    elif ys%400==0:
        return True
    else:
        return False

year = int(input())
print(year)