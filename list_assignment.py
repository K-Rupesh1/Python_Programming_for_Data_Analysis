
#Assignment 1: Creating and Accessing Lists
#Create a list of the first 20 positive integers. Print the list.
lst=list(x for x in range(1,21))
print(lst)

#Assignment 2: Accessing List Elements
#Print the first, middle, and last elements of the list created in Assignment 1.
first=lst[0]
middle=int(len(lst)/2)
last=lst[-1]
print(f"first element of a list {first}")
print(f"middle element of a list {middle}")
print(f"last element of a list {last}")

#Assignment 3: List Slicing
#Print the first five elements, the last five elements,
#and the elements from index 5 to 15 of the list created in Assignment 1.
first_five=lst[:6]
last_five=lst[-5:]
elements=lst[5:15]
print(f"first five elements in a list {first_five}")
print(f"last five elements in a list {last_five}")
print(f" elements from index 5 to 15 {elements}")

#Assignment 4: List Comprehensions
#Create a new list containing the squares of the first 10 positive integers 
#using a list comprehension. Print the new list.
lst=list(x**2 for x in range(1,11))
print(f"squares of a first 10 positive integers {lst}")

#Assignment 5: Filtering Lists
#Create a new list containing only the even numbers from the list created in Assignment 1 
#using a list comprehension. Print the new list.
#Create a list of the first 20 positive integers. Print the list.
lst=list(x for x in range(1,21) if x%2==0)
print(f"even numbers in list {lst}")
lst1=list(range(0,21))
print(f" first 20 positive integers {lst1}")

#Assignment 6: List Methods
#Create a list of random numbers and sort it in ascending and descending order.
#Remove the duplicates from the list and print the modified list.
import random
lst=list(random.randint(0,11) for _ in range(10))
print(lst)
ascending=sorted(lst)
print(ascending)
descending=sorted(lst,reverse=True)
print(descending)
remove_duplicates=set(lst)
new_list=list(remove_duplicates)
print(new_list)

#Assignment 7: Nested Lists
#Create a nested list representing a 3x3 matrix and print the matrix.
#Access and print the element at the second row and third column.

lst=[[1,2,3],
     [4,5,6],
     [7,8,9]]
for row in lst:
    print(row)
print(f"the element at the second row and third column ",lst[1][2])

#Assignment 8: List of Dictionaries
#Create a list of dictionaries where each dictionary represents a student 
#with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order 
#and print the sorted list.
students = [
    {'name': 'rupesh', 'score': 88},
    {'name': 'umesh', 'score': 72},
    {'name': 'kiran', 'score': 95},
    {'name': 'raju', 'score': 65},
    {'name': 'rajesh', 'score': 78}
]
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
print("Sorted students by score in descending order:")
for student in sorted_students:
    print(student)

#Assignment 9: Matrix Transposition
#Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose.
#Print the original and transposed matrices.

def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)
    

#Assignment 10: Flattening a Nested List
#Write a function that takes a nested list and flattens it into a single list. 
#Print the original and flattened lists.
def flatten_list(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return flat_list

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = flatten_list(nested_list)
print("Original nested list:")
print(nested_list)
print("Flattened list:")
print(flattened)

#Assignment 11: List Manipulation
#Create a list of the first 10 positive integers.
#Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5.
#Print the modified list.
lst=list(range(1,11))
print(lst)
del lst[2]
del lst[4]
del lst[6]
lst.insert(5,99)
print(lst)
#Assignment 12: List Zipping
#Create two lists of the same length. 
#Use the `zip` function to combine these lists into a list of tuples and print the result.
lst=[1,2,3,4,5]
lst1=[6,7,8,9,0]
combine=list(zip(lst,lst1))
print(combine)

#Assignment 13: List Reversal
#Write a function that takes a list and returns a new list with the elements in reverse order.
#Print the original and reversed lists.
def reverse(lst):
    return list(reversed(lst))
print(f"original list : {lst}")
print(f"reversed list : {reverse(lst)}")
lst=[1,2,3,4,5,6,7]

#Assignment 14: List Rotation
#Write a function that rotates a list by n positions. Print the original and rotated lists.
def list_rotate(lst1,k):
    k=k%len(lst1)
    #return lst1[k:]+lst1[:k] # rotates left
    return lst1[-k:]+lst1[:-k] # rotates right
lst1=[3,4,5,1,2]
rotated=list_rotate(lst1,2)

print(f"original list : {lst1}")
print(f"rotated list : {rotated}")



#Assignment 15: List Intersection
#Write a function that takes two lists and returns a new list containing only the elements
# that are present in both lists. Print the intersected list.
def intersection(list1, list2):
    return [item for item in list1 if item in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(intersection(list1, list2))