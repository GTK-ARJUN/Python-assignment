"""https://drive.google.com/file/d/1GmzMWfbw9YDcAzTRsrEfKIZxBHKlEufF/view"""

"""
Question1. 
    Create a function that takes three arguments a, b, c and returns the sum of the
    numbers that are evenly divided by c from the range a, b inclusive.
"""
a, b, c = 1, 10, 2
sum = 0
for i in range(a, b+1):
    if i % c == 0:
        sum += i
print(sum)


"""
Question2. 
    Create a function that returns True if a given inequality expression 
    is correct and False otherwise.
"""
string1 = "3<7<11"


def validate(string):
    print(eval(string))


validate(string1)

"""
Question3. 
    Create a function that replaces all the vowels in a string with a specified character.
"""


string2 = "aardvark minnie mouse shakespeare"
sp_char = "*"

vowels = ['a', 'e', 'i', 'o', 'u']


def replaced_vowel(string, char):
    for i in string:
        if i in vowels:
            string = string.replace(i, char)
    print(string)


replaced_vowel(string2, sp_char)

"""
Question4. 
    Write a function that calculates the factorial of a number recursively.
"""
num = 5


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(num))

"""
Question 5
    Hamming distance is the number of characters that differ 
    between two strings.
"""
string1 = "strong"
string2 = "strung"
sum = 0
for i in range(len(string1)):
    if string1[i] != string2[i]:
        sum += 1

print(sum)
