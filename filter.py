'''
example one

'''
# list_one = ['mango', 'java', 'html']
# for x in list_one:
#     print(x)
ages = [5, 12, 17, 18, 24, 32]
def myFUN(x):
    if x <18:
        return False
    else:
        return True
adults = filter(myFUN, ages)
# print(adults)
for i in adults:
    print(i)

#end the program