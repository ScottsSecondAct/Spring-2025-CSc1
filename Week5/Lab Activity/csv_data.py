first_names = []
last_names = []
majors = []

count = int(input ("Enter a number greater than zero: "))
for i in range(count):
    first_name = input("Enter First Name: ")
    first_names.append(first_name)

    last_name = input("Enter Last Name: ")
    last_names.append(last_name)

    major = input("Enter Major: ")
    majors.append(major)

try:
    with open("csv_file.csv", "w") as f:
        f.write("First Name, Last Name, Major\n")
        for i in range(count):
            f.write(f"{first_names[i]},{last_names[i]},{majors[i]}\n")
except IOError as e:
    print(f"Error writing to file: {e}")
    print("Make sure the file is not open in another program.")