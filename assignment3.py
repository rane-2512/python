```python
# Open the file in read mode
with open("assignment.txt", "r") as file:

    # Read the entire content of the file
    content = file.read()

# Split the content into a list of words
words = content.split()

# Print the total number of words in the file
print("Total number of words:", len(words))

# Convert the list into a set to remove duplicate words
unique_words = set(words)

# Print all unique words
print("\nUnique words:")
for word in unique_words:

    # Display each unique word
    print(word)
```
