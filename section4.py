import numpy as np

mylist = [1,4,560]
myarr = np.array(mylist)
print(type(mylist))
print(type(myarr))
print(mylist)
print(myarr)
list2 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(list2)
print(list2)
print(arr2)

arr3 = np.arange(0,5)
print(arr3)
arr4 = np.arange(0,10,2)
print(arr4)
print(np.zeros(5))#default floating point
print(np.ones((5,5)))
print(np.linspace(0,10,6))#remember even 10 is included and 6 digits equally spaced from 0 - 10 are printed,starting with zero, ending with 10
print(np.eye(3))#identity matrix
print(np.random.rand(5,2))#(row,column) - numbers printed are from 0 to 1-uniform distribution
print(np.random.randn(5))#from standard distribution - 0 mean and 1 variance - 5 numbers are printed - close to zero (higher chance)
print(np.random.randint(0,15,(5,3)))#0-14 random nums
print(np.random.randint(0,15,3))#0-14 random nums
np.random.seed(42)
print(np.random.rand(4))
np.random.seed(42)#sticks to a specific set of random numbers
print(np.random.rand(4))
np.random.seed(42)
print(np.random.randint(0,50,3))
np.random.seed(42)
print(np.random.randint(0,50,3))
np.random.seed(42)
print(np.random.rand(4))
arr5 = np.arange(0,15)
print(arr5)
arr7 = arr5.reshape(5,3)#15 elements
print(arr5)
print(arr7)
#arr5.reshape(4,4)- 16 elements not available in the original array - returns error
print(arr5.dtype)
arr6 = np.random.randint(0,10000,10)
print(arr6)
print(arr6.max())
print(arr6.min())
print(arr6.argmax())# gives the index at which max value is present, same goes to min value
print(arr6.argmin())
#to find shape
print(arr5.shape)
print(arr6.shape)
print(arr7.shape)
#numpy array slicing,indexing
arr8 = [[1,2,3],[4,5,6],[7,8,9,]]
arr9 = np.array(arr8)
print(arr9)
print(arr9.shape)
print(arr9[0])
print(arr9[2,2])#accessing specific elements in a matrix
print(arr9[1,2])
print(arr8[0])
arr10=np.array([4,67,8,456,1,20])
print(arr10)
arr10[:3] = 100 #broadcasting - only works with numpy arrays - not with normal ones
print(arr10)
arr11 = arr10[:4]#creates a pointer for that part of the array
print(arr10)
print(arr11)
arr11[:]= 500
print(arr10)
print(arr11)
#to just copy a numpy array or part of it use .copy()
arr12= arr10[:4].copy()
print(arr12)
print(arr10)
arr12[:] =1
print(arr12)
print(arr10)# the original  numpy array remains unchanged
print(arr10[4:])#slicing
#2d array - matrix submatrix access
print(arr9)
print(arr9[:2,1:])
#most important part - conditional filtering of arrays
print(arr10[arr10<500])# filters according to condition
bool_arr10 = arr10<500
print(bool_arr10)# when the conditions in bool_arr10 is sent as an index to arr10 , the original array
#it filters out the true condition elements or indices
#numpy arithmetic operations
arr13 = np.arange(5,15)
print(arr13)
print(arr13 +2)
print(arr13)
print(arr13 + arr13)# remember length of the arrays must be same to add every corresponding element
arr14 = [0,1,2]
arr15 = np.ones(3)
print(arr14/arr15)
print(arr15/arr14)
arr16= np.zeros(3)
print(arr14/arr16)#0/0 = nan (not) , 1/0 = inf - only with numpy arrays, with just python variables - wud return error
#special functions for  np arrays
print(np.sqrt(arr14))
print(np.sin(arr14))
print(np.log(arr14))#natural log

arr14 = np.append(arr14,[10,8,2.718])#remember it returns a copy of the appended array, not directly append and update the array
print(arr14)
print(np.log(arr14))
print(np.log10(arr14))
print(arr14.sum())
print(arr14.mean())
print(arr14.var())
print(arr14.max())
print(arr14.std())#standard deviation
#axes for 2d arrays
arr_2d = np.arange(0,25).reshape(5,5)
print(arr_2d.sum())
print(arr_2d.sum(axis = 0))#fix a column and across the rows the elements present for that column are added up, done for all the columns
print(arr_2d.sum(axis = 1))#the vice versa , column -> row