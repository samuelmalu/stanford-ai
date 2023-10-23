#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:14:15 2023

@author: samuelmalu
"""

import numpy
import torch
import torch.nn as nn

import pprint
pp = pprint.PrettyPrinter()

data = [
        [0,1, 4, 5],
        [2,3, 4, 5],
        [4,5, 4, 5]
       ]

data = torch.tensor(data)
pp.pprint(data.shape)
pp.pprint(data.view([3,2]))

# data = data.unsqueeze(1)
# pp.pprint(data)
# pp.pprint(data.shape)
# pp.pprint("============")

# x_python = torch.tensor(data,dtype=torch.float)
# x_python2 = torch.LongTensor(data)

# pp.pprint(x_python)
# pp.pprint(x_python.bool())
# pp.pprint(x_python2);

# print("="*10)

# import numpy as np
# #intialize from numpy array
# ndarray = np.array(data)
# x_numpy = torch.from_numpy(ndarray).long()

# pp.pprint(x_numpy)

# x = torch.tensor([
#                     [1., 2],
#                     [3, 4]
#                 ])
# pp.pprint(x)
# x_zeros = torch.zeros_like(x)
# pp.pprint(x_zeros)

# x_ones = torch.ones_like(x)
# pp.pprint(x_ones)

# # Initialize a tensor where each element is sampled from a uniform distribution
# # between 0 and 1
# x_rand = torch.rand_like(x)
# pp.pprint(x_rand)


# # Initialize a tensor where each element is sampled from a normal distribution
# x_randn = torch.randn_like(x)
# pp.pprint(x_randn)


# Initialize a 5x2 tensor, with 5 rows and 2 columns
# x = torch.arange(10).reshape(5, 2)
# pp.pprint(x.shape)
# pp.pprint(x)
# # Add a new dimension of size 1 at the 1st dimension
# x = x.unsqueeze(1)
# pp.pprint(x.shape)
# pp.pprint(x)
# # Squeeze the dimensions of x by getting rid of all the dimensions with 1 element
# x = x.squeeze()
# pp.pprint(x.shape)
# pp.pprint(x)