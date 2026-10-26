# Count the vowels in a text file

vowels="aeiouAEIOU"
count=0

with open("apply note.txt", "r") as file:
    f = file.read()

for ch in f:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
