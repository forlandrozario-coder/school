side_1 = int(input("Enter the first side of the triangle : "))
side_2 = int(input("Enter the second side of the triangle : "))
side_3 = int(input("Enter the third side of the triangle : "))
if side_1 == side_2 == side_3:
    print("The triangle is an equilateral triangle.")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("The triangle is an isosceles triangle.")
elif side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
    print("The triangle is a sacalene triangle.")
