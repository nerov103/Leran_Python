
# x = 'name = "Nerov"\nage="18"\nprint(f"Hello mr.{name}")\nprint(f"Her old is {age}")'
# exec(x)

#more examples
key = input("enter yout value:")
vlaue = input("enter your code: ")
exec(f"{key} = {vlaue}")
print(f"the ourport is : {eval(vlaue)}")