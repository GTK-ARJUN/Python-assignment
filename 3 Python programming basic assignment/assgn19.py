"""https://drive.google.com/file/d/1KkpC-4rnQuRnhIoxRAW6sTHYXCIH553I/view"""
"""
Question1
    Create a function that takes a string and returns a string in which each 
    character is repeated once.
"""
string = "hello"
string2 = ""

for i in string:
    string2 += i*2
print(string2)

"""
Question2
    Create a function that reverses a boolean value and returns the string:
    boolean expected&quot; if another variable type is given.
"""
inp_bool = False

if type(inp_bool) == bool:
    if inp_bool == True:
        inp_bool = False
    else:
        inp_bool = True
    print(inp_bool)
else:
    print("boolean expected")

"""
Question3
    Create a function that returns the thickness (in meters) of a 
    piece of paper after folding it n number of times. 
    The paper starts off with a thickness of 0.5mm.
"""
fold = 21


def fold_paper(fold):
    thickness = (2**fold*0.5)/1000
    return thickness


print(f"{fold_paper(fold)} m")

"""
Question4
    Create a function that takes a single string as argument and 
    returns an ordered list containing the indices of all capital 
    letters in the string.
"""
string4 = "eDaBiT"
indice = []
for i in string4:
    if i.isupper():
        indice.append(string4.index(i))
print(indice)

"""
Question5
    Using list comprehensions, create a function that finds all even 
    numbers from 1 to the given number.
"""
num = 10

list = [i for i in range(1, num+1) if i % 2 == 0]
print(list)
