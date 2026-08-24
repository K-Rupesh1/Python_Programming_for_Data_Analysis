# 1: Array Creation and Manipulation
#1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
#2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
import numpy as np
import random
arr=np.random.randint(1,21,size=(5,5))
print(arr)
arr[:,2]=1
print(arr)

arr1=np.random.randint(1,17,size=(4,4))
print(arr1)
np.fill_diagonal(arr1,1)
print(arr1)

### Assignment 2: Array Indexing and Slicing
#1. Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
#2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
arr=np.arange(1,37).reshape((6,6))
print(arr)
print(arr[3:6,2:5])

arr1=np.random.randint(1,21,size=(5,5))
print(arr1)
border_elements = np.concatenate((arr1[0, :], arr1[-1, :], arr1[1:-1, 0], arr1[1:-1, -1]))
print("Border elements:")
print(border_elements)

### Assignment 3: Array Operations
#1. Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, 
#and division.
#2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
arr=np.random.randint(1,10,size=(1,5))
arr1=np.random.randint(10,20,size=(1,5))
print(arr)
print(arr1)
addition=np.add(arr,arr1)
print(addition)
subtraction=np.subtract(arr,arr1)
print(subtraction)
multiply=np.multiply(arr,arr1)
print(multiply)
divide=np.divide(arr,arr1)
print(divide)

arr2=np.random.randint(1,16,size=(4,4))
print(arr2)
row_wise_sum=np.sum(arr2,axis=1) #axis 1 is for row
print(row_wise_sum)
column_wisw_sum=np.sum(arr2,axis=0) # axis 0 is for column
print(column_wisw_sum)

### Assignment 4: Statistical Operations
#1. Create a NumPy array of shape (5, 5) filled with random integers. Compute the mean, median, standard deviation, 
#and variance of the array.
#2. Create a NumPy array of shape (3, 3) with values from 1 to 9. Normalize the array 
#(i.e., scale the values to have a mean of 0 and a standard deviation of 1).
arr=np.random.randint(1,10,size=(5,5))
print(arr)
mean=np.mean(arr)
median=np.median(arr)
standard_deviation=np.std(arr)
variance=np.var(arr)
print(f"mean of an array : {mean}")
print(f"median of an array : {median}")
print(f"standard_deviation of an array : {standard_deviation}")
print(f"variance of an array : {variance}")

arr2=np.arange(1,10).reshape(3,3)
print(arr2)
mean=np.mean(arr2)
print(mean)
std=np.std(arr2)
print(std)
normalize=(arr2-mean)/std
print(normalize)
mean=np.mean(normalize)
print(mean)
std=np.std(normalize)
print(std)
### Assignment 5: Broadcasting
#1. Create a NumPy array of shape (3, 3) filled with random integers. Add a 1D array of shape (3,) 
#to each row of the 2D array using broadcasting.
#2. Create a NumPy array of shape (4, 4) filled with random integers. Subtract a 1D array of shape (4,) 
#from each column of the 2D array using broadcasting.
arr=np.random.randint(1,10,size=(3,3))
print(arr)
new_row=np.random.randint(1,10,size=(3,))
print(new_row)
print(np.add(arr,new_row))

arr2=np.random.randint(1,17,size=(4,4))
print(arr2)
new_row=np.random.randint(1,17,size=(4,))
print(new_row)

print(np.subtract(arr2,new_row))

### Assignment 6: Linear Algebra
#1. Create a NumPy array of shape (3, 3) representing a matrix. Compute its determinant, inverse, and eigenvalues.
#2. Create two NumPy arrays of shape (2, 3) and (3, 2). Perform matrix multiplication on these arrays.
matrix=np.random.randint(1,10,size=(3,3))
print(matrix)
determinant=np.linalg.det(matrix)
print(f"determinant of a matrix : {determinant}")
inverse=np.linalg.inv(matrix)
print(f"inverse of a matrix : {inverse}")
eigenvalues=np.linalg.eigvals(matrix)
print(f"eigenvalues of a matrix : {eigenvalues}")
arr1=np.arange(1,7).reshape(2,3)
print(arr1)
arr2=np.arange(1,7).reshape(3,2)
print(arr2)
#matrix multiplication
multiplication=np.dot(arr1,arr2) # dot operator is used for multiplying two arrays with different shapes
print(f"multiplication of arrays : {multiplication}")

### Assignment 7: Advanced Array Manipulation
#1. Create a NumPy array of shape (3, 3) with values from 1 to 9. Reshape the array to shape (1, 9) and then to shape (9, 1).
#2. Create a NumPy array of shape (5, 5) filled with random integers. Flatten the array and then reshape it back to (5, 5).
arr1=np.arange(1,10).reshape(3,3)
print(arr1)
arr2=arr1.reshape(1,9)
print(f"reshaped array : {arr2}")
arr3=arr2.reshape(9,1)
print(f"reshaped array : {arr3}")

arr=np.random.randint(1,26,size=(5,5))
print(arr)
flatten=arr.flatten()
print(f"flatten array : {flatten}")
arr1=flatten.reshape(5,5)
print(f"reshaped array : {arr1}")

### Assignment 8: Fancy Indexing and Boolean Indexing
#1. Create a NumPy array of shape (5, 5) filled with random integers. Use fancy indexing to extract the elements at the corners of the array.
#2. Create a NumPy array of shape (4, 4) filled with random integers. Use boolean indexing to set all elements greater than 10 to 10.
arr=np.random.randint(1,26,size=(5,5))
print(arr)
corners=arr[[0,0,-1,-1],[0,-1,0,-1]]
print(corners)

arr1=np.random.randint(1,17,size=(4,4))
print(arr1)
arr1[arr1>10]=10
print(arr1)

### Assignment 9: Structured Arrays
#1. Create a structured array with fields 'name' (string), 'age' (integer), and 'weight' (float). Add some data and sort the array by age.
#2. Create a structured array with fields 'x' and 'y' (both integers). Add some data and compute the Euclidean distance between each pair of points.
data_type=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')]
data=np.array([('rupesh',22,45.0),('umesh',20,43.0),('rajesh',32,65.0)],dtype=data_type)
print(data)
#sort array by age
sorted_array=np.sort(data,order='age')
print(sorted_array)

data_type=[('x','i4'),('y','i4')]
data=np.array([(1,2),(3,4),(5,6),(7,8)],dtype=data_type)
print(data)
distances=np.sqrt((data['x'][:,np.newaxis]-data['x'])**2 + (data['y'][:,np.newaxis]-data['y'])**2)
print(f"euclidean : {distances}")

### Assignment 10: Masked Arrays
#1. Create a masked array of shape (4, 4) with random integers and mask the elements greater than 10. Compute the sum of the unmasked elements.
#2. Create a masked array of shape (3, 3) with random integers and mask the diagonal elements. 
# Replace the masked elements with the mean of the unmasked elements.
import numpy.ma as ma
arr=np.random.randint(1,17,size=(4,4))
print(arr)
# masked array
masked_array=ma.masked_greater(arr,10)
print(f"masked array greather than 10 : {masked_array}")
unmasked_array=masked_array.sum()
print(f"sum of unmasked array: {unmasked_array}")

arr1=np.random.randint(1,10,size=(3,3))
print(arr1)
# mask the diagonal
masked_array=ma.masked_array(arr1,np.eye(3,))
print(masked_array)
# Replace the masked elements with the mean of the unmasked elements.
mean=np.mean(masked_array)
print(mean)
masked_array=masked_array.filled(mean)
print(masked_array)
