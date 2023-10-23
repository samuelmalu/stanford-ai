#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:19:23 2023

@author: samuelmalu
"""

print(dict([(0, 1), ( 1, 2), (2, 3)]))
print(set([1,1,2,3,4,4,4,5]))

alist = list() # linear, size not fixed, unhashable
atuple = tuple() # linear, fixed size, hashable
adict = dict() # hash table, not hashable, stores ke-value pairs
aset = set() #hash table, like dict but only stores keys
acopy = alist.copy() #shallow copy


d = dict()
d[("a", "cat")] = 10 #a tuple as a dictionary key, e.g to store ngram counts

print(d[("a", "cat")])

alist = []
alist = [1,2,3,4,5]
print(alist)


print("-"*10)

#list indexing
print(alist[0])
print(alist[-1])
print(alist[3:]) # get element STARTING from index 3 inclusive
print(alist[:3]) #get elements STOPPING at index 3 exclusive
print(alist[2:4]) #get elements withi index range 2 inclusive and 4 exclusive
print(alist[6:]) #prints nothing, index out of range
print(alist[::-1]) #reversed list

print("-"*10)

#list modification
alist.append("new item") #insert at end
alist.insert(0, "new item") #insert at index
alist.extend([2,3,4])# concatenate list
alist += [2,3,4] #concatenate list
newItemIndex = alist.index("new item") #search by content
newItemIndex = alist.index("new item", 1) #search by content from an index
newItemIndex = alist.index("new item", 1, 9) #search by content within some range
alist.remove("new item") #remove by content
alist.pop(0)  #remove by index
print(alist)

print("-"*10)
if "new item" in alist:
    print("found")
else:
    print("not found")
    
print("-"*10)
#list traversal
for item in alist:
    print(item)

print("-"*10)
# traverse with index
for i, item in enumerate(alist):
    print(i, item)

print("-"*10)
atuple = (1,2,3,4,5) #does not make sense to create an empty tuple
atuple = tuple([1,2,3]) #cast from another iterable
atuple = tuple({'a': 1, 'b': 2}) # ('a', 'b')
print(atuple)

print("-"*10)
adict = {} #empty dictionary
adict = ({'a': 1, 'b': 2, 'c': 3})
print(adict)
print(adict.keys()) #get keys
print(adict['a']) #get value paired with key

key = "e"
if key in adict:
    print(adict[key]) #accessing keys not in dictionary leads to exception

#add or modify dictionary entries
adict['e'] = 10 #instert new key
adict['e'] = 5 #modify existin keys

print("="*10)
#traverse keys only
for key in adict:
    print(key, adict[key])

print("="*10)
#traverse key value pairs
for key, value in adict.items():
    print(key, value)
    
print("="*10)
aset = set()
aset.add('a')

#deduplication shortcut
alist = [3,1,2,3,3,3,4,1]
alist = list(set(alist))
print(alist)

#default_dictionary returns a value computed from a default 
#   function for non-existedn entries
from collections import defaultdict
adict = defaultdict(lambda: 'unknown')
adict['cat'] = 'feline'
print(adict['cat'])
print(adict['dog'])

#couter is a dictionary with defual value of 0 and provides handy iterable
#counting tools
from collections import Counter
counter1 = Counter()
counter1['t'] = 10
counter1['t'] += 1
counter1['e'] += 1
print(counter1['z'])
print(counter1)
counter2 = Counter("leters to be counted")
print(counter2)
print("-"*10)

#computations using conters
print("1", counter1 + counter2)
print("2", counter1 - counter2)
print("3", counter1 or counter2) #research some more
print("4", counter1 and counter2) #research some more

print("-"* 10)
#sorting
a  = [4,6,1,7,0,5,-1,8,0, 9]
a =  sorted(a)
print(a)
a = sorted(a, reverse=True)
print(a)
a = [("cat", 1), ("dog", 3), ("bird", 2)]
a = sorted(a)
print(a)
a = sorted(a, key=lambda x:x[1])
print(a)

adict = {"cat": 3, "bird": 1}
print(sorted(adict.items(), key=lambda x:x[1]))

print("-"* 10)
#one line control flow

sent = ["i am good", "a beautiful day", "HELLO FRIENDS"]

sent1 = [s.lower().split(" ") for s in sent]
print(sent1)

sent2 = [s.lower().split(" ") for s in sent if len(s) > 10]

# Use this for deep copy!
# copy = [obj.copy() for obj in original]

# Syntax sugar: * operator for repeating iterable elements
print("-"*10) # Note: This only repeating by value
print([1]*10) # So you cannot apply the trick on reference types

# To create a double list
# DONT
doublelist = [[]]*10
doublelist[0].append(1)
print(doublelist)
#DO
doublelist = [[] for _ in range(10)]
doublelist[0].append(1)
print(doublelist)
