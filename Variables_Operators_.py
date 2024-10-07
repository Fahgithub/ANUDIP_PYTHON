# Arithmetic operators
a = 10
b = 5
x = 5

# Naming convention
user_id = 101
user_name = 'Farheen'
designation = ""

# CamelCase
totalAmount = 200
userName = ''

# Valid variable names
id9 = 12
_id = 12
id_ = 13

# Sum example
num_1 = 2
num_2 = 5
summation = num_1 + num_2
print(summation)  # Output: 7

# Mathematical operators: +, -, *, /, %, **, //
num1 = 10
num2 = 2
print(num1 / num2)  # Output: 5.0
print(num1 // num2)  # Output: 5
print(10 // 3)  # Output: 3 (floor value)
print(10 / 3)  # Output: 3.3333333333333335
print(2 ** 2)  # Output: 4
print(2 ** 3)  # Output: 8

# Comparison operators: <, >, <=, >=, ==, !=
num1 = 20
num2 = 100
is_equal = (num1 == num2)
print(is_equal)  # Output: False
print(num1 > num2)  # Output: False
print(num1 < num2)  # Output: True
print(num1 != num2)  # Output: True

# Logical operators: and, or, not
print(num1 == 20 and num2 == 50)  # Output: False
print(num1 == 20 and num2 == 100)  # Output: True
print(num1 == 20 or num2 == 50)  # Output: True
print(not True)  # Output: False

# Assignment operators: +=, -=, *=, /=, //=
num1 = 10
num2 = 20
num1 += num2
print(num1)  # Output: 30
num1 -= num2
print(num1)  # Output: 10
num1 *= num2
print(num1)  # Output: 200
num1 /= num2
print(num1)  # Output: 10.0
num1 //= num2
print(num1)  # Output: 0.0

# Identity operators: is, is not
print(5 is 5)  # Output: True
print("Fahh" is "Farheen")  # Output: False
print("Fahh" is "Fahh")  # Output: True

# Membership operators: in, not in
names_list = ["Ram", "seta", "Raju", "sonu"]
is_present = "Ram" in names_list
print(is_present)  # Output: True
print("Tara" in names_list)  # Output: False
print("Tara" not in names_list)  # Output: True
