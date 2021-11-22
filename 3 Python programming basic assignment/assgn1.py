# 1. Write a Python program to print &quot;Hello Python&quot;?
import random
print("Hello Python")

# 2. Write a Python program to do arithmetical operations addition and division.?
a = 10
b = 5
print("Addition of a and b is:", a+b)
print("Division of a and b is:", a/b)
print("Subtraction of a and b is:", a-b)
print("Multiplication of a and b is:", a*b)

# 3. Write a Python program to find the area of a triangle?
base = 10
height = 5

# comment above base and height and uncomment below to find area of triangle if you want to take input from user
#base=float(input("Enter the base of triangle:"))
#height=float(input("Enter the height of triangle:"))

area_triangle = 0.5*base*height
print("Area of triangle is:", area_triangle)

# 4. Write a Python program to swap two variables?
i = input("Enter the first variable i :")
j = input("Enter the second variable j :")
i, j = j, i

print(f"After swapping:{i,j}")

# 5. Write a Python program to generate a random number?
print(random.randint(1, 10))
