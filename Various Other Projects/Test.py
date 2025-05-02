import decimal as d
import math as m
import os
import random
import time

import matplotlib.pylab as pl  # Don't use it.Use below instead.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import statsmodels as st
from numpy import random

# ---------------------------------


# ------------------------
a = range(12)
a
list(a)
b = np.arange(12)
type(b)
c = range(12)
a + c  # Error
list_ = []
list_ += [a[i] + c[i] for i in range(12)]
list_
list2 = [a[i] + c[i] for i in range(12)]
list2
d = np.arange(12)
b + d
# -------------------------------------------------------
# Numpy course

a1 = np.array([1, 3, 6, 8])
a2 = np.array([[1, 3, 6, 8], [2, 4, 1, 5], [7, 5, 1, 0]])
a3 = np.array(
    [
        [[1, 7, 6, 8], [2, 4, 1, 5]],
        [[9, 3, 6, 5], [7, 8, 1, 5]],
        [[3, 2, 4, 6], [1, 2, 4, 3]],
    ]
)
a4 = np.array([[], [], [], []])
a4.shape
a5 = np.array([])
a5.shape
a6 = np.array([[[]], [[]], [[]], [[]]])
a6.shape
a1.shape  # یک بعدی
a2.shape  # دوبعدی
a3.shape  # سه بعدی this show a3 is three 2*4 matrixes.
a1[1:3]
a2[0:2]
print(a2[0:2])
a2[0:2][:-1]
a3[0:2]
a3[0:2].shape
a3[0:2][1]
a3[0:2][1][0]
type(a3[0:2][1][0])
a3[0:2][1].shape
a3[0:2][0]
len(a1.shape)  # از روی طول ابعاد میتوان فهمید چند بعدی است.
len(a2.shape)
len(a3.shape)
a = np.array([1, 2, 3])
a.shape
np.resize(a, (4, 4))
a
np.resize(1, (5, 6))  # build an array with your own unique values
a = range(12)
np.resize(a, (5, 5))
np.resize(a, (4, 3, 5))  # 4 3*5 matrices
x = np.resize(a, (4, 3, 5))
x[2][1:]
x[2][1:][1]
x[2][1:][1]
x
x[0:2, 1:]
x[0:2, 1:, 1:3]
x[:2, :, 1:4]
f = np.resize(1, (2, 4))
np.sum(f, axis=0)  # element-wise addition of rows. axis=0 is for rows
np.sum(f, axis=1)
a.resize((4, 4))
a
a = np.array([1, 2, 3])
a.resize((4, 4))
a
a = np.ones((5, 5), dtype=np.uint8)
a
a.dtype
a = np.array([1, 2, 3, 4, 5])
a.resize((4, 5))
a
a.diagonal()
np.diag(a)
np.diagonal(a)
np.zeros((3, 3), dtype=np.float32)
np.repeat([1, 2, 4], 5)
a = np.array([1, 2, 3, 4, 5], dtype=np.int8)
a.dtype
a = np.array([1, 23, 4, 556, 6, 3])
b = np.ones((3, 6))
np.vstack((a, b), dtype=np.int16, casting="unsafe")
a.resize((3, 2))
a
np.hstack((a, b))
a, b = np.array([1, 2, 3]), np.array([1, 2, 4])
a.dot(b)  # inner product of arrays a and b.
a = np.random.rand(
    3, 2
)  # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)
a
a.T  # Transpose of a
b = np.random.rand(4, 4)
c = np.random.randint(0, 5, size=(4, 4))
# The discrete uniform distribution with parameters
# constructs a random variable that has an equal probability
# of being any one of the integers in the half-open range .
b + c
z = np.arange(15)
z[5::-1]  # when step is negative start and stop are reversed
z[-1::-1]
z[-8:-2:1]
z[
    -3:-10:2
]  # it returns an empty array because you can't tell it to start from the end of a set and go forward!
z[
    -3:-10
]  # it returns an empty array because you can't tell it to start from the end of a set and go forward!
# indeed the end of the set is smaller than it's start with a default 1 step size!
rand_array = np.random.randint(10, size=(4, 4)) + np.random.rand(4, 4)
# read the documentation for randint its huge!
rand_array[0:4, 2]  # It gives a vector
rand_array[0:4, -1:]  # It gives and nd-array (semicolon is key here)
rand_array[0:5:2, 0:5:2]
rand_array[2:3:1, 0:2:2]  # It again gives an array of one dimension!
rand_array < 3  # It's a boolean matrix
rand_array[rand_array < 3]  # a vector because it returns truths only.
rand_array[(1 < rand_array and rand_array < 3)]  # Throws error.
rand_array[np.logical_and(1 < rand_array, rand_array < 3)]  # This how you do it!
rand_array = np.random.randint(10, size=(4, 4)) + np.random.rand(4, 4)
rand_array[-1]  # the last row
rand_array[0:2] = 1
rand_array[:, 1:3] = 1
rand_array3 = rand_array
rand_array3 is rand_array  # True
rand_array2 = rand_array.copy()
rand_array is rand_array2  # false
g, k = np.random.randint(10, size=(4, 4)), np.random.randint(10, size=(4, 4))
g
k
list(zip(g, k))
x = np.array([[2, 1, 6], [0, 7, 3]])  # Returns the indices that would sort an array.
x
type(x)
np.sort(x, axis=0)
np.sort(x, axis=1)
np.sort(x, axis=None)
ind = np.argsort(x)  # default axis is 1.
ind
xSorted = np.take_along_axis(x, ind, axis=1)
xSorted
ind = np.argsort(x, axis=0)
ind
xSorted = np.take_along_axis(x, ind, axis=0)
xSorted
ind = np.argsort(x, axis=None)
ind
xSorted = np.take_along_axis(x, ind, axis=None)
xSorted
x
np.max(x)
np.max(x, axis=0)
np.max(x, axis=1)
np.expand_dims(np.max(x, axis=1), axis=1)
x
x.shape
y = np.expand_dims(x, axis=0)
y
y.shape
y = np.expand_dims(x, axis=1)
y
y.shape
y = np.expand_dims(x, axis=2)
y
y.shape
rng = np.random.default_rng(154)
rng.random()
rng.random((5,))
rng.random((5, 2))
rng.integers(1, 10)
rng.integers(1, 10, size=(2, 3), endpoint=True)
rng.integers(10, size=(2, 3), endpoint=True)
np.cov(rng.random((5, 2)), rng.random((5, 2)))
np.corrcoef(rng.random((5, 2)))
np.mean(rng.random((5, 2)))
np.var(rng.random((5, 2)))
a = np.array([-129, -128, 0, 1, 127, 128, 257], dtype=np.int8)
a
s = np.array(["Amir", "Sina", "Mina", "Mohammadreza", "Zahra"])
s.dtype
s = np.array(["Amir", "Sina", "Mina", "Mohammadreza", "Zahra"], dtype="<U9")
s
s.dtype
s = s.astype("<U12")
s[3] = "Mohammadreza"
s
s.dtype
a = np.array(
    [
        [32, 19, 17, 39, 16, 20, 13],
        [29, 10, 32, 36, 27, 30, 21],
        [26, 34, 28, 16, 26, 23, 19],
        [12, 39, 13, 15, 40, 34, 10],
        [16, 27, 12, 16, 20, 19, 16],
        [37, 22, 25, 18, 21, 37, 38],
    ]
)
len(a)
a
a[0]
a[0, 3]
a[2:5, 3:6]
a[2:5, 3:]
a[:5, 3:6]
a[:, -1]
a[::2, 3:6:2]
b = np.array([32, 19, 17, 39, 16, 20, 13])
i = np.array([False, True, True, False, False, False, True])
b[i]
b % 2 == 1
b[b % 2 == 1]
i = np.array([False, True, True, False, False, False, True])
np.where(i)
a[2, 3] = 0
a
a[a > 30] = 0
a
x = np.array([12, 14, 51, 8, 11, 9, 5, 4, 25])
sorted(x)
sum(x)
max(x)
min(x)
len(x)
x = [False, True, True, False, False]
sum(x)
x = np.ones((3, 4))
x
x = np.zeros((3, 4))
x
x = np.arange(0, 10, 0.2)
x
np.arange(10)
np.arange(10, step=2)
x = np.array([1, 2, 4, 1, 3, 4, 5, 6, 3])
y = np.array([11, 12, 14, 11, 13, 14, 15, 16, 13])
x.shape == y.shape
x + y
x * y
y / x
y // x
y % x
x**2
x > y
x == y
x % 3 != 0
x = np.arange(100 + 2, 500, 3)  # Vector of numbers divisable by 3 in range 100 to 500
sum(x % 7 == 1)  # Numbers in the above vector whichare divisable by 7
sum(
    np.logical_and(x % 7 == 1, x % 5 == 1)
)  # There is another condition combined with the logical and method.
# عمگرهای منطقی پرکاربرد دیگر نیز در قالب متدهای logical_or logical_not  logical_xor در نامپای در دسترس هستند.
x = np.random.random(10)
x
x + 1
100 * x
# The difference between np.random.rand and np.random.random is that np.random.rand takes any number of integer arguments to specify the shape of the output array, while np.random.random takes a tuple or integer as an argument. Other than that, the functions are similar in that they both generate random numbers that are uniformly distributed between 0 and 1.
np.random.seed(124)
x = np.random.randint(1, 100, 50)
x.shape = (5, 10)
x
x.min()
x.max()
x.sum()
x.mean()
x.std()  # standard deviation
x.cumsum()  # cumulative sum
y = x.cumsum()
plt.plot(y)
x = np.arange(-10, 11, 0.1)
y = x - np.cos(x)
plt.plot(x, y)

