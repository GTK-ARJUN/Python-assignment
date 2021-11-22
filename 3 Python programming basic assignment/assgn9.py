"""https://drive.google.com/file/d/1hdUGW5tzH08haEyPq8ttmK16I5POSlqp/view"""
# 1. Write a Python program to check if the given number is a Disarium Number?
#num = int(input("Enter a number: "))
num = 135
sum = 0

for i in range(len(str(num))):
    sum += int(str(num)[i])**(i+1)
if num == sum:
    print(f" {num} is a Disarium")
else:
    print(f" {num} is not a Disarium")

# 2. Write a Python program to print all disarium numbers between 1 to 100?


def disarium(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i])**(i+1)
    if num == sum:
        print(f" {num} is a Disarium")


for i in range(1, 101):
    disarium(i)

# 3. Write a Python program to check if the given number is Happy Number?
#num3=int(input("Enter a number to check happy or not : "))
num3 = 19
while len(str(num3)) > 1:
    sum = 0
    for i in range(len(str(num3))):
        sum += int(str(num3)[i])**2
    num3 = sum

if num3 == 1:
    print(f" {num3} is a Happy Number")
else:
    print(f" {num3} is not a Happy Number")

# 4. Write a Python program to print all happy numbers between 1 and 100?


def happy(num):
    happy_num = num
    while len(str(num)) > 1:
        sum = 0
        for i in range(len(str(num))):
            sum += int(str(num)[i])**2
        num = sum
    if num == 1:
        print(f" {happy_num} is a Happy Number")


for i in range(1, 101):
    happy(i)

print("*"*10)
# 5. Write a Python program to determine whether the given number is a Harshad Number?
#num5=int(input("Enter a number to check harshad or not : "))
num5 = 408
sum = 0
for i in range(len(str(num5))):
    sum += int(str(num5)[i])

harshad_number = num5/sum
print(f" {harshad_number} is a Harshad Number for {num5}")
print("*"*10)
# 6. Write a Python program to print all pronic numbers between 1 and 100?
print("Pronic Numbers between 1 to 100")
flag = 1
while flag == 1:
    for i in range(1, 101):
        pronic_number = i*(i+1)
        if pronic_number > 100:
            flag = 0
            break
        print(f" {pronic_number} ")
