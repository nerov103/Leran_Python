# import math
# result1 = (1.0 - 5.0)**2
# result2 = (7.0 - 9.0)**2
# plush = result1 + result2

# print(math.sqrt(plush))

from math import sqrt
x1,y1 = list(map(float, input().split(" ")))
x2,y2 = list(map(float, input().split(" ")))

result1 = (x2 - x1)**2
result2 = (y2 - y1)**2
result = sqrt(result1 + result2)

print(f"{result:.4f}")


# another example
# a = input().split(" ")
# print(a) #like this outport example like here: ['1.0', '7.0', '5.0', '9.0']