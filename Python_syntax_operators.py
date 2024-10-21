# Operators - Arithmetic
a = 10
b = 5
x = 5

# Naming conventions
user_id = 101
user_name = 'Farheen'
designation = ""
total_amount = 200  # using snake_case
user_name_camel = ''  # using camelCase

# Variable names cannot start with a digit
# 9id = 10  # invalid syntax
id9 = 12  # valid syntax
_id = 12
id_ = 13

# Variables can contain letters, numbers, and underscores, but cannot start with a number
num_1 = 2
num_2 = 5
summation = num_1 + num_2
print(summation)  # Output: 7

# Keywords are reserved words in Python and cannot be used as variable names
# if = 12  # invalid syntax

student_name = ""
std_id = 10
is_valid = 1
has_id = 10
login_attempt = []  # defining an empty list
city_list = []
max_marks = 120
maximum_marks = 120  # correct way to write a variable

# Rules for declaring variables
# pin-code, pinCode, first-name: firstName

# Operators
# Mathematical: +, -, *, /, %, **, //
num1 = 10
num2 = 2
print(num1 / num2)  # Output: 5.0
print(num1 // num2)  # Output: 5
print(10 // 3)  # Output: 3 (floor value)
print(10 / 3)  # Output: 3.3333333333333335
print(2 ** 2)  # Output: 4 (exponential/power)
print(2 ** 3)  # Output: 8

# Comparison operators: <, >, <=, >=, ==, !=
num1 = 20
num2 = 100
is_equal = (num1 == num2)  # Comparison should use '=='
print(is_equal)  # Output: False
print(num1 > num2)  # Output: False
print(num1 < num2)  # Output: True
print(num1 != num2)  # Output: True

# Logical operators: and, or, not (negation)
print(num1 == 20 and num2 == 50)  # Output: False
print(num1 == 20 and num2 == 100)  # Output: True
print(num1 == 20 or num2 == 50)  # Output: True
print(not True)  # Output: False

# Assignment operators
num1 = 10
num2 = 20
num3 = num2 + num1
num1 += num2  # Equivalent to num1 = num1 + num2
print(num1)  # Output: 30
num1 -= num2  # Equivalent to num1 = num1 - num2
print(num1)  # Output: 10
num1 *= num2  # Equivalent to num1 = num1 * num2
print(num1)  # Output: 200
num1 /= num2  # Equivalent to num1 = num1 / num2
print(num1)  # Output: 10.0
num1 //= num2  # Equivalent to num1 = num1 // num2
print(num1)  # Output: 0.0

# Demonstrating variable assignment and incrementing
x = 6
x + 2  # This does not change x
print(x)  # Output: 6
x = x + 2  # This changes x
print(x)  # Output: 8
x += 2  # Another way to increment x
print(x)  # Output: 10

# Identity operators: is, is not
print(5 is 5)  # Output: True
print("Fahh" is "Farheen")  # Output: False
print("Fahh" is "Fahh")  # Output: True

# Membership operators: in, not in
names_list = ["Ram", "Seeta", "Raju", "Sonu"]
is_present = "Ram" in names_list
print(is_present)  # Output: True
print("Tara" in names_list)  # Output: False
print("Tara" not in names_list)  # Output: True

