# Bits and Bytes
# Packages and Libraries
# Data Types: int, float, string, list

# Import sys package
import sys

age = 20

# Checking capacity of integer container
print(f"The size of int is {sys.getsizeof(age)} bytes")  # Output: size of int

# 1 byte = 8 bits, 28 bytes = 224 bits, approximately for 9/10 digits

name = "Sana"
print(f"The size of string is {sys.getsizeof(name)} bytes")  # Fixed from 'string' to 'name'

# Checking size of float
float_num = 2.5  # Avoid using 'float' as a variable name since it's a built-in type
print(f"The size of float is {sys.getsizeof(float_num)} bytes")  # Output: size of float

# Checking size of list
my_list = [1, 2, 3, 4]  # Avoid using 'list' as a variable name since it's a built-in type
print(f"The size of list is {sys.getsizeof(my_list)} bytes")  # Output: size of list

# Checking size of boolean
boolean = True
print(f"The size of boolean is {sys.getsizeof(boolean)} bytes")  # Output: size of boolean

# Additional variable examples
address = 104
name = 5  # Note: this overwrites the previous value of 'name'

# To check the type of a container/variable
print(type(address))  # Output: <class 'int'>
print(type(name))  # Output: <class 'int'>

# Reassigning float variable
float_num = 2.7  # Avoid using 'float' as a variable name
print(type(float_num))  # Output: <class 'float'>

# String example
string = "Tara"
print(type(string))  # Output: <class 'str'>

# Complex number example
z = 5 + 6j
print("Real part is:", z.real)  # Output: Real part
print("Imaginary part is:", z.imag)  # Corrected from 'img' to 'imag'
