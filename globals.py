# print(globals())
'''
this is globals varable 
ima show how to use tihs  function
'''
a = 20
def show():
    a = 10
    print(a)
    x = globals()['a']
    print("ima a globals:", x)
    update_globals = x = 100
    print("Update globals",update_globals)

show()
print(a)
