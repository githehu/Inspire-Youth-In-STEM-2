#advanced data types

#mutable vs imutable

#mutable are data types that can bechangedduring programme life cycle
#add remove elements

#immutable are data types that cannot be edited during programme life cycle

friends = ["josh","brasso","dennis","leah"]
#1 list (mutable)

friends = ["josh","brasso","dennis","leah"]
# or friends = [] for emty list
#add--->append(),extend()

students = ["sam","paul"]

friends.extend(students)
friends.append("tony")
friends.sort()

#Tuples
#rype of a list that is immutable

stationeries = ("pen","eraser","ruler","pencil","crayons")


#you can replace the whole tuple
stationeries = ("porch","marker","ink")

for stationery in stationeries:
    print(stationery)

numbers = (1,2,3,4,5,6,7,8,87,54)

#dictionaries
#uses key and value pair

student = {"name" : "david","age" : 20,"gender" : "male","is_tall" : "true"}

print (student["name"])
print(student["age"])
print(student["gender"])
print(student["is_tall"])

friend = {"fav_color" : "white","hobby" : "swimming","course" : "education","weight" : "70kg","height" : "2m"}
print(friend["fav_color"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend["height"])


           

