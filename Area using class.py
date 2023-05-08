import math


def get_float_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid input, please enter a number")
            continue


class Shape:
    def __init__(self, shape):
        self.shape = shape.lower()

    def calculate_area_perimeter(self):
        if self.shape == "rectangle":
            length = get_float_input("Enter length: ")
            width = get_float_input("Enter width: ")
            if length is not None and width is not None:
                area = length * width
                perimeter = 2 * (length + width)
                print("The area:", area)
                print("The perimeter :", perimeter)

        elif self.shape == "square":
            side = get_float_input("Enter the side : ")
            if side is not None:
                area = side * side
                perimeter = 4 * side
                print("The area :", area)
                print("The perimeter :", perimeter)

        elif self.shape == "circle":
            radius = get_float_input("Enter the radius: ")
            if radius is not None:
                area = math.pi * radius * radius
                perimeter = 2 * math.pi * radius
                print("The area :", area)
                print("The circumference:", perimeter)

        else:
            print("Invalid shape entered")


shape = Shape(input("Enter the shape (rectangle, square, circle): "))
shape.calculate_area_perimeter()
