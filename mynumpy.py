import numpy as np

# Creating a 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# Creating a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1)
print(arr2)

print(arr2.ndim)       # Number of dimensions (2 for a 2D array)
print(arr2.shape)      # Shape of the array (number of rows and columns)
print(arr2.size)       # Total number of elements
print(arr2.dtype)      # Data type of the array elements

print(arr2[0, 1])   # Accessing element at row 0, column 1 (output: 2)
print(arr2[1, :])   # Accessing all elements of row 1 (output: [4, 5, 6])
print(arr2[:, 2])   # Accessing all elements of column 2 (output: [3, 6])

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print(a + b)  # Output: [5, 7, 9]

# Element-wise multiplication
print(a * b)  # Output: [4, 10, 18]

# Applying mathematical functions
print(np.sin(a))  # Sine of each element

a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

# Broadcasting allows you to add arrays of different shapes
print(a + b)  
print("IHfdhd")
print(b + a)
# Output:
# [[2, 3, 4],
#  [3, 4, 5],
#  [4, 5, 6]]

# Reshaping an array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])

reshaped_arr = arr2.reshape(3, 2)
print(reshaped_arr)

# Transposing an array
transposed_arr = arr2.T
print(transposed_arr)

# Generating a 1D array of 5 random numbers
random_array = np.random.rand(5)

# Generating a 2D array of random integers
random_int_array = np.random.randint(1, 10, size=(3, 5))

print(random_array)
print(random_int_array)

d = np.random.randint(1,56, size = (10,5))
print(d)

rven = np.arange(10,50, 2)
print(rven)

flo = np.linspace(11, 12, 3)
print(flo)

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8,9], [10,11,12], [2,3,4]])

# print(a*b)
print(a@b)