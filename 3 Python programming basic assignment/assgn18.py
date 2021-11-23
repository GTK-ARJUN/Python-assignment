"""https://drive.google.com/file/d/1M4TrgsdcMxEAbT5_R_J2GsJSxYXgatYs/view"""

"""
Question 1
    Create a function that takes a list of non-negative integers and strings and 
    return a new list without the strings.
"""
list1 = [1, 2, 3, 4, 5, "a", "b", "c"]
filtered_list = []
for i in list1:
    if type(i) == int:
        filtered_list.append(i)

print(filtered_list)

"""
Question 2
    The &quot;Reverser&quot; takes a string as input and returns that 
    string in reverse order, with theopposite case.
"""
string3 = "Hello World"
string_n = ""

for i in range(len(string3)+1):
    string_n = string_n+string3[-i].swapcase()

print(string_n)

"""
Question 3
    You can assign variables from lists like this:
    lst = [1, 2, 3, 4, 5, 6]
    first = lst[0]
    middle = lst[1:-1]
    last = lst[-1]
"""
lst = [1, 2, 3, 4, 5, 6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]
print(first)
print(middle)
print(last)

"""
Question 4
    Write a function that calculates the factorial of a number recursively.
"""
num = 5


def factorial(num):
    if num == 0:
        return 1
    else:
        fact = num*factorial(num-1)
        return fact


print(factorial(num))


"""
Question 5
    Write a function that moves all elements of one type to the end of the list.
"""
# question not clear
