age = 16
gender = "male"

if (age<20):
    print("you are still young")
else:
    print("You should get an id")

#compound/multiple conditions
if((age>30) & (gender == "Male")):
    print("you qualify for a loan")
else:
    print("No loan for you")

fav_colour = "black"
age = 21
if(fav_colour == 'black') | (age <=20):
    print("happy birthday to you")
else:
    print("no birthday present for you")