"""Read a file as a single string and print it forward and in reverse."""
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end=" ")
