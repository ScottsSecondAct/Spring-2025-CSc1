names = []
university = input("University: ")
for i in range(10):
    name = input(f"Enter student name: ")
    names.append(name)
print("The following students attend {university}:")
for i in range(10):
    print(names[i])