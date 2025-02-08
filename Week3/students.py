names = []

university = input("University: ")
#  Enter student names
for i in range(10):
    name = input(f"Enter student name: ")
    names.append(name)

# Display student names
print("The following students attend {university}:")
for i in range(10):
    print(names[i])
