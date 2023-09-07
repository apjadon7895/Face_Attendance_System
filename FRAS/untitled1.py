import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#arr = np.array([1,2,3,4,5])
#print(arr)
#print(type(arr))

#arr = np.array(42)
#print(arr)

#arr = np.array([[1,2,3],[4,5,6]])
#print(arr)

#arr = np.zeros(6)
#print(arr)

#arr = np.ones(10)*8
#print(arr)

#arr = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])
#print(arr)

#a= np.array(42)
#b= np.array([1,2,3,4,5])
#c = np.array([[ [1,2,3],[4,5,6]]])
#d = np.array([[1,2,3],[4,5,6],[7,8,9],[1,2,3]])

#print(a.ndim)
#print(b.ndim)
#print(c.ndim)
#print(d.ndim)

#arr = np. array([1,2,3,4], ndmin=5)
#print(arr)
#print('number  of  dimensions :', arr.ndim)

#arr= np.array([1,2,3,4,5])
#print(arr[0])
#print(arr[2]+arr[3])

#arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print('2nd element  on 1st  row:', arr[0,1])

#arr = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])
#print(arr[1,1 ])

#c = np.array([ [1,2,3], [4,5,6]])
#print(c[:,0:2])

#age = 21
#college = "gla"
#print(f"my name  is amit pratap singh my age{0} and my collage name{1}",age,college)
#print(a.format(age, college))

#thislist = ["apple","banana","cherry"]
#hislist[1] = "papaya"
#print(thislist)

# =============================================================================
# thislist = ["apple","banana","cherry"]
# thislist[1:3] = ["papaya"]
# print(thislist)
# =============================================================================

# =============================================================================
# thislist = ["apple","banana","cherry"]
# thislist[1:3] = ["papaya","kiwi"]
# print(thislist)
# =============================================================================
 
# =============================================================================
# thislist = ["apple","banana","cherry"]
# thislist[1:2 ] = ["papaya","kiwi"]
# print(thislist)
# =============================================================================

# =============================================================================
# xpoints = np.array([0,6])
# ypoints = np.array([0,200])
# plt.plot(xpoints, ypoints)
# plt.show()
# =============================================================================

# =============================================================================
# x = np.array(["a","b","c","d"])
# y = np.array([3,8,1,10])
# plt.plot(x, y, 'o')
# plt.show()
# =============================================================================

# =============================================================================
# x = np.array(["a","b","c","d"])
# y = np.array([3,8,1,10])
# plt.barh(x, y)
# plt.show()
# =============================================================================


x = np.array(["a","b","c","d"])
y = np.array([3,8,1,10])
plt.bar(x, y)
plt.show()



# =============================================================================
# mydataset = {'car':["bmw","honda","suzuki"],'passing':[3,4,7]}
# myvar = pd.DataFrame(mydataset)
# print(myvar)
# =============================================================================












