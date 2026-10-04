marks=[12,33,56,89,10,40]
print(marks)
print(marks[1])
print(len(marks))

marks[2]=50#changing value
print(marks)

print(marks[0:2])#slicing

print(marks[-5:-1])#negative index

marks.append(69)#add new value at end
print(marks)

print(marks.sort())#default asc order
print(marks)

print(marks.sort(reverse=True))#desc order
print(marks)

print(marks.reverse())#reverse string
print(marks)

print(marks.insert(2,100))#insert new wlw in betwn
print(marks)

print(marks.remove(100))#remove the given ele
print(marks)

print(marks.pop(2))#remove the given index ele
print(marks)
