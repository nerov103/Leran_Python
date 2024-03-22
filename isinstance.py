#one class
class windows():
    name = "Windows xp"
    another_name = "windows 10"

win = windows()

#tow class
class MCos():
    name = "MackBook pro"
    another_name = "Mini mcbook pro"
mc = MCos()

#now ima chack the isinstance() function 
value = isinstance(mc, MCos)
if value==True:
    print("Win holo mc class object!")
else:
    print("NO! win is another class object!")

