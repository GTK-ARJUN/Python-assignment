"""https://drive.google.com/file/d/1Yg8d2Hj-LtWp0JrJOcuPuPZQswOqwe-U/view"""
"""
Question 1:
    Please write a program using generator to print the numbers which can be divisible 
    by 5 and 7 between 0 and n in comma separated form while n is input by console.
    Example:
    If the following n is given as input to the program:
    100
    Then, the output of the program should be:
    0,35,70
"""
#num1=int(input("Enter the number: "))
num1 = 100


def divisible_by_5_and_7(num1):
    for i in range(num1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


for i in divisible_by_5_and_7(num1):
    print(i, end=",")

print("\n")
"""
Question 2:
    Please write a program using generator to print the even numbers between 
    0 and n in comma separated form while n is input by console.
    Example:
    If the following n is given as input to the program:
    10
    Then, the output of the program should be:
    0,2,4,6,8,10
"""
num2 = 10


def even_num(num2):
    for i in range(num2):
        if i % 2 == 0:
            yield i


values = even_num(num2)
for i in values:
    print(i, end=",")


print("\n")

"""
Question 3:
    The Fibonacci Sequence is computed based on the following formula:
    f(n)=0 if n=0
    f(n)=1 if n=1
    f(n)=f(n-1)+f(n-2) if n&gt;1
    Please write a program using list comprehension to print the Fibonacci Sequence in comma
    separated form with a given n input by console.
    Example:
    If the following n is given as input to the program:
    7

    Then, the output of the program should be:
    0,1,1,2,3,5,8,13
"""
num3 = 7
fib_Ser=[]
for i in range(num3+1):
    if i == 0:
        fib_Ser.append(0)
    elif i == 1:
        fib_Ser.append(1)
    else:
        fib_Ser.append(fib_Ser[i-1] + fib_Ser[i-2])

print(str(fib_Ser).strip("[]"))


"""
Question 4:
    Assuming that we have some email addresses in the ;username@companyname.com; format,
    please write program to print the user name of a given email address. Both user names and
    company names are composed of letters only.
    Example:
    If the following email address is given as input to the program:
    john@google.com
    Then, the output of the program should be:
    john
"""
#email=input("Enter the email address: ")
email="john@google.com"
email=email.split("@")
print(email[0])

"""
Question 5:
    Define a class named Shape and its subclass Square. The Square class has an init function
    which takes a length as argument. Both classes have a area function which can print the area
    of the shape where Shape&#39;s area is 0 by default.
"""
class Shape:
    def __init__(self):
        pass
    
    class Square:
        def __init__(self, length):
            self.length = length
        def area(self):
            return self.length**2   

print(Shape.Square(4).area())