x.min(axis=0)
x.max(axis=0)
x.sum(axis=0)
x.mean(axis=0)
x.std(axis=0)
x.min(axis=1)
x.max(axis=1)
x.sum(axis=1)
x.mean(axis=1)
x.std(axis=1)
np.random.seed(129)
x = np.random.random(100).round(3)
x.sort()
x
# Comparing Numpy with Python

import time as tm

N = 1000000

np.random.seed(115)
x = np.random.random(N)
t1 = tm.time()
x = sorted(x)
t2 = tm.time()
t_base = t2 - t1

np.random.seed(115)
x = np.random.random(N)
t1 = tm.time()
x.sort()
t2 = tm.time()
t_numpy = t2 - t1

t_base / t_numpy
# ---------
# In Numpy axis=0 means columns and axis=1 means rows.It's the other way round in Pandas!


# -----------------------------------
# PANDAS
file_ = pd.read_csv("C:\\Tomato First.csv")
file_.info()
file_.head()
file_.columns
file_[file.Sweet > 3]
file_[(file.Sweet > 3) & (file.Color == 2.9)]
file_.columns
x = file_.Price
y = file_["Avg of Totals"]
p.plot(x, y)
p.xlabel("Sweetness")
p.ylabel("Average of totals")
p.hist(x, bins=10)
p.hist(y, bins=10)
# در کتابخانه نامپای، متدهای مربوط به تولید اعداد تصادفی در قفسه random در کتابخانه numpy در دسترس هستند. به همین دلیل، برای فراخوانی آن‌ها لازم است نام قفسه (sub-module) هم قید شود. به عنوان مثال اگر بخواهیم برداری تصادفی از 'a' و 'b' و 'c' ایجاد کنیم، متد choice در بخش random در کتابخانه numpy در دسترس است. پس باید به صورت زیر عمل کنیم.
# Generate a random integer from 0 to 100:
from numpy import random

