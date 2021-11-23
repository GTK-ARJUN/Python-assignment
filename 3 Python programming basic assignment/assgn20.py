"""https://drive.google.com/file/d/15cu6V9tsKJrukQM_d3hYYx8JnaAQIHne/view"""

"""
Question1
    Create a function that takes a list of strings and integers, 
    and filters out the list so that it returns a list of integers only.
"""

alist = ["a", 'a', 0, 1, 5, 7, 'python']

filtered_list = [i for i in alist if type(i) == int]
print(filtered_list)


"""
Question2
    Given a list of numbers, create a function which returns the 
    list but with each element&#39;s index in the list added to itself. 
    This means you add 0 to the number at index 0, add 1 to the number 
    at index 1, etc...
"""
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_n = []
for i in range(len(list2)):
    list_n.append(list2[i]+i)

print(list_n)

"""
Question3
    Create a function that takes the height and radius of a cone as 
    arguments and returns the volume of the cone rounded to the 
    nearest hundredth. 
"""
height = 14
radius = 5


def volume(height, radius):
    vol = (height*3.14*radius**2)/3
    print(round(vol, 2))
    return


volume(height, radius)

"""
Question4
    This Triangular Number Sequence is generated from a pattern of dots that form a triangle. 
    The first 5 numbers of the sequence, or dots, are:
    1, 3, 6, 10, 15
    This means that the first triangle has just one dot, 
    the second one has three dots, the third one has 6 dots and so on.
    Write a function that gives the number of dots with its corresponding 
    triangle number of the sequence.
"""
num = 215
op = 0
for i in range(1, num+1):
    op += i

print(op)


"""
Question5
    Create a function that takes a list of numbers between 1 and 10 
    (excluding one number) and returns the missing number.
"""
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 10]

for i in range(2, 11):
    if i not in list3:
        print(i)
