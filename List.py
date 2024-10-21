# Defining individual scores
s1 = 100
s2 = 200
s3 = 100
s4 = 150
s5 = 80

# Correct way to store data in a list (ordered, mutable)
marksOfStudents = [100, 200, 100, 150, 80]
print(marksOfStudents)  # Output: [100, 200, 100, 150, 80]

# Updating values (lists are mutable, index-based)
marksOfStudents[1] = 158  # Changing the second student's marks
print(marksOfStudents)  # Output: [100, 158, 100, 150, 80]

# Accessing elements
print(marksOfStudents[4])  # Output: 80 (marks of the 5th student)

# Slicing
print(marksOfStudents[:4])  # Output: [100, 158, 100, 150]

# Updating another student's marks
marksOfStudents[4] = 90  # Changing marks at the 5th index
print(marksOfStudents)  # Output: [100, 158, 100, 150, 90]

# List methods
# Checking the length of the list
length = len(marksOfStudents)
print(length)  # Output: 5

# Appending a new value at the end
marksOfStudents.append(160)
print(marksOfStudents)  # Output: [100, 158, 100, 150, 90, 160]

# Inserting a value at the 0th index
marksOfStudents.insert(0, 122)
print(marksOfStudents)  # Output: [122, 100, 158, 100, 150, 90, 160]

# Removing a specific value
marksOfStudents.remove(90)  # Removes the value 90
print(marksOfStudents)  # Output: [122, 100, 158, 100, 150, 160]

# Deleting using index
marksOfStudents.pop(4)  # Removes the element at index 4
print(marksOfStudents)  # Output: [122, 100, 158, 100, 160]

# Counting occurrences of a value
total = marksOfStudents.count(100)
print(total)  # Output: 2 (the number 100 appears twice)

# Checking the index of a value
print(marksOfStudents.index(158))  # Output: 2
print(marksOfStudents.index(160))  # Output: 4

# Sorting the list
marksOfStudents.sort()
print(marksOfStudents)  # Output: [100, 100, 122, 158, 160]

# Reversing the list
marksOfStudents.reverse()
print(marksOfStudents)  # Output: [160, 158, 122, 100, 100]

# Copying the list (returns a shallow copy)
marksOfStudents.copy()
print(marksOfStudents)  # Output: [160, 158, 122, 100, 100]

# Iterating over the list
for i in marksOfStudents:
    print(f"The element is {i}")

# Another iteration example
for i in marksOfStudents:
    print(i)

# Different types of lists
# List of strings
li1 = ["Fahh", "Far"]

# List of floats
li2 = [12.3, 7.7]

# List of booleans
li3 = [True, False]

# Mixed type list
li4 = [1, "Hasina", 4.5, True, 'V']
