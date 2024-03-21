'''
now ima show how to use getarrt() function in python
'''
class new_class:
    name = "javascript"
    roll = 100
    country = "Japan"
'''
jode aiter attribute nam bol hoy tahola tome "not show this massge ai massge ta print korba are  na hola tome crreat ans ta show korba
'''
obj = getattr(new_class, "roll", "Not show this massge")
print(obj)

# print(getattr(newFUNCTION, 'roll', "Nerov hello"))
# colling_the_class = getattr(newFUNCTION, 'roll')
# print(colling_the_class, "Hello Alom")
# colling_the_class()