import numpy as np

# 1D array
arr=np.array([1,2,3,4,5])
print(arr)
print(arr.reshape(5,1))

# 2D array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)

# arange function
arr2=np.arange(0,10,2)
print(arr2)

print(np.ones((3,2)))
print(np.zeros((2,3)))

#identity matrix
arr=np.eye(3)
print(arr)

arr1=np.array([1,2,3,4,5])
arr2=np.array([10,11,12,13,14])

# addition
print(f"addition",arr1+arr2)

# subtraction
print(f"subtraction",arr1-arr2)

# multiplication
print(f"multiplication",arr1*arr2)

# division
print(f"division",np.round(arr1/arr2,2))


print(np.sqrt(36))
print(np.sin(45))

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)

print(array[0][1])
print(array[1:,1:])

# modify array
array [0,0]=10
print(array)

# arr[1:,2:] arr[1:]--> row of an array
#               2:--> coloum of an array

data=np.array([1,2,3,4,5])
mean=np.mean(data)
std_dev=np.std(data)

normalized_data=(data-mean)/std_dev
print(f"normalized data :",normalized_data)

mean=np.mean(data)
print(f"mean of a data : {mean}")
median=np.median(data)
print(f"median of a data : {median}")
std_dev=np.std(data)
print(f"standard deviation of  a mode: {std_dev}")
variance=np.var(data)
print(f"variance of a data : {variance}")

data=np.array([1,2,3,4,5,6,7,8,9,10])
print(data[data>5])

#logical operation
logical=data[(data>=5)&(data<8)]
print(logical)
