name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
print(name)
print(age)
print(height)
print("Your name is", name, "and your age is", age, "and your height is", height, "cm.")   

exp1 = eval(input("Enter an expression: "))
print("The result of the expression is:", exp1)

#Implicit Type Casting 
name = "Ronnie"
print(type(name))

#Explicit Type Casting
a = 12
b = 23.4
c = "Ronnie1012"  # Assigning a string value to c

print(type(a), type(b), type(c))

d = a + b
print(d)
print(type(d))


b = int(b)  # Explicitly converting b to an integer
print(type(b))  
