a,b,c = list(map(float,input().split()))

formula = b**2-4*a*c
if a == 0 or formula<0:
    print("Impossivel calcular")
else:
    x1 = (-b + formula**0.50)/(2*a)
    x2 = (-b - formula**0.50)/(2*a)
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")