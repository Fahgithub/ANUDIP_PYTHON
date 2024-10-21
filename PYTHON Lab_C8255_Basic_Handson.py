import sys

# Print "Hello World"
print("Hello World")

# Define variables of different types
a = 1                    # Integer
b = 1.5                  # Float
c = "FARHEEN"            # String
d = 5 + 6j               # Complex number
e = {"Dad", "Mom", "sibling", "cousin"}  # Set
f = ["Sefali", 3, 4.5, 4 + 5j]  # List
g = True                 # Boolean
h = ("Darvin", 4)        # Tuple
i = {'Daisy': 'name', 'Laura': 4, 'Aisha': 4.5, 'Fahh': 'cool'}  # Dictionary

# Print the type of each variable
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'complex'>
print(type(e))  # <class 'set'>
print(type(f))  # <class 'list'>
print(type(g))  # <class 'bool'>
print(type(h))  # <class 'tuple'>
print(type(i))  # <class 'dict'>

# Print the size of each variable
print(f"The size of a is {sys.getsizeof(a)} bytes")  # Size of integer
print(f"The size of b is {sys.getsizeof(b)} bytes")  # Size of float
print(f"The size of c is {sys.getsizeof(c)} bytes")  # Size of string
print(f"The size of d is {sys.getsizeof(d)} bytes")  # Size of complex
print(f"The size of e is {sys.getsizeof(e)} bytes")  # Size of set
print(f"The size of f is {sys.getsizeof(f)} bytes")  # Size of list
print(f"The size of g is {sys.getsizeof(g)} bytes")  # Size of boolean
print(f"The size of h is {sys.getsizeof(h)} bytes")  # Size of tuple
print(f"The size of i is {sys.getsizeof(i)} bytes")  # Size of dictionary

# Demonstrating boolean type
a = True
b = False
print(f"The size of a (True) is {sys.getsizeof(a)} bytes")  # Size of True
print(f"The size of b (False) is {sys.getsizeof(b)} bytes") # Size of False

# Working with complex numbers
a = 5 + 3j
b = 25 + 45j
print(a.real)  # Output: 5.0
print(b.imag)  # Output: 45.0
