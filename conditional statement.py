#statement: print, expression, input, conditional statement
#condition : login-> userid and password
#if else
#login
#username and password -> if correct ->dashboard
#-> if not -> error
#Login page example
name= input("enter username for login :")
password =input("Enter your password :")
if(name == "Fahh" and password== "12345"):
    print(f"Welcome {name}")
else:
    print("Invalid")
print("-------------------------------------------")

num=int(input("Enter number:"))
if num>10:
    print("greater")
else:
    print("smaller")

print("----------Guess the number---------------------------------")

num=int(input("Enter number:"))
if num==0:
    print("It is not zero")
elif num > 10:
    print("Greater, please try again")
elif num < 10:
    print("Smaller, please try again")
elif num == 10:
    print("You Won")
else:
    print("Please try again")

print("----------Even or Odd---------------------------------")

num=int(input("Enter number:"))
if num%2==0:
    print("It is Even")
else:
    print("It is Odd")

print("----------Even or Odd---------------------------------")
#for loop- limit/range defined

for num in range(1,100):
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


