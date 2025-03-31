#Conditioannal Statement
# if, elif, else

marks = int(input("Enter your marks: "))
if marks >=90:
    print('Grade A, you will get 100% scholarship')
elif marks >=80 and marks <90:
    print('Grade B, you will get 50% scholarship')
elif marks >=70 and marks <80:
    print('Grade C, you will get 25% scholarship')
elif marks >=60 and marks <70:
    print('Grade D, you will get 10% scholarship')
else:
    print('Grade B, you will not get a scholarship')



#Nested if statement
if marks >=90 and marks <95:
    print('You will get iPhone 13')
    if marks >=95:
        print('You will get iPhone 14 Pro Max')
else:
        print('You will Not get any phone')


#SHORT HAND IF STATEMENT
if marks >=95: print('You will get iPhone 14 Pro Max')

#SHORT HAND IF ELSE STATEMENT
print('you are genius') if marks >=95 and marks else print('You are not genius')


#Problem Solving

# 1. Write a program to check if a number is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
    