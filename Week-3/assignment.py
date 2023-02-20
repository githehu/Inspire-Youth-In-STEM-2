
#using a for loop add five new musicians
#copy the list to a new list called celebs
#sort the list
#pop out two celebs
#count the remaining celebs in the list
favourite_musicians = ["von","durk","moneybaggyo","foogiano","future","21savage"]
for musician in favourite_musicians:
    print(musician)
favourite_musicians.append("tupac")
favourite_musicians.append("shiesty")
favourite_musicians.append("gucci")
favourite_musicians.append("metro")
favourite_musicians.append("reese")
for musician in favourite_musicians :
    print(musician)
celebs = favourite_musicians.copy()
print(celebs)

celebs.sort()
print(celebs)

celebs.pop()
print(celebs)

print(len(celebs))