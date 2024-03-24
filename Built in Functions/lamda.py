#create a functon in lamda
def main_function(i):
    return lambda x: x + i
call_main_funcation = main_function(7)
print(call_main_funcation(3))

#and the function
#nwo ima show another example
lambda_function = lambda a: a + 2
print("Hello ima secend lamdba function:",lambda_function(8))
