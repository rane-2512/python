```python
# Open the file in read mode
with open("assignment.txt", "r") as file:

    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Print the total number of lines in the file
print("Total number of lines:", len(lines))

# Check if the file contains at least 2 lines
if len(lines) >= 2:

    # Print the second line after removing extra spaces and newline
    print("2nd line:", lines[1].strip())

# Check if the file contains at least 4 lines
if len(lines) >= 4:

    # Print the fourth line after removing extra spaces and newline
    print("4th line:", lines[3].strip())
```
