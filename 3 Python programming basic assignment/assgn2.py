# 1. Write a Python program to convert kilometers to miles?
import math
import datetime
km = float(input("Enter the distance in kilometers: "))
miles = km/1.609
print(f"The distance in miles is: {miles}")

# 2. Write a Python program to convert Celsius to Fahrenheit?
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius*1.8+32
print(f"The temperature in Fahrenheit is: {fahrenheit}")

# 3. Write a Python program to display calendar?
print(datetime.datetime.now().strftime("%A, %B %d, %Y"))

# 4. Write a Python program to solve quadratic equation?
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = b**2-4*a*c
if d > 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(f"The roots are {x1} and {x2}")
elif d == 0:
    x = -b/(2*a)
    print(f"The roots are {x}")
else:
    print("The equation has no real roots")


# 5. Write a Python program to swap two variables without temp variable?
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a, b = b, a
print(f"The value of a is: {a}")
print(f"The value of b is: {b}")
