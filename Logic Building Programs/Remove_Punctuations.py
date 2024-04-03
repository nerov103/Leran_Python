demo = input("Enter a string with Punctuations: ")
Punctuations = "?\[*&#$]"
value = ""

for i in demo:
    if i not in Punctuations:
        value+=i

print(value)