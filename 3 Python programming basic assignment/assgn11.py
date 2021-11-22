"""https://drive.google.com/file/d/1746HlOfuieTY61nVpgrfJJpcOY7IVlyW/view"""
# 1. Write a Python program to find words which are greater than given length k?
words = ['hello', 'world', 'my', 'name', 'is', 'Anna']


def find_words_greater_than_k(k):
    result = []
    for word in words:
        if len(word) > k:
            result.append(word)
    return result


#k=int(input("Enter the length of the word: "))
k = 4
print(find_words_greater_than_k(k))

# 2. Write a Python program for removing i-th character from a string?
string1 = """Write a Python program for removing i-th character from a string?"""
#i=int(input("Enter the index of the character to be removed: "))
i = 3
string2 = string1[:i-1]+string1[i:]
print(string2)

# 3. Write a Python program to split and join a string?
string1 = """Write a Python program to split and join a string?"""
string2 = string1.split()
print(f"{string2 = }")
string3 = " ".join(string2)
print(f"{string3 = }")

# 4. Write a Python to check if a given string is binary string or not?
string1 = """0101"""
string1_set = set(string1)

if string1_set == {'1', '0'} or string1_set == {'0', '1'} or string1_set == "1" or string1_set == "0":
    print("Yes")
else:
    print("No")


# 5. Write a Python program to find uncommon words from two Strings?
words1 = ['hello', 'python', 'my', 'name', 'is', 'shweta']
words2 = ['hello', 'world', 'my', 'name', 'is', 'akshay']

print([i for i in words1 if i not in words2] +
      [i for i in words2 if i not in words1])

# 6. Write a Python to find all duplicate characters in string?
string1 = """Write a Python to all all duplicate characters python duplicate ?"""
string2 = string1.split()

print(set([i for i in string2 if string2.count(i) > 1]))

# 7. Write a Python Program to check if a string contains any special character?
string1 = """Write* > a Python Program to check if a * *string contains any special character?"""

print(string1.isalnum())
