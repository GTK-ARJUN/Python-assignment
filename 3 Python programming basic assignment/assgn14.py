"""https://drive.google.com/file/d/1ePUiHLs0lNCIwunPmoUDsonVzR-ZQoBa/view"""
"""
Question 1:
    Define a class with a generator which can iterate the numbers, which are divisible by
    7, between a given range 0 and n."""
input_1 = 50


def div_7(n):
    i = 1
    while i <= n:
        if i % 7 == 0:
            yield i
        i += 1


values = div_7(input_1)

for i in values:
    print(i)

"""
Question 2:
    Write a program to compute the frequency of the words from the input. The output
    should output after sorting the key alphanumerically. Suppose the following input 
    is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
    2:2, 3.:1, 3?:1, New:1, Python:5, Read:1, and:1 between:1 choosing:1 or:2 to:1"""

string1 = """New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."""
string1 = string1.split(" ")
string1.sort()
meta_String = {'word': [], 'count': []}
words = set(string1)


for word in words:
    meta_String['word'].append(word)
    meta_String['count'].append(string1.count(word))

print(meta_String)

"""
Question 3:
    Define a class Person and its two child classes: Male and Female. 
    All classes have a method &quot;getGender&quot; which can print &quot;
    Male&quot; for Male class and &quot;Female&quot; for Female class."""


class Person(object):
    def getGender(self):
        return "Unknown"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


aMale = Male()
aFemale = Female()
print(aMale.getGender())

print(aFemale.getGender())

"""
Question 4:
    Please write a program to generate all sentences where subject is in [&quot;I&quot;, &quot;You&quot;] and
    verb is in [&quot;Play&quot;, &quot;Love&quot;] and the object is in [&quot;Hockey&quot;,&quot;Football&quot;]."""


"""
Question 5:
    Please write a program to compress and decompress the string &quot;hello world!hello
    world!hello world!hello world!&quot;."""


"""
Question 6:
    Please write a binary search function which searches an item in a sorted list. The
    function should return the index of element to be searched in the list."""