x = random.randint(100)
print(x)
# ----------------------------
# Generate a random float from 0 to 1:

x = random.rand()
print(x)
# -------------------------------------------
# Generate a 1-D array containing 5 random integers from 0 to 100:

x = random.randint(100, size=(5))
x
print(x)
type(x)
# -------------------------------------------------
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

x = random.randint(100, size=(3, 5))
type(x)
x
print(x)
# --------------------------------------------
# Generate a 1-D array containing 5 random floats:

from numpy import random

# rand() is a numpy library function that returns an array of random samples from the uniform distribution over [0,1] .
x = random.rand(5)

print(x)
# --------------------------------------
# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
from numpy import random

x = random.rand(3, 5)

print(x)
# ---------------------------------------------
# Return one of the values in an array:
random.seed(int(time.time()))
x = random.choice([3, 5, 7, 9])
x
print(x)
# -------------------------------------
# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):

x = random.choice([3, 5, 7, 9], size=(3, 5))
x
print(x)
import matplotlib.pyplot as plt

# ------------------------------------------
# import numpy
import numpy as np

# Using uniform() method
gfg = np.random.uniform(-5, 5, 5000)

plt.hist(gfg, bins=50, density=True)
plt.show()

# ------------------------------------
# import numpy
import matplotlib.pyplot as plt
import numpy as np

# Using uniform() method
gfg = np.random.uniform(2.1, 5.5, 10000)

