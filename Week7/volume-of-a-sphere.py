import math

def volume_of_sphere(radius):
    return (4/3) * math.pi * radius ** 3

while True:
    try:
        radius = float(input("Enter radius of sphere: "))
        if radius < 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    volume = volume_of_sphere(radius)
    print(f"Volume of sphere: {volume:.4f}")

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    if cont == "n":
        break

