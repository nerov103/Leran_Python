
count = [0, 1, 2, 3]
my_list = [1, 20, 50, 80] # this is a simple list
# print(len(my_list)) # now ima check the list len
# index = 0
# for i in my_list:
#     print(i)
#     if index==3:
#         print("Hello Harry!")
#     index+=1

#this is another example
# enumreate_list = enumerate(my_list, 1)
# # print(enumreate_list) #create a enumreate object
# convart_tolist = list(enumreate_list) # now ima convart to list
# print(convart_tolist)

fav_food_list = ["mango", "chre", "banana", "goyba", "apple"]
# for x,y in enumerate(fav_food_list, 1):
    # print(f"{x}.{y}")
    
conv = enumerate(fav_food_list, 1) # this is outport the a object and mamore location in my pc
conv_to_dics = dict(conv) # and thean crate a dictnary formate
# print(conv_to_dics) #print the dict value

import json
cov = json.dump(conv_to_dics)
print(cov)
