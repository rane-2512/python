# Write data
with open("demo.txt", "w") as f:
    f.write("Python file handling")

# Read data
with open("demo.txt", "r") as f:
    print(f.read())
