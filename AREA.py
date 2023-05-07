import math


# function to calculate the area and perimeter of a rectangle
def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# function to calculate the area and perimeter of a square
def square_area_perimeter(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter


# function to calculate the area and perimeter of a circle
def circle_area_perimeter(radius):
    area = math.pi * radius * radius
    perimeter = 2 * math.pi * radius
    return area, perimeter


# function to correct input strings
def correct_input_string(string):
    string = string.lower().strip()
    return string


# function to correct input numbers
def correct_input_number(num):
    try:
        num = float(num)
        return num
    except ValueError:
        print("Invalid input, please enter a number")
        return None


# main function
def main():
    shape = input("Enter the shape (rectangle, square, circle): ")
    shape = correct_input_string(shape)

    if shape == "rectangle":
        length = input('Enter the length: ')
        length = correct_input_number(length)
        width = input("Enter the width: ")
        width = correct_input_number(width)

        if length is not None and width is not None:
            area, perimeter = rectangle_area_perimeter(length, width)
            print("The area:", area)
            print("The perimeter:", perimeter)

    elif shape == "square":
        side = input("Enter the side of the square: ")
        side = correct_input_number(side)

        if side is not None:
            area, perimeter = square_area_perimeter(side)
            print("The area :", area)
            print("The perimeter:", perimeter)

    elif shape == "circle":
        radius = input("Enter the radius of the circle: ")
        radius = correct_input_number(radius)

        if radius is not None:
            area, perimeter = circle_area_perimeter(radius)
            print("The area is:", area)
            print("The circumference of the circle is:", perimeter)

    else:
        print("Invalid shape entered")


# calling the main function
main()
