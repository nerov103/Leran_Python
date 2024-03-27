
user = int(input()) #tk==(576)=>500
print(user)

my_data = [100, 50, 20, 10, 5, 2, 1]
for i in my_data:
    print(f"{user//i} nota(s) de R$ {i},00")
    user = user%i

