# one dimensional example
from numpy import array
# list of data
data = [11, 22, 33, 44, 55]
# array of data
data = array(data)
print(data)
print(type(data))

# two dimensional example
from numpy import array
# list of data
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print(data)
print(type(data))

######### Indexing ##########
## simple indexing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[0])
print(data[4])

# simple indexing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[4])

# simple indexing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
# index data
print(data[-1])
print(data[-5])

## 2d indexing
from numpy import array
# define array
data = array([[11, 22], [33, 44], [55, 66]])
# index data
print(data[0,0])

# 2d indexing
from numpy import array
# define array
data = array([[11, 22], [33, 44], [55, 66]])
# index data
print(data[0,])

##########################################

############# Slicing #############
# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[:])

# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[0:1])

# simple slicing
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data[-2:])

############# 2 dimensional slicing #############

# split input and output
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
# separate data
X, y = data[:, :-1], data[:, -1]
print(X)
print(y)


##################################################

## Split data
# split train and test
from numpy import array
# define array
data = array([[11, 22, 33],
		[44, 55, 66],
		[77, 88, 99]])
# separate data
split = 2
train,test = data[:split,:],data[split:,:]
print(train)
print(test)


##################################################

## Data Shape
# array shape
from numpy import array
# define array
data = array([11, 22, 33, 44, 55])
print(data.shape)

# array shape
from numpy import array
# list of data
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print(data.shape)

# array shape
from numpy import array
# list of data
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print('Rows: %d' % data.shape[0])
print('Cols: %d' % data.shape[1])

# reshape 1D array
from numpy import array
from numpy import reshape
# define array
data = array([11, 22, 33, 44, 55])
print(data.shape)
print(data)

# reshape
data = data.reshape((data.shape[0], 1))
print(data.shape)
print(data)

print("Reshape 2 d array !")
# reshape 2D array
from numpy import array
# list of data
data = [[11, 22],
		[33, 44],
		[55, 66]]
# array of data
data = array(data)
print(data.shape)
print(data)

# reshape
data = data.reshape((data.shape[0], data.shape[1], 1))
print(data.shape)
print(data)






