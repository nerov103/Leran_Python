example = "My name is {name} i'm {age} years old".format(name = "nerov Ahmead", age = 18)
print(example)

'''
amir kasa mona hoy..f{format}
ai format ta ink valo and sosoj
'''

# =======format_map()==========
my_dics = {
    "name" : "nerov",
    "roll" : 100,
    "Hi" : "Hello"
}

result = "My name is {name} and my roll is {roll} ! Aey {Hi} {name}"
print(result.format_map(my_dics))


'''
amir kasa ai format_map() function ta ink valo lagsa..
aita dis ink valo kora kaj kora ji 

'''