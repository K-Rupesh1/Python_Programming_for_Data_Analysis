
#1: Creating and Accessing Tuples
#Create a tuple with the first 10 positive integers. Print the tuple.
num=(1,2,3,4,5,6,7,8,9,10)
print(type(num))
print(num)

tp=tuple( range(1,11))
print(tp)

#2: Accessing Tuple Elements
#Print the first, middle, and last elements of the tuple created in Assignment 1.
print(num[0],num[4],num[9])
print(num[0])
print(num[(len(num)//2)])
print(num[-1])

#3: Tuple Slicing
#Print the first three elements, the last three elements, 
#and the elements from index 2 to 5 of the tuple created in Assignment 1.
print(num[:3])
print(num[-3:])
print(num[2:5])

#4: Nested Tuples
#Create a nested tuple representing a 3x3 matrix and print the matrix.
#Access and print the element at the second row and third column.
matrix=((1,2,3),
        (4,5,6),
        (7,8,9))
print(matrix)
for row in (matrix):
    print(row)
print(f"element at second row and third column : {matrix[1][2]}")

#5: Tuple Concatenation
#Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
tp1=(1,2,3)
tp2=(4,5,6)
tp3=tp1+tp2
print(tp3)
    
#6: Tuple Methods
#Create a tuple with duplicate elements and count the occurrences of an element. 
#Find the index of the first occurrence of an element in the tuple.
tp=(1,2,1,3,5,4,1)
count=0
print(f"occurance of 1 : {tp.count(1)}")
print(f"index of first occurance : {tp.index(1)}")

#7: Unpacking Tuples
#Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
tp=(1,2,3,4,5)
a,b,c,d,e=tp
print(a,b,c,d,e)

#8: Tuple Conversion
#Convert a list of the first 5 positive integers to a tuple. Print the tuple.
lst=[1,2,3,4,5]
tp=tuple(lst)
print(tp)
print(type(tp))

#9: Tuple of Tuples
#Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
tp=((1,2,3),
    (4,5,6),
    (7,8,9))
print(tp)

#10: Tuple and List
#Create a tuple with the first 5 positive integers. 
#Convert it to a list, append the number 6, 
#and convert it back to a tuple. Print the resulting tuple.
tp=tuple(range(1,6))
lst=list(tp)
lst.append(6)
print(lst)
converted_tuple=tuple(lst)
print(converted_tuple)

#11: Tuple and String
#Create a tuple with the characters of a string.
#Join the tuple elements into a single string. Print the string.
tp=('s','t','r','i','n','g')
string=str(tp[0]+tp[1]+tp[2]+tp[3]+tp[4]+tp[5])
print(string)
print(type(string))

#12: Tuple and Dictionary
#Create a dictionary with tuple keys and integer values. Print the dictionary.
tp=("quantity","price")
values=(2,50)
dictionary=dict(zip(tp,values))
print(dictionary)

#13: Nested Tuple Iteration
#Create a nested tuple and iterate over the elements, printing each element.
student = (
    ("Rupesh", 21),
    ("Rahul", 22),
    ("Priya", 20)
)

for stu in student:
    for value in stu:
        print(value)

#14: Tuple and Set
#Create a tuple with duplicate elements. Convert it to a set to remove duplicates and
# print the resulting set.
tp=(1,2,1,3,2,4,2,1,5)
result=set(tp)
print(result)

#15: Tuple Functions
#Write functions that take a tuple and 
# return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
def tp(nums):
    minimum=min(nums)
    maximum=max(nums)
    sum=0
    for i in range(0,len(nums)):
        sum=sum+i    
    print(f"minimum : {minimum}")
    print(f"maximum : {maximum}")
    print(f"sum of elements : {sum}")
nums=(1,2,3,4,5,6)
tp(nums)