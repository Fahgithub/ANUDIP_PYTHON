# Assignment Operators
# (+=, -=, *=, /=, //=, **=, %=)
x = 5
x += 2
print(x)  # Output: 7

x -= 2
print(x)  # Output: 5

x *= 5
print(x)  # Output: 25

x /= 5
print(x)  # Output: 5.0

x //= 5
print(x)  # Output: 1.0

x = 8
x %= 4
print(x)  # Output: 0

x = 9
print(x)  # Output: 9

x = 5
x **= 6
print(x)  # Output: 15625

# Performing basic arithmetic operations
x = 15
y = 10
addition = x + y
subtraction = x - y
division = x / y
multiplication = x * y
modulus = x % y
exponentiation = x ** y
floor_division = x // y

print(addition)          # Output: 25
print(subtraction)       # Output: 5
print(division)          # Output: 1.5
print(multiplication)    # Output: 150
print(modulus)           # Output: 5
print(exponentiation)    # Output: 576650390625
print(floor_division)    # Output: 1

# Membership operators (in, not in)
# Declare list
names = ["Ram", "Shyam", "Seeta", "Geeta"]

# Check membership
name_in_list = "Ram" in names
print(name_in_list)  # Output: True

name_not_in_list = "Damu" not in names
print(name_not_in_list)  # Output: True

# Function to calculate the area of a circle
import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_area_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")

# Function to calculate the area of a triangle
def calculate_area_triangle(base, height):
    area = 0.5 * base * height  # Using the formula: 1/2 * base * height
    return area

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = calculate_area_triangle(base, height)
print(f"The area of the triangle with base {base} and height {height} is: {area}")

# Function to calculate the area of a rectangle
def calculate_area_rectangle(length, width):
    area = length * width  # Using the formula: length * width
    return area

# Input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_area_rectangle(length, width)

# Output the result
print(f"The area of the rectangle with length {length} and width {width} is: {area}")
