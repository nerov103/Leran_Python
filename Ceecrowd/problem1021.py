# order = float(input())

# lst = [100, 50, 20, 10, 5, 2]
# print("NOTAS:")
# for i in (lst):
#     print(f"{int(order//i)} nota(s) de R$ {i}.00")
#     order = float(f"{order%i:.2f}")

# print(order)
# float(f"{order:.2f}")

# coin = [1, 0.50, 0.25, 0.10, 0.05,0.01]
# print("MOEDAS:")
# for x in (coin):
#     print(f"{int(order//x)} moeda(s) de R$ {x:.2f}")
#     order = float(f'{order%x:.2f}')
  
order = float(input())

lst = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for i in (lst):
    print(f"{int(order//i)} nota(s) de R$ {i}.00")
    order = float(f"{order%i:.2f}")

coin = [1, 0.50, 0.25, 0.10, 0.05,0.01]
print("MOEDAS:")
for x in (coin):
    print(f"{int(order//x)} moeda(s) de R$ {x:.2f}")
    order = float(f'{order%x:.2f}')
