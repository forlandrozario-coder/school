import math 
length = float(input("Enter the length of the wall in meters : "))
width = float(input("Enter the width of the wall in meters : "))
height = float(input("Enter the height of the wall in meters : "))
coverage_per_can = 10
total_wall_area = 2 * (length * width + length * height + width * height)
cans_needed = math.ceil(total_wall_area / coverage_per_can)
print(f"the total area of the wall is {total_wall_area:,} square meters.")
print(f"you will need {cans_needed} cans of paint to cover the wall.")
