"""https://drive.google.com/file/d/1JS8JSCU--7YcoTZcvYPpn-hR2--sFBBC/view?usp=sharing"""
"""
Question 1:
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30. D is the variable whose values should
    be input to your program in a comma-separated sequence.
"""

#values=input("Enter the value of C: ")
import numpy as np
C, H = 50, 30
values = """100,150,180"""
values = [int(i) for i in values.replace(" ", "").split(",")]
print(values)


def def_func(i):
    Q = (2*C*i)/H
    Q = Q**0.5
    return int(Q)


op = []
for i in values:
    op.append(def_func(i))

op = str(op).replace(" ", "")
print(op)

"""
Question 2:
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
    element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡Y-1.
"""
num1, num2 = 3, 5
mat1 = np.zeros([num1, num2])

for i in range(num1):
    for j in range(num2):
        mat1[i][j] = i*j

print(mat1)


"""
Question 3:
    Write a program that accepts a comma separated sequence of words as input and prints the
    words in a comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
    without,hello,bag,world
    Then, the output should be:
    bag,hello,without,world
"""

string1 = """without,hello,bag,world"""
string1 = string1.replace(" ", "").split(",")
string1.sort()
string1 = ",".join(string1)
print(string1)

"""
Question 4:
    Write a program that accepts a sequence of whitespace separated words as input and prints
    the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and hello world again
    Then, the output should be:
    again and hello makes perfect practice world
"""
string1 = """hello world and practice makes perfect and hello world again"""
string1 = string1.split(" ")
string1.sort()
string1 = " ".join(string1)
print(string1)

"""
Question 5:
    Write a program that accepts a sentence and calculate the number of letters and digits.
    Suppose the following input is supplied to the program:
    hello world! 123
    Then, the output should be:
    LETTERS 10  DIGITS 3
"""

string5 = """hello world! 123"""
LETTERS, DIGITS = 0, 0

for i in string5:
    if i.isdigit():
        DIGITS += 1
    elif i.isalpha():
        LETTERS += 1
print(f"{LETTERS=}")
print(f"{DIGITS=}")


"""
Question 6:
    A website requires the users to input username and password to register. Write a program to
    check the validity of password input by users.
    Following are the criteria for checking the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
"""
#pass_list=input("Enter the password list: ")
pass_list = """ABd1234@1,a F1#,2w3E*,2We3345"""


def password_checker(string6):
    flag = [0, 0, 0, 0]  # easch element represent one criteria of the password
    if len(string6) >= 6 and len(string6) <= 12:
        for i in string6:
            if i.isdigit():
                flag[1] = 1
            elif i.islower():
                flag[0] = 1
            elif i.isupper():
                flag[2] = 1
            elif i in ['$', '#', '@']:
                flag[3] = 1
    if sum(flag) == 4:
        print(string6)


pass_list = pass_list.split(",")
for j in pass_list:
    password_checker(j)
