#while
ind=1
while (ind<=20):
    print("welcome u're in while loop")
    ind+=1 #counter

#string
#name=120 #integer
name = "120" #"text"
import sys
print(type(name))

para="Hello this is My First para, Welcome and have a look"
#methods in string
print(para.lower())
print(para.upper())

#accessing characters #indexing based
print(para[11])
print(para[11:20]) #slicing
print(para[0:])
print(para[:20])
print(para[-1:-10])
print(para[:-2])
print(para[-4:])

#method
#concatenation
print(para + "     Fahh")
print("Fahh" * 5)

#in , not in
print("is" in para)
print("is" not in para)
print("Fahh"=="Far")
print("Fahh"=="Fahh")

#lexicographically- alphabetically
name1="Fahh"
name2="Farheen"
name3="Farro"
condition=name1>name2
print(condition)

#ascii code -0 -255
import string
print(string.printable)

#reverse string
name="Farheen Mujawar"
print(name)
rev=""
for i in name:
    rev+=i
    print(rev)

for i in name:
    rev=i+rev
    print(rev)

for i in name:
    rev=i+rev
print(rev)

#methods of string
print(name)

#replace
print(name.replace("Farheen","Fahh"))
name="         Farheen         "
print(name)

#to remove extra spaces
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(name.join("Farroo"))

#count
print(name.count("Farheen"))

#startswith and endswith
print(name.startswith("Far"))
print(para)
print(para.startswith("Hello"))
print(para.endswith("look"))



