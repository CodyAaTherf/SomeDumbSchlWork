# import math

# choice = str(input(
#     "What do you want to do? \n" \
#     "A. Calculate the Area of a Circle. \n" \
#     "B. Calculate the Area of a Rectangle \n" \
#     "C. Calculate the Area of a Square: "
# ))
# print("What do you want to do?")


# if choice == "A" or "a":
#     a_pi = math.pi
#     # a_c = str(input("Is the value in Diameter or Radius: "))
#     # if a_c == "Diameter" or "diameter":
#     #     a_diameter = float(input("Enter the diameter of the circle: "))
#     #     a_dia_calc = (pi * (a_diameter ^2))/4
#     #     print("Area = {0}".format)
#     a_r = float(input("Enter the Radius of the circle: "))
#     a_circ = a_pi * a_r * a_r
#     print("Area of the circle %.2f" %a_circ)
# elif choice == "B" or "b":
#     b_length = float(input("Enter the length of the Rectangle: "))
#     b_height = float(input("Enter the height of the Rectangle: "))
#     b_area = b_length * b_height
#     print("Area of the Rectange is %.2f" %b_area)
# elif choice == "C" or "c":
#     print("do something c")

print("1. Circle")
print("2. Square")
print("3. Rectangle")
number = int(input("Which shape do you want to calculate the area of: "))

if number == 1:
    radius = int(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    print(f"The area of circle is {area}")
elif number == 2:
    side = int(input("Enter the side of the square: "))
    area = side * side
    print(f"The area of the square is {area}")
elif number == 3:
    b = int(input("Enter the breadth of rectangle: "))
    l = int(input("Enter the length of rectangle: "))
    area = b * l
    print(f"The area of rectangle is {area}")
else:
    print("Please enter a valid number!")
