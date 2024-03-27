
# a,b = 1.0, 7.0
# x,y = 5.0, 9.0

# xa = (x - a)**2
# yb = (y - b)**2
# result = (xa + yb) /2
# print(result)
# import math

# def euclidean_distance(point1, point2):
#     return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# # Example usage:
# point1 = (1.0, 7.0)
# point2 = (5.0, 9.0)
# # print("result:",point1[1])
# print(euclidean_distance(point1, point2))
# 1015 number poblem 

# user_data = input().split(" ")
# value = map(float, user_data) # aita akta object create korba ba mamory location
# to_list = list(value) #ami object taka akta list convart korlam

x1, x2 = list(map(float, input().split(" ")))
y1, y2 = list(map(float, input().split(" ")))

result = ((y1 - x1)**2 + (y2 - x2)**2)**0.5

print(f"{result:.4f}")