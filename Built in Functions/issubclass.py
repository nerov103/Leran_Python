#now ima show how to use issubclass() in python function
#first class
class Car:
    pass

#secend calss
class Food(Car):
    pass

#three class
class Forest(Food):
    pass


#now ima use to issubclass() function
result = issubclass(Car, Forest) #check the subclass
# print("Food is Car class subclass: ", result)
if result==True:
    print("Same class subclass this!")
else:
    print("Not!, not same class subclass!")
