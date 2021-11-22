import math
# 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
#num=int(input("Enter the number of terms:"))
num = 5


def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1)+fib(n-2))


for i in range(num):
    print(fib(i))
# 2. Write a Python Program to Find Factorial of Number Using Recursion?
#num=int(input("Enter the number:"))
num = 5


def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)


print(f"Factorial of {num} is {fact(num)}")

# 3. Write a Python Program to calculate your Body Mass Index?
#weight=float(input("Enter your weight in kg:"))
#height=float(input("Enter your height in meters:"))
weight = 70
height = 1.75


def bmi(weight, height):
    return(weight/(height**2))


print(f"Your BMI is {bmi(weight,height)} Kg/m\u00b2")
# 4. Write a Python Program to calculate the natural logarithm of any number?
#num=float(input("Enter the number:"))
num = 5


def log(n):
    return(round(math.log(n), 5))


print(f"The natural logarithm of {num} is {log(num)}")

# 5. Write a Python Program for cube sum of first n natural numbers?
#num=int(input("Enter the number:"))
num = 5
sum = 0


def cube(n):
    return(n**3)


for i in range(num+1):
    sum += cube(i)
print(f"The sum of cubes of first {num} natural numbers is {sum}")
