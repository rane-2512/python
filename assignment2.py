```python
# Take a sentence as input from the user
sen = input("Enter a sentence: ")

# Split the sentence into a list of words
words = sen.split()

# Assume the first word is the longest
longest = words[0]

# Check each word in the list
for word in words:

    # Compare the length of the current word with the longest word
    if len(word) > len(longest):

        # Update longest if the current word is longer
        longest = word

# Print the longest word
print("Longest word =", longest)
```
