my_list=[] #empty list
print(my_list) #[]
colors=["red","green"]
colors.append("green") #add new value at end
print(colors)
colors.insert(1,"yellow") #add new value at specific position
print(colors)
colors.remove("red") # to remove that item with his value name
print(colors)
colors.pop()
print(colors)
#fun 
print(len(colors))
#print(sum(colors))
print(sorted(colors))#reverse=True for desc

print(max(colors))
print(min(colors))
