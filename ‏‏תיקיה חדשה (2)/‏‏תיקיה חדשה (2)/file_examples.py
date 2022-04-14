# READING FROM A FILE
from os.path import exists, isfile

print(exists("test.txt") and isfile("test.txt"))

try:
    with open('test.txt', 'r') as f:  # a w
        print(f.read())

        for line in f:
            print(line.rstrip())

        f.seek(0)
        print(f.readlines())

        print([line.rstrip() for line in f.readlines()])

        for line in reversed(f.readlines()):
            print(line.rstrip())

        for line in f.readlines()[1:3]:
            print(line.rstrip())
except FileNotFoundError:
    print("The specified file doesn't exist")
except PermissionError:
    print("You don't have permission to read from the file")

# WRITING TO A FILE
try:
    with open('test.txt', 'w') as f:  # a
        f.write("My amazing text")
except PermissionError:
    print("You don't have permission to read from the file")
