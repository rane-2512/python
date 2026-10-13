with open("assignment.txt", "r") as file:
    lines = file.readlines()


print("Total number of lines:", len(lines))


if len(lines) >= 2:
    print("2nd line:", lines[1].strip())

if len(lines) >= 4:
    print("4th line:", lines[3].strip())
