Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Assignment Operators
#(+=,-=,*=,/=,//=,**=,%=
x=5
>>> x+=2
>>> print(x)
7
>>> x-=
SyntaxError: incomplete input
>>> x-=2
>>> print(x)
5
>>> x*=5
>>> print(x)
25
>>> x/=5
>>> print(x)
5.0
>>> x//=5
>>> print(x)
1.0
>>> x=8
>>> x%=4
>>> print(x)
0
>>> x=9
>>> print(x)
9
>>> x=5
>>> x**=6
>>> print(x)
15625
>>> 
>>> 
>>> 
>>> 
>>> x=15
>>> y=10
>>> addition=x+y
>>> subtraction=x-y
>>> division=x/y
>>> multiplication=x*y
>>> modulus=x%y
>>> exponentiation=x**y
>>> floor_division=x//y
print(addition)
25
print(subtraction)
5
print(DIVISION)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(DIVISION)
NameError: name 'DIVISION' is not defined
print(division)
1.5
print(multiplication)
150
print(modulus)
5
print(exponentiation)
576650390625
print(floor_division)
1
#membership operator (in, not in)
#declare list
names=["Ram","Shyam","Seeta","Geeta"]
#declare string
in_list=
SyntaxError: incomplete input
name_in_list="Ram" in names
print(name_in_list)
True
name_not_in_list="Damu" not in names
print(name_not_in_list)
True




import math
def calculate_area(radius):
    area=math.pi*radius**2
    return area

radius= float(input("Enter the radius of the circle:"))
Enter the radius of the circle:2
area=calculate_area(radius)
print(f"The area of the circle with radius{radius}is:{area}")
The area of the circle with radius2.0is:12.566370614359172


def calculate_area(base, height):
    area = 0.5 * base * height  # Using the formula: 1/2 * base * height
    return area
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
SyntaxError: invalid syntax
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
SyntaxError: multiple statements found while compiling a single statement
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
SyntaxError: multiple statements found while compiling a single statement
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    
SyntaxError: unexpected indent
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
SyntaxError: multiple statements found while compiling a single statement
base = float(input("Enter the base of the triangle: "))
Enter the base of the triangle: 
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    base = float(input("Enter the base of the triangle: "))
ValueError: could not convert string to float: ''



def calculate_area(base, height):
    area = 0.5 * base * height  # Using the formula: 1/2 * base * height
    return area
base = float(input("Enter the base of the triangle: "))
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
base = float(input("Enter the base of the triangle: "))
Enter the base of the triangle: 5
height = float(input("Enter the height of the triangle: "))
Enter the height of the triangle: 7
area = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is: {area}")
The area of the triangle with base 5.0 and height 7.0 is: 17.5





def calculate_area(length, width):
    area = length * width  # Using the formula: length * width
    return area
length = float(input("Enter the length of the rectangle: "))
SyntaxError: invalid syntax
length = float(input("Enter the length of the rectangle: "))
Enter the length of the rectangle: 8
width = float(input("Enter the width of the rectangle: "))
Enter the width of the rectangle: 6
area = calculate_area(length, width)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    area = calculate_area(length, width)
TypeError: calculate_area() takes 1 positional argument but 2 were given
area = calculate_area(length, width)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    area = calculate_area(length, width)
TypeError: calculate_area() takes 1 positional argument but 2 were given



def calculate_area(length, width):
    area = length * width  # Using the formula: length * width
    return area

# Input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = calculate_area(length, width)

# Output the result
print(f"The area of the rectangle with length {length} and width {width} is: {area}")
SyntaxError: invalid syntax

def calculate_area(length, width):
    area = length * width  # Using the formula: length * width
    return area
length = float(input("Enter the length of the rectangle: "))
SyntaxError: invalid syntax
length = float(input("Enter the length of the rectangle: "))
