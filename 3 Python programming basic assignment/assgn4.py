# 1. Write a Python Program to Find the Factorial of a Number?
number1 = 5  # int(input("Enter the number:"))
factorial = 1
for i in range(1, number1+1):
    factorial = factorial*i
print("Factorial of the number is:", factorial)


# 2. Write a Python Program to Display the multiplication Table?
num = 5
#num=int(input("Enter the number for multiplication table:"))
print(f'multiplication table of {num}')
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")

# 3. Write a Python Program to Print the Fibonacci sequence?
nterms = 10
#nterms = int(input("How many terms? "))
# first two terms
n1 = 0
n2 = 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

# 4. Write a Python Program to Check Armstrong Number?
num = 153
#num=int(input("Enter the number:"))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum+digit**3
    temp = temp//10
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")


# 5. Write a Python Program to Find Armstrong Number in an Interval?
lower = 100
upper = 1000
#lower=int(input("Enter the lower limit:"))
#upper=int(input("Enter the upper limit:"))
for num in range(lower, upper+1):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum+digit**3
        temp = temp//10
    if num == sum:
        print(num)

# 6. Write a Python Program to Find the Sum of Natural Numbers?
n = 6
#n=int(input("Enter the number:"))
sum = 0
for i in range(1, n+1):
    sum = sum+i
print(f"Sum of natural numbers upto {n} is:", sum)
