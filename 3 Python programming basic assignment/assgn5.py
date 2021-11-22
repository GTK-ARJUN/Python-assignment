# 1. Write a Python Program to Find LCM?
#n1 = int(input("Enter the first number: "))
#n2 = int(input("Enter the second number: "))
n1, n2 = 12, 15
if n1 > n2:
    greater = n1
else:
    greater = n2

while(True):
    if((greater % n1 == 0) and (greater % n2 == 0)):
        lcm = greater
        break
    greater += 1

print("The LCM of", n1, "and", n2, "is", lcm)

# 2. Write a Python Program to Find HCF?
#n1 = int(input("Enter the first number: "))
#n2 = int(input("Enter the second number: "))
n1, n2 = 12, 15
if n1 > n2:
    smaller = n2
else:
    smaller = n1

for i in range(1, smaller + 1):
    if((n1 % i == 0) and (n2 % i == 0)):
        hcf = i

print("The HCF of", n1, "and", n2, "is", hcf)

# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
#number = int(input("Enter the number: "))
number = 10
print(f"Input number is {number} ")
print(f"Binary = {bin(number)}")
print(f"Octal = {oct(number)}")
print(f"Hexadecimal = {hex(number)}")

# 4. Write a Python Program To Find ASCII value of a character?
#ch = input("Enter the character: ")
ch = 'a'
print(f"The ASCII value of {ch} is {ord(ch)}")
# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif choice == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif choice == 3:
    print(num1, "*", num2, "=", num1 * num2)
elif choice == 4:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid input")
