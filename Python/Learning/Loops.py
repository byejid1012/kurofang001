#Loops
#Types of Loops
#1. For Loop: Used for iterating over a sequence (like a list, tuple, dictionary, set, or string).
#2. While Loop: Repeats as long as a certain condition is true.
#3. While True: An infinite loop that runs until a break statement is encountered.
#4. Nested Loop: A loop inside another loop.


n = 1
i = 4

#While Loop
while n <=10:
    print(n,"x", i, "=", n*i)
    n += 1
print("***************")

#While True Loop
while True:
    number1 = int(input("Enter a num1: "))
    number2 = int(input("Enter a num2: "))

    print("The sum of", number1, "and", number2, "is:", number1 + number2)
    repeat = input("Do you want to continue? (yes/no): ")
    if repeat == "no":
        break
print("***************")


#Nested Loop
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()



    