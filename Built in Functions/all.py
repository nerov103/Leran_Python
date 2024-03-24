'''
The all() function returns True if all items in an iterable are true, otherwise it returns False.

If the iterable object is empty, the all() function also returns True.
'''

# my_list = [1, 3, 8, 4, "hello WOrld", 0]

# result = all(my_list)
# print(result)

'''
when used on dictionary the all() function chacks all key valus is true
'''
# mydis = {
#     'name' : "Mr.Pydor",
#     'from' : "unknow",
#     None : "no data"
# }
# print(all(mydis))

# my_list = []
# x = all(my_list)
# print(x)

#new ima chack the 0 is true or false
# o = 0

# if o is True:
#     print("0 is true!")
# elif o is not True:
#     print("o Not False")
# else:
#     print("something another!")


'''
now ima show this is my locsh

'''
my_list = ["java", "c++", 0]
my_tuple = (50, "NO data")

user_data = {
    'name' : "rana",
    'from' : "japan",
    'age' : 25,
    'granda' : 'Mail',
    "0" : "No data"

}

user_all_data = my_list
check = all(user_all_data)
if check is True:
    print("Login Successfull!")
elif check is False:
    print("User is Not Auto!")
else:
    print("connect to Mr.Pydor")