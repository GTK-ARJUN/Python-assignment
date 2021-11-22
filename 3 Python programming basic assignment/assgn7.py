"""https://drive.google.com/file/d/12gBynIzKKfWri0UfR5zm-JClbBlK-1vp/view"""
#1. Write a Python Program to find sum of array?
arr1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in arr1:
    sum=sum+i
print(sum)

#2. Write a Python Program to find largest element in an array?
arr1=[15,2,3,4,5,6,7,8,9,10]
max=arr1[0]
for i in arr1:
    if i>max:
        max=i 
print(max)
#3. Write a Python Program for array rotation?
arr1=[1,2,3,4,5,6,7,8,9,10]
arr1.append(arr1[0])
arr1.pop(0)
print(arr1)

#4. Write a Python Program to Split the array and add the first part to the end?
arr1=[1,2,3,4,5,6,7,8,9,10,11]
half=int(len(arr1)/2)
arr2=arr1[half+1:]
arr2.extend(arr1[0:half])
print(arr2)
#5. Write a Python Program to check if given array is Monotonic?
arr1=[1,2,3,4,5,6,7,8,9,10]
flag=0
for i in range(len(arr1)-1):
    if arr1[i]>arr1[i+1]:
        flag=1
        break
if flag==0:
    print("Array is monotonic")
else:
    print("Array is not monotonic")
