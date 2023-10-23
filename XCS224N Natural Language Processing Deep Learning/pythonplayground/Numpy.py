#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:38:28 2023

@author: samuelmalu
"""

#TO DO - revise Matrices

import numpy as np
a = np.array([
                [1, 2],
                [3, 4],
                [5, 6],
              ])
print(a)
print(a.shape)

#create all-zero/one arrayes
b = np.ones((3,4))
#b = np.zeros((3,4))
print(b)
print(b.shape)

#create identity matrix
c = np.eye(5)
print(c)
print(c.shape)

#reshaping arrays
a = np.arange(8) # [8,] similar range() you use in for-loops
b = a.reshape((4,2))
c = a.reshape((2,2, -1)) # shape [2,2,2] -- -1 for auto-fill - <REVISE THIS>
d = c.flatten() # shape [8,]
e = np.expand_dims(a, 0) # [1,8]
f = np.expand_dims(a, 1) # [8,1]
g = e.squeeze() # shape[8, ] -- remove all unnecessary dimensions

print("a:\n", a)
print("b:\n", b)
print("c:\n", c)
print("d:\n", d)
print("e:\n", e)
print("f:\n", f)
print("g:\n", g)

a = np.ones((4,3))
b = np.zeros((4,3))
c = np.concatenate([a, b], 0)
print("concat c:\n", c)
print(c.shape)
d = np.concatenate([a, b], 1);
print("concat d:\n", d)
print(d.shape)

# one application is to create a batch for NN <REVISE THIS>
x1 = np.ones((32,32,3))
x2 = np.ones((32,32,3))
x3 = np.ones((32,32,3))
# --> to create a batch of shape (3,32,32,3)
x = [x1, x2, x3]
x = [np.expand_dims(xx, 0) for xx in x] # xx shape becomes (1,32,32,3)
x = np.concatenate(x, 0)
print(x.shape)
print(x)

#access aray slices by index
a = np.zeros([10, 10])
a[:3] = 1
a[:, :3] = 2
a[:3, :3] = 3
rows = [4,6,7]
cols = [9,3,5]
a[rows, cols] = 4
print(a)

print("="*10)
#transposition
a = np.arange(24).reshape(2,3,4)
print(a.shape)
print(a)

a = np.transpose(a, (2,1,0)) #swap 0th and 2nd axes
print(a.shape)
print(a)


#...CONTINUE NUMPY