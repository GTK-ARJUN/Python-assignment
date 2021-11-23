"""https://drive.google.com/file/d/19-J6nCYXNUw_mcim9yqptiN-8PCjEco0/view"""
# 1. Write a Python program to Extract Unique values dictionary values?
from collections import OrderedDict
d = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
print(set(d.values()))

# 2. Write a Python program to find the sum of all items in a dictionary?
d = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
print(sum(d.values()))

# 3. Write a Python program to Merging two Dictionaries?
d1 = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 1}
d2 = {'x': 1, 'y': 2, 'z': 1}
d3 = {**d1, **d2}
print(d3)

# 4. Write a Python program to convert key-values list to flat dictionary?
values = [1, 2, 3, 4, 5]
keys = ['a', 'b', 'c', 'd', 'e']
dict1 = {"key": [], 'values': []}
for i in range(len(values)):
    dict1['key'].append(keys[i])
    dict1['values'].append(values[i])
print(dict1)

# 5. Write a Python program to insertion at the beginning in OrderedDict?
dict1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
dict1.update([('d', 4)])
dict1.move_to_end('d', last=False)
print(dict1)

# 6. Write a Python program to check order of character in string using OrderedDict()?
dict1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(dict1)


# 7. Write a Python program to sort Python Dictionaries by Key or Value?
