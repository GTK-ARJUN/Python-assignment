"""https://drive.google.com/file/d/1KMvOueR-cQxRJD9cADGccJxVmYDp2xkV/view"""
#1. Write a Python Program to Add Two Matrices?
mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[1,2,3],[4,5,6],[7,8,9]]
mata=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mata[i][j]=mat1[i][j]+mat2[i][j]
print(mata)

#2. Write a Python Program to Multiply Two Matrices?
mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[1,2,3],[4,5,6],[7,8,9]]
matm=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        matm[i][j]=mat1[i][j]*mat2[i][j]
print(matm)

#3. Write a Python Program to Transpose a Matrix?
mat1=[[1,2,3],[4,5,6],[7,8,9]]
matm=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        matm[j][i]=mat1[i][j]
print(matm)

#4. Write a Python Program to Sort Words in Alphabetic Order?
words=['hello','world!','my','name','is','akshay']
words.sort()
print(words)
#5. Write a Python Program to Remove Punctuation From a String?
string="Hello, World! My name is Akshay"
string=string.replace(",","") 
string=string.replace(".","")
string=string.replace("!","")
string=string.replace("?","")
string=string.replace(" ","")
print(string)
# alternative method
str2=[]
for i in range(len(string)):
    if (string[i].isalnum()):
        str2.append(string[i])

str2="".join(str2)
print(str2)
