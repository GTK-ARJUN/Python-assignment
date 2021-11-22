"""https://drive.google.com/file/d/10ASPbmmQ86ZM78c5FjTHIhIJDwMZRHkE/view"""
# 1. Write a Python program to find sum of elements in list?
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in list1:
    sum += i
print(sum)

# 2. Write a Python program to Multiply all numbers in the list?
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = 1
for i in list2:
    product *= i
print(product)

# 3. Write a Python program to find smallest number in a list?
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smallest = list3[0]
for i in list3:
    if i < smallest:
        smallest = i
print(smallest)

# 4. Write a Python program to find largest number in a list?
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = list4[0]
for i in list4:
    if i > largest:
        largest = i
print(largest)

# 5. Write a Python program to find second largest number in a list?
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = list5[0]
second_largest = list5[0]
for i in list5:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(second_largest)


# 6. Write a Python program to find N largest elements from a list?
list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest = list6[0]
for i in list6:
    if i > largest:
        largest = i
print(largest)

# 7. Write a Python program to print even numbers in a list?
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list7:
    if i % 2 == 0:
        print(i)

# 8. Write a Python program to print odd numbers in a List?
list8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list8:
    if i % 2 != 0:
        print(i)

# 9. Write a Python program to Remove empty List from List?
list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, []]
for i in list9:
    if i == []:
        list9.remove(i)
print(list9)

# 10. Write a Python program to Cloning or Copying a list?
list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list11 = list10.copy()
print(list11)

print("*"*10)
# 11. Write a Python program to Count occurrences of an element in a list?
list11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = {'num': [], 'len': []}
for i in list11:
    if i not in length['num']:
        length['num'].append(i)
        length['len'].append(list11.count(i))
print(length)
