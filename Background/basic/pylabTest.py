#!============================================================================
#! Numpy
#!============================================================================

#! Many of the examples are taken from: http://www.scipy.org/Cookbook

#! Building Arrays
#!---------------------------
import numpy

#! Arrays can be created from the usual python lists and tuples using the array function.
a = numpy.array([1,2,3])
print(a.shape)

#! returns a one dimensional array of integers. The array instance a has a large set of methods and properties attached to it. For example, a.shape is the dimension of the array. In this case, it would simply be (3,).

#! Arrays can also be created using numpy functions, e.g.: array of n-dim zeros
c = numpy.zeros((2,1,3))
print(c)
print(c.shape)

#! Array of n-dim ones
d = numpy.ones((10))
print(d)
print(d.shape)

#! Empty arrays of proper dim
d = numpy.empty((2,1))
print(d)

#! Regular spaced numbers
e = numpy.arange(10,20,2)
print(e)

#! Evenly spaced samples from start to stop.
f = numpy.linspace(10,20,7)
print(f)
print(f.shape)

#! Evenly spaced samples from start to stop, on log-scale.
f = numpy.logspace(10,20.,num=7,base=10.)
print(f)
print(f.shape)
print()

#! Meshgrid
x,y = numpy.meshgrid([1,2,3], [4,5,6,7])
print(x)
print(y)

#! Simple operations
#!---------------------------

#! Addition of two arrays adds the arrays elements-wise:
b = numpy.array((10,11,12))
print(a)
print(b)
print(a + b)

#! Subtraction, multiplication and division are defined similarly.
print(a-b)

#! min, max, sorting, clip ...
c = numpy.array([2,45,1,9])
print(c.min())
print(c.max())
d = c.copy()
d.sort()
print(c,d)
print(c.clip(2,9))

#! argmin, argmax, argsort
indices = c.argsort()
print(c[indices])
print(c.argmin())
print(c.argmax())

#! var, std, mean
print(c.var())
print(c.std())
print(c.mean())

#! unique
d = numpy.array([1,2,3,2,3,1,5,6,4])
print(numpy.unique(d))
print()

#! Data type of the array.
#!---------------------------
#! The array construct uses the type of its argument. Since a was created from a list of integers, it is defined as an integer array:
a = numpy.array([1,2,3])
print(a.dtype)

#! mathematical operations such as division will operate as usual in python, that is, will return an integer answer:
print(numpy.divide(a,3))

#! If divided by a float the results will be a float value:
print(numpy.divide(a,3.))

#! Similarly we can define the type at initialization time:
a = numpy.array([1,2,3],dtype=float)
print(numpy.divide(a,3))

#! Casting is another possibility:
a = numpy.array([1,2,3],dtype=int)
b = a.astype('float')
print(numpy.divide(a,3))
print(numpy.divide(b,3))
print()

#!===================
#! Indexing & Slicing
#!===================
#! The elements of an array are accessed using the bracket notation a[i] where i is an integer index starting at 0. Sub-arrays can be accessed by using general indexes of the form start:stop:step. a[start:stop:step] will return a reference to a sub-array of array a starting with (including) the element at index start going up to (but not including) the element at index stop in steps of step:
a = numpy.array([1,2,3,4,5,6,7,8,9,10], float)
#! get all values
print(a[:])

#! get the first 3 values
print(a[0:3])

#! get the last 3 values
print(a[-3::])

#! get the sub-array from index 2 till 8
print(a[2:8])

#! get the sub-array from index 2 till 8 in steps of 2
print(a[2:8:2])

#! This works of course in n-dim
a = numpy.ones((2,3,4,5,6))
b = a[0,1:3,2:3,:,0]
print(b.shape)

#! Indexing using bool-arrays
a = numpy.array([1,2,3,4,5,6,7,8,9,10], float)
i = a>=4
print(i)
print(a[i])

#! multiple bool-arrays
j = a<7
print(a[i&j])

