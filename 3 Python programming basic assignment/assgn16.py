"""https://drive.google.com/file/d/1uNLLFb5QaW2W_LzdoUii48gb7CM0sOEN/view"""

"""
Question1.
    Write a function that stutters a word as if someone is struggling to read it. 
    The first two letters are repeated twice with an ellipsis ... and space after 
    each, and then the word is pronounced with a question mark ?.
"""
word = "incredible"


def stutter(word):
    return (word[:2]+"..."+word[:2]+"..."+word[2:]+"?")


print(stutter(word))

"""
Question 2.
    Create a function that takes an angle in radians and returns the 
    corresponding angle in degrees rounded to one decimal place.
"""
radians = 1


def degree(num):
    return round(num*180/3.14159, 1)


print(degree(radians))

"""
Question 3. 
    In this challenge, establish if a given integer num is a Curzon number. 
    If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied 
    by num, then num is a Curzon number. Given a non-negative integer num, 
    implement a function that returns True if num is a Curzon number, or False
    otherwise.
"""
num = 5


def curzon(num):
    num = 1+2**num
    den = 1+2*num
    if num//den == 0:
        print("Curzon number")
    else:
        print("Not a Curzon number")


curzon(num)

"""
Question 4.
    Given the side length x find the area of a hexagon.
"""
#s=float(input("Enter the side length of the hexagon: "))
s = 2
A = round((3*(3**0.5)*s**2)/2, 1)
print(A)

print("\n")
"""
Question 5. 
    Create a function that returns a base-2 (binary) representation of a base-10
    (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10)
    010101001(2) = 1 + 8 + 32 + 128.
    Going from right to left, the value of the most right bit is 1, 
    now from that every bit to the left will be x2 the value, 
    value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
"""
dec = 169
bin = []
temp = dec
while temp > 0:
    bin.append(temp % 2)
    temp = temp//2
bin.reverse()
bin = str(bin).replace(", ", "")
print(bin)
