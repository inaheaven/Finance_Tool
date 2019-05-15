import numpy as np
print(np.array([2,3,4]))

print(np.array([(1,2,3),(4,5,6)]))

print(np.empty(5))
print(np.empty((5,4)))
print(np.empty((5,4,3)))

print(np.ones((5,4)))
print(np.ones((5,4), dtype=np.int_))

print(np.random.random((5,2)))
print(np.random.rand(5,2))
print(np.random.normal(size=(2,3))) #standard normal (mean =0, sd = 1)
print(np.random.normal(50, 10, size=(2,3))) #standard normal (mean =50, sd = 10)

print(np.random.randint(10))
print(np.random.randint(0, 10))
print(np.random.randint(0, 10, size=5))
print(np.random.randint(0, 10, size=(5,2)))

a = np.random.randint(0, 10, size=(5,4))
print(a)
print(a.shape)
print(a.shape[0])
print(a.shape[1])
print(len(a.shape)) # dimension of array
print(a.size)       #row * col
print(a.dtype)
print(a)
print("sum",a.sum())
print("sum in col", a.sum(axis=0))
print("sum in row", a.sum(axis=1))
print("min in col", a.min(axis=0))
print("min in arr", a.min(axis=1))
print("mean", a.mean(axis=0))
print(a[0])
print(a[0][1])
print(a[3,2])
print(a[0,1:3])
print(a[0:2, 0:2])
print(a[:, 0:4:2])

a= np.random.randint(0,10, size=(5,4))
print(a)
a[2,0]=23
a[0,:] = 123
a[3,:] = [1,2,3,4]
print("a",a)

a=np.random.randint(0,10,size=(5,3))
print(a)
indices = [1,2,2]
a[3,:] = indices
print(a[1,indices])

a = np.array([(1,2,3,4,5),(10,20,30,40,50)])
print(a)
print(a/2)
b = np.array([(100,200,300,400,500),(10,20,30,40,50)])
print(a+b)
print(b-a)
print(a*b)
print(a/b)
