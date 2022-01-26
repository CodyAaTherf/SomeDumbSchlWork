import math

choice = input(
    "What do you want to do? \n" \
    "A. Calculate the Area of a Circle. \n" \
    "B. Calculate the Area of a Rectangle \n" \
    "C. Calculate the Area of a Square: "
)

if choice == "A" or "a":
    a_pi = math.pi
    # a_c = str(input("Is the value in Diameter or Radius: "))
    # if a_c == "Diameter" or "diameter":
    #     a_diameter = float(input("Enter the diameter of the circle: "))
    #     a_dia_calc = (pi * (a_diameter ^2))/4
    #     print("Area = {0}".format)
    a_r = float(input("Enter the Radius of the circle: "))
    a_circ = a_pi * a_r * a_r
    print("Area of the circle %.2f" %a_circ)
elif choice == "B" or "b":
    print("something for b")
elif choice == "C" or "c":
    print("do something c")