plt.hist(gfg, bins=20, density=True)
plt.show()
# ----------------------------------------
import matplotlib.pyplot as plt

values = [
    87,
    53,
    66,
    61,
    67,
    68,
    62,
    110,
    104,
    61,
    111,
    123,
    117,
    119,
    116,
    104,
    92,
    111,
    90,
    103,
    81,
    80,
    101,
    51,
    79,
    107,
    110,
    129,
    145,
    139,
    110,
]

plt.hist(values, bins=7, edgecolor="yellow", color="green")
plt.show()
import matplotlib.pyplot as plt

# -----------------------------------------------------
# MATPLOTLIB.PYPLOT COURSE
import numpy as np
import pandas as pd

# import matplotlib.pyplot as plt
# np.arange(3)
# >array([0, 1, 2])
# np.arange(3.0)
# >array([ 0.,  1.,  2.])
# np.arange(3,7)
# >array([3, 4, 5, 6])
# np.arange(3,7,2)
# >array([3, 5])
# For integer arguments the function is roughly equivalent to the Python built-in range, but returns an ndarray rather than a range instance.
# When using a non-integer step, such as 0.1, it is often better to use numpy.linspace.
# dtypedtype, optional
# The type of the output array. If dtype is not given, infer the data type from the other input arguments.
# Read for warnings:https://numpy.org/doc/stable/reference/generated/numpy.arange.html

plt.plot()  # prints an empy canvas
x = np.arange(0, 5, 0.1)
x
print(x)  # doesn't have commas when shown by print function.
y = np.sin(x)
plt.plot(x, y)


# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# Return evenly spaced numbers over a specified interval.
# Returns num evenly spaced samples, calculated over the interval [start, stop].
# The endpoint of the interval can optionally be excluded.
# np.linspace(2.0, 3.0, num=5)
# >array([2.  , 2.25, 2.5 , 2.75, 3.  ])
# np.linspace(2.0, 3.0, num=5, endpoint=False)
# >array([2. ,  2.2,  2.4,  2.6,  2.8])
# np.linspace(2.0, 3.0, num=5, retstep=True)
# >(array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
# You must run the code below together to get a single plot


N = 8
y = np.zeros(N)
y
x1 = np.linspace(0, 10, N, endpoint=True)
x1
x2 = np.linspace(0, 10, N, endpoint=False)
x2
plt.plot(x1, y, "o")
plt.plot(x2, y + 0.5, "d")
# plt.plot(x2, y + 0.5, #'d' or 'b' or ...)
plt.ylim([-0.5, 1])  # limits y axis
# >(-0.5, 1)
plt.show()

# Zip function
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
tuple(x)  # Here x is full
for a, b in x:
    print(a + " was zipped with " + b)

tuple(x)  # here x is empty!
a = [1, 2, 3, 4, 5]
b = [4, 5, 7, 8, 9]
x = zip(a, b)
list(x)  # full
list(x)  # empty


x = [1, 2, 3, 54, 7, 8, 56, 63, 442, 878, 3, 2, 8, 79, 876, 875, 343, 3211, 12]
ar1 = np.array(x)
type(ar1)
ar1
y = list()
y += [round(random.randint(0, 300) + random.random(), ndigits=3) for i in range(len(x))]
y
# The basic idea is [f(x) for x in xs if condition]
ar2 = np.array(y)
ar2
ar1.shape
ar1 + ar2
ar1 * ar2
ar1 / ar2
ar1 * 10
select = ar2 < 100
select
ar2[ar2 < 100]
ar2
np.mean(ar2)
np.median(ar2)
np.std(ar2)
np.sort(ar2)

arr = np.linspace(
    1, 22, 6
)  # gives 6 numbers uncluding bounds with equal distance form one another
arr
ar3 = np.array([1, 23, 4, 56])
ar3.shape
ar4 = np.array([[1, 23, 4, 56], [2, 334, 12, 4, 65]])
# this is erroneous because it's not a multidimensional array,
# if you want to make it an object of any kind then specify it as below.
ar4 = np.array([[1, 23, 4, 56], [2, 334, 12, 4, 65]], dtype=object)
ar4
ar4.shape
ar5 = np.array([[1, 23, 4, 56], [2, 334, 12, 4]], dtype=float)
ar5 = np.array([[1, 23, 4, 56, 21, 11], [2, 334, 12, 4, 40, 14]], np.int16)
ar5
ar5.shape
ar5.shape = (4, 3)
ar5
ar5.sum()
ar5[1][2]
ar5[1, 2]  # only if we have a multidimensional array
ar5[1][1] = 38
ar5
ar2.dtype
ar5.dtype
ar6 = np.zeros(10)
ar6
np.ones(10)
ar7 = np.ndarray([])
ar7.shape

