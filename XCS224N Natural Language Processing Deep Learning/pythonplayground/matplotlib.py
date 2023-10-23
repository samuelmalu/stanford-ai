#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 22:50:00 2023

@author: samuelmalu
"""

import matplotlib.pyplot as plt

#line plot
x = [1, 2, 3]
y = [1, 3, 2]
#plt.plot(x, y)
#plt.scatter(x, y)
#plt.bar(x, y)

x = [1,2,3]
y1 = [1,3,2]
y2 = [4,0,4]


#set figure size
plt.figure(figsize=(5,5))
# set axes
plt.xlim(0,5)
plt.ylim(0,5)
plt.xlabel("x label")
plt.ylabel("y label")
# add title
plt.title("My Plot")
plt.plot(x,y1, label="data1", color="red", marker="*")
plt.plot(x,y2, label="data2", color="green", marker=".")
plt.legend()