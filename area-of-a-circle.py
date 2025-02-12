import math

large_diameter = 4
small_diameter = 2

area_of_large_circle = math.pi*(large_diameter/2)**2
area_of_small_circle = math.pi*(small_diameter/2)**2
area_of_ring = area_of_large_circle - area_of_small_circle

print(f"Diameter of large circle: {large_diameter:.2f}")
print(f"Diameter of small circle: {small_diameter:.2f}")
print(f"Area of large circle:     {area_of_large_circle:.2f}")
print(f"Area of small circle:     {area_of_small_circle:.2f}")
print(f"Area of ring:             {area_of_ring:.2f}")