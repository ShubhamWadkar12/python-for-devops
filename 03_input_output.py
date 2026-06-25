name = input("Enter your name : ")
# print("Your name is",name, "and you are from Pune")

#String formatting
nami = f"hello dost, I am {name} and i am from pune"

"""a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(f"The addition of two numbers is {a+b}")"""

other_name = input("Enter the other name : ")
print(nami.replace("dost",other_name))

print(dir(nami))