# ---------------------------------------------
random.choice(x)  # one choice
random.choices(x, k=7)  # 7 choices with replacement
random.sample(x, 3)  # three choices without replacement
random.randint(0, 100)  # rand int between and including range bounds
random.random()
random.seed(12)
random.random()

os.getcwd()
os.chdir("c:\\")
os.chdir("c:\\Users\\M\\Desktop\\VS_Projects\\Practice")
m.log(m.e)
m.e
m.pi
d.getcontext()
d.getcontext().prec = 10
d.Decimal(12)
d.Decimal(m.pi)
d.Decimal(m.pi).sqrt()
d.Decimal(f"{m.pi}")
d.Decimal(f"{m.pi}").sqrt()
m.degrees(m.acos(1 / 2))
m.degrees(1)
m.degrees(1 * 2 * m.pi)
d = {}
type(d)
s = set()
type(s)
for i in range(4):
    print(i)
l = []
l += [1, 2, 3, 1, 3, 4, 5, 6]
l
d1 = {(1, 2): 9, 2: 4, (15, "ds"): 0, "hello": [1, 2, 3]}
d1
type(d1)
d2 = {"dryer": [(1, 2, 3), "Goodbye"]}
d1 + d2  # Error
d1["dryer"] = d2["dryer"]
d1
d1.update({"NItz": {"a": 12, (1, 4): [7, 6, 5]}})
d1
d3 = {1: 12, "Just": [1, (1, 2)]}
d1 |= d3
d1
d1 |= {"prime": {"a": 2}}
d1
d4 = d2 | d3
d4
d1.items()
for object in d1.items():
    print(object)
k, v = d1.keys(), d1.values()
k
v
t = ()
t + (1,)
t
t = (1,) + (2, 3)
t
a = 10
b = a
s = set()
s
len(s)
s + {
    1,
    2,
    3,
    4,
}  # Error
s.union(
    {
        1,
        2,
        3,
        4,
    }
)
s
s = s.union(
    {
        1,
        2,
        3,
        4,
    }
)
s
s2 = {}
s2.union(s)  # Error
print(b)
a += 1
print(a)
print(b)
A = list(range(10))
B = A
A.append(["k", a, b])
print(A)
print(B)
print(
    1,
    2,
    3,
    4,
)
msg = "the lord of the rings"
msg.title()
l = "0110101111010001".split("0")
"0".join(l)
l1 = [12, 334, 64, 2, 4, 5457, 56, 6]
l2 = l1.copy()
l2
# -------------------------------------------
el = list()
for i in range(4):
    el += [int(input("Enter a number:"))]
el
# --------------------------------
import sklearn
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=1000, n_features=20, n_redundant=5, n_informative=15, random_state=7
)
plt.plot(X)


# -----------------------------------
def f(x):
    return x**3 - 4 * x**2 + 8 * x - 600


def g(x):
    return -(x**4) - 24 * x**3 + 12 * x**2 + 45 * x + 1000


import matplotlib.pyplot as plt
import numpy as np

f1 = np.array([f(x) for x in np.linspace(-10, 10, 1000)])
f2 = np.array([g(x) for x in np.linspace(-10, 10, 1000)])

# Below plots f1 and f2 based on their indexes, which is wrong.
plt.plot(f1, label="f(x)")
plt.plot(f2, label="g(x)")
# below plots correctly
x = np.linspace(-10, 10, 100)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, g(x), label="g(x)")
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# To find the intersection of two plots (on the plot, so it's not a solution!)
compare = f(x) > g(x)
itemindex = np.where(compare == True)  # returns a tuple fo size 2
itemindex[0][0]
# itemindex = np.where(compare == True)[0][0]  # You can also write this way.
x_intersect = x[itemindex[0][0]]
y_intersect = f(x_intersect)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.scatter(x_intersect, y_intersect, c="black")
# plt.semilogy()
# plt.semilogx()
x1 = np.linspace(-100, 100, 10000)
# plt.semilogx()
plt.semilogy(1000000)
plt.xlim(-30, 10)
plt.plot(x1, g(x1))
