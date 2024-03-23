#now ima show how to use to locals function  in python 
# now goto the coding ...

def locals_x():
    dis = [10, "Hello", 50]
    # more_dis = ("java", 00)
    print(locals())

locals_x()
print(locals())
#this is another function
def function2():
    print(locals())
function2()

print(locals())