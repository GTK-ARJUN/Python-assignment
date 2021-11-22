# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 2. Write a Python Program to Check if a Number is Odd or Even?
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Write a Python Program to Check Leap Year?
year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# 4. Write a Python Program to Check Prime Number?
number = int(input("Enter a number: "))
for i in range(2, number):
    if number % i == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")

# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
for i in range(2, 10000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
