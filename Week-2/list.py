names = ("Fiona", "Samara", "David")
#accesing names on a list
print(names)
print(names[0])
print(names[0:2])
print(names[-1])
fruits = ("kiwi","apple","banana","mellon","strawberry")
print(fruits[0:-1])
print("My favorite fruit is",fruits[1].upper())
#Adding two lists
vegetables = ("tomato","cucumer","kales","spinach","cabbage")
print(vegetables[2:3])
stationery = ("pencil","eraser","pen","sharpener")
shoppings = vegetables + stationery
print(shoppings)
print(shoppings[3])
for vegetable in vegetables :
    print(vegetable)
for shopping in shoppings :
    print(shopping)
print("My name is  " + names[2] + "  and my favorite fruit is  " + fruits[2])