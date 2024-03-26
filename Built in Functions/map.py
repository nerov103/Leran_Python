#how to use map function 
#now ima this show 
#this function return the all reven number

def mkae_even(n):
    if n%2==1:
        return n+1
    else:
        return n
    
number = [1, 2, 3, 4, 5, 6, 9]

# stor = []
# for i in number:
#     stor.append(mkae_even(i))

#this is another why
wya2 = map(mkae_even, number)
print(list(wya2))

#this is anotehr why
# why3 = [mkae_even(j) for j in number]
# print(why3)
# print(stor)
