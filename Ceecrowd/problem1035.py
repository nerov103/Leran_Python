a,b,c,d = list(map(int, input().split(" ")))

if b>c and d>a and (c+d) > (a+b) and c%2==0 and d%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")