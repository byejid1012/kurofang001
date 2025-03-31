#Area Calculator

# This program calculates the area of a rectangle, triangle, and circle based on user input.
print("********")
print("""Area Calculator
      1. Rectangle
      2. Triangle
      3. Square
      4. Circle""")
choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
elif choice == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
elif choice == 3:
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area}")
elif choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius ** 2
    print(f"The area of the circle is: {area}")
else:
    print("Invalid choice! Please select a valid option.")

Letter = input("Enter a letter: ")
if Letter in "aeiou" or Letter in "AEIOU":
    print("The letter is Vowel.")
else:
    print("The letter is not Vowel.")
    