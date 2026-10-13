with open("assignment.txt", "r") as file:
    content = file.read()

words = content.split()


print("Total number of words:", len(words))


unique_words = set(words)

print("\nUnique words:")
for word in unique_words:
    print(word)