#! Removing all length-1 dimensions
a = numpy.ones((10,1))
print(a.shape)
print(a)
b = a.squeeze()
print(b.shape)
print(b)
print()

#!=========================
#! Shaping arrays
#!=========================

#! Reshaping
a = 8*numpy.ones((2,3,4),float)
print(a)
b = a.reshape(6,4)
print(b)

#! Resizing
a = numpy.array([1,2])
print(a)
b = numpy.resize(a,(5))
print(b)

#! Flatten
a = numpy.ones((1,4,5,6))
print(a.shape)
print(a.flatten().shape)

#!===============
#! Appending
#!===============
a = numpy.arange(5)
print(a)
b = numpy.arange(3)
print(b)
c = numpy.append(a,b)
print(c)

#! Appending on the proper axis
a = numpy.array([[10,20,30],[40,50,60],[70,80,90]])
print(numpy.append(a,[[15,15,15]],axis=0))
print(numpy.append(a,[[15],[15],[15]],axis=1))

#!===============
#! Random numbers
#!===============
a = numpy.random.uniform(low=0.,high=10.,size=(2,3))
print(a)
b = numpy.random.normal(loc=10.,scale=2.,size=(100,100))
print(b.shape,b.size)
print(b.mean())
print(b.std())
print()

#! Seeds
#!-------
print(numpy.random.uniform(low=0.1,high=2.),numpy.random.uniform(low=0.1,high=2.))
numpy.random.seed(67)
print(numpy.random.uniform(low=0.1,high=2.),numpy.random.uniform(low=0.1,high=2.))
numpy.random.seed(67)
print(numpy.random.uniform(low=0.1,high=2.),numpy.random.uniform(low=0.1,high=2.))

print(dir(numpy.random))
print()

#!===============
#! Histograms
#!===============
#! 1D
b = numpy.random.normal(loc=10.,scale=2.,size=(100))
hs = numpy.histogram(b)

#! 2D
numpy.histogram2d

#! nD
numpy.histogramdd

#!=========================
#! Masked array: numpy.ma
#!=========================
# import numpy as np
# import numpy.ma as ma
# x = np.array([1, 2, 3, -1, 5])
# mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])
# mx.mean()
# 2.75

#!=========================
#! Input & Output
#!=========================

#! Saving and loading from text files
data = numpy.random.uniform(size=(5,5))
numpy.savetxt('myfile.txt', data)
loaded_data = numpy.loadtxt('myfile.txt')
print(numpy.alltrue(data == loaded_data))

#! Automaticall zipping
data = numpy.random.uniform(size=(5,5))
numpy.savetxt('myfile.gz', data)
loaded_data = numpy.loadtxt('myfile.gz')
print(numpy.alltrue(data == loaded_data))

#! Binary Files, save one array in one file
# numpy.save('test.npy', data)
# data2 = numpy.load('test.npy')

#! Save mulpiple arrays in one file
# a = numpy.random.uniform(size=(5,5))
# b = numpy.random.uniform(size=(5,5))
# numpy.savez('foo.npz', a=a,b=b)
# foo = numpy.load('foo.npz')
# print foo.files
# ['a', 'b']
# a2 = foo['a']
# b2 = foo['b']
print()

#!=========================
#! FFT
#!=========================
x = numpy.arange(-100,100,0.01)
y = numpy.zeros_like(x)
# A box of height 1
y[(x>-0.5)&(x<0.5)] = 1.0

#! Plotting


#import pylab

import matplotlib as mpl
mpl.use('TkAgg')  # or whatever other backend that you want
import matplotlib.pyplot as pylab

#import pylab

pylab.figure()
pylab.plot(x,y)
pylab.axis([-1,1,-0.5,2])
pylab.show()

z = numpy.fft.fft(y)
f = numpy.fft.fftfreq(len(y),d=0.01)

pylab.figure()
pylab.plot(f,numpy.abs(z))
pylab.axis([-5,5,0,100])
pylab.show()

