my_list = ["html", "css"]
iter_obj = iter(my_list)

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj, "hello, ima optional"))

for i in range(5):
    ei = next(iter_obj, "hello ima a optionl")
    print(ei)
