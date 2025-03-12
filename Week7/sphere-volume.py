import math

def volume_of_a_sphere(radius):
    return (4/3) * math.pi * radius ** 3

while True:
  radius = float(input("Please enter the radius of the sphere: "))
  volume = volume_of_a_sphere(radius)
  print(f"The volume of the sphere is {volume:.4f}")

  cont = input("Do you want to continue? (y/n): ").strip().lower()
  if cont ==  'n':
    break


  def power(base, exponent):
      return base ** exponent

  num = power(2,5)
  print(num)