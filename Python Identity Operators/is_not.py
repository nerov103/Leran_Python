# this is  is not identity opertators in python

a = input("enter your first name:")
b = input("enter your secent name:")

# if a is not b:    
#     print("Your Tow name is same!")
# else:
#     print("your Tow Name is not same!")

def check():
    if a is not b:
        return False
    else:
        return True
print(check())