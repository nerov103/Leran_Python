string = "Hello world"
l = [10, 20, 30, 40, 50]

iter_obj = iter(l)
print(iter_obj)

print(next(iter_obj))

for i  in iter_obj:
    print("i= ",+ i)

# print(iter(string))
# print(type(iter(string)))