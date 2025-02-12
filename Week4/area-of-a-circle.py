import math

large_diameter = 4
small_diameter = 2

area_of_large_circle = math.pi * (large_diameter / 2) ** 2
area_of_small_circle = math.pi * (small_diameter / 2) ** 2

area_of_ring = area_of_large_circle - area_of_small_circle

print(f"Large Diameter:       {large_diameter:.2f} cm")
print(f"Small Diameter:       {small_diameter:.2f} cm")
print()
print(f"Area of Large Circle: {area_of_large_circle:.2f} cm^2")
print(f"Area of Small Circle: {area_of_small_circle:.2f} cm^2")
print(f"Area of Ring:         {area_of_ring:.2f} cm^2")

