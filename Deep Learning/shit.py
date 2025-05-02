print("Hellow World")
a = 10
a = 12
print(a)

#make a dictionary with names and addresses as key value pairs    

dic=dict(name="zhangsan",age=18,address="beijing",city="beijing")
print(dic)

for i in dic:
    print(i,sep="--")

for i in dic.values():
    print(i)

for i in dic.keys():
    print(i)

for i in dic.items():
    print(i)

dic.update(name="lisi")
print(dic)

b=[x*x for x in range(10)]
print(b)
from random import shuffle
shuffle(b)
print(b)
import numpy as np
arr=np.arange(20)
np.random.shuffle(arr)

sample=np.random.choice(arr,5,replace=False)
print(sample)

sample1=np.random.permutation(arr)
print(sample1)

sample2=np.random.randint(0,10,5)
print(sample2)

import random
sample=random.sample(range(10),5)
print(sample)

import os
os.getcwd()
os.chdir("C:\\Users\\
