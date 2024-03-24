data = {
    3 : "a",
    2 : "b",
    4 : "d",
    1 : "x",
    5 : "e"

}
tup = ((1, 'a'), (2, 'g'), (4, 's'), (5, 'd'))
# print(sorted(data.values()))
# print(sorted(data.items()))
# print(sorted(data.items(), key=lambda i: i[1]))
def my_FUN(x):
    return x[0] #0==first index and 1==secend index in list or tuple and any object

print(sorted(tup, key=my_FUN))
