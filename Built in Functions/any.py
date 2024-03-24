'''
The any() function returns True if any item in an iterable are true, otherwise it returns False.

If the iterable object is empty, the any() function will return False
'''
# my_list = [False, False, False, True]
# print(any(my_list))

mydict = {0 : "Apple", None : "Orange"}
x = any(mydict)
print(x)
