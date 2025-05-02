s = "Hello World"
s.islower()
u = 2 * "hello"
2.0 * "ab"
o = 2 + 15
int("3")
-2 - -3
-12 - -14 - -3
--23
--3 * 3 + 2 ** --1
name = input("Enter a value:")
type(name)

3 - 1 / 223

x = int(input("Enter the number:"))
if x % 4 == 0 and x % 5 == 0.0 and x % 200 == 0:
    print("You are correct")
else:
    print("You are wrong")

2.3 == 0.3 + 2
print(3 + 2)
bool(0)

"1S" < "S"
1 + "s"
help(TypeError)
print("dsgfsdg", 2544)
print("gfdjbdf", round(4.252743, 3))
print("gfdjbdf" + str(round(4.252743, 3)))


if 50 < 30:
    print(1)
elif 50 < 200:
    print(2)
else:
    print(3)
# --------------------------
if 50 < 300:
    print(1)
elif 50 < 200:
    print(2)
elif 20 < 400:
    print(3)
else:
    print(4)

# -----------------------
if 50 < 100:
    print(1)
if 50 < 20:
    print(2)
else:
    print(3)
# ------------------------
if 50 < 100:
    print(1)
if 50 < 200:
    print(2)
else:
    print(3)

# -----------------------------
print("bmi=", 23)
# ..............................
"""
for pixel in picture:
    pixel=change(pixel)

for char in "statistics":
    print(char)
"""
import numpy as np

list(range(2, 10))
list(np.arange(2, 10))
np.arange(2, 10)

a = 10
f"{a+1}"
f"{list(range(1,10))}"
a
###########################
n = 6
fact = 1
for i in range(1, n + 1):
    fact = fact * i
    print(fact)

n = 6
j = 1
fact = 1
while j <= n:
    fact = fact * j
    print(fact)
    j += 1
####################################
x = print(2)
type(x)

from math import ceil

ceil(12.2)


def cube(x):
    """Makes a cubic function.

    Args:
        x (float): Any number entered as input

    Returns:
        float: Triples the input and adds it to 10.
    """
    a = 10
    y = x**3 + a
    return y


cube(12.4)
cube(-1.9)
print(a)


def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact


factorial(10)
factorial(5)


n = 1


def factorial(x):
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
        # n+=1: this gives error.
    return fact


factorial(5)
print(n)
help(cube)


def sum(x=4, y=10):
    return x + y


sum()
sum(5)
sum(34, 12)
sum(x=48, y=3)


def sum(x: int, y: float):
    return x + y


####################################
a = 1
x = "Sharif University of Technology"
len(x)
x[0]
x[6]
for i in range(len(x)):
    print(x[i], end="")
    # print(x[i])
# alt+cap+arrow is interesting
# alt+shift+arrow also is interesting!
for i in x:
    print(i, end="*")

x[1:5]  # end is exclusive
x[1:10:2]
x[:10]  # The first up to and not including the tenth
x[len(x)]
x[len(x) - 1]
x[-1]
x[-2]
x[-1] == x[len(x) - 1]
"U" in x
"Sh" in x
"z" in x
# str is immutable
x[0] = "g"
x = "H" + x[1:]
x

# value.method()
"Hello World".lower()
l = []
l.append([121, 115, 949])
l
l.extend([1, 54, 42, 4, 267, 6])
l
l.clear()
l += [121, 115, 949]
l.insert(1, 150)
l
min(l)
max(l)
sum(l)
l = input("Enter a list:")
type(l)
l
l = eval(l)
type(l)
l
eval("4+1")
eval("[i**.5 for i in range(11)]")
l = eval("[i**.5 for i in range(11)]")
l
l.count(0)
l.index(2)
l.index(2, 2)
l.insert(4, "He")
l
l.remove(2.23606797749979)
l
l.pop(6)
l.reverse()
l
l2 = ["df", "df", "ffg", "htt"]
"/".join(l2)
"*".join([1, 2, 3, 4, 5])  # error
"dsg gf hg fgr".split(" ")
l2.split("/")  # error
l = [2, 134, 5, 5, 43, 54, 23, 13, 4, 5, 7, 6, 868, 89, 0]
l.sort()
l.reverse()
l
l.sort(reverse=True)
l
l = [2, 134, 5, 5, 43, 54, 23, 13, 4, 5, 7, 6, 868, 89, 0]
sorted(l)
l
l = sorted(l)
l
#################################
# Important note

l1 = [1, 2, 3, 4, 5]
l2 = l1
l2.append(6)
l2, l1  # both lists have changed!
# instead
l2 = l1[0:]
l2
l2.append(6)
l2, l1
# another method
l2 = l1.copy()
l2
#####################
# The code below cannot remove the shared elements between the two lists why?
# because you're iterate on a list whose elements are being changed.So the list is variable.
l1 = [1, 2, 4, 6, 3, 56, 32, 87, 3, 2, 76]
l2 = [1, 35, 7, 3, 7, 2, 35, 87]
for i in l1:
    if i in l2:
        l1.remove(i)
l1

# instead
l1 = [1, 2, 4, 6, 3, 56, 32, 87, 3, 2, 76]
l2 = [1, 35, 7, 3, 7, 2, 35, 87]
l1c = l1.copy()
for i in l1c:
    if i in l2:
        l1.remove(i)
l1

# Or
l1 = [1, 2, 4, 6, 3, 56, 32, 87, 3, 2, 76]
l2 = [1, 35, 7, 3, 7, 2, 35, 87]

print([x in l1 for x in l2])
[x for x in l1 if x not in l2]
sorted(x for x in l1 if x not in l2)

# or
# set(l1)-set(l2)


###########################
# This doesn't work either. Because l1 is changing.
l1 = [1, 2, 4, 6, 3, 56, 32, 87, 3, 2, 76]
l2 = [1, 35, 7, 3, 7, 2, 35, 87]
for e in l2:
    if e in l1:
        l1.remove(e)
l1

#
l1 = [1, 2, 4, 6, 3, 56, 32, 87, 3, 2, 76]
[a for a in l1 if a % 2 == 0]

##########################


"sgjhgjfk  mytrsv vmvcvx".count(" ")
"sgjhgjfk  mytrsv vmvcvx".count("")
"sgjhgjfk  mytrsv vmvcvx"
x = ()
# Tuple is immutable
y = 2
type(y)
y = (2,)
type(y)
z = (3, "dsf", [5])
u = y, z
u
t = 1, 2, 43, 5
t
type(t)
# Tuple can be used for easy value swapping,
# and returning a number of variables in functions
x = 15
y = 10
y, x = x, y
x
y


def test():
    return 42, 95


e = test()
e
r = range(4, 20, 3)
type(r)
tuple(r)
r[0]
r[0] = 5  # range is immutable
# list is mutable
l = []
l.extend(range(1, 10, 2))
l
# range() is an iterable type

s = {}  # this dictionary
type(s)
s1 = set()
type(s1)
s1 = {1, 2}
s1
type(s1)
s2 = set()
s2.update(s1)
s2
s2.issubset(s1)
# In python values are either scaler or non-scaler
capitals = {"USA": "Washington D.C.", "France": "Paris", "India": "New Delhi"}
capitals["France"]

d = {}  # empty dictionary

numNames = {1: "One", 2: "Two", 3: "Three"}  # int key, string value
numNames[2]
decNames = {
    1.5: "One and Half",
    2.5: "Two and Half",
    3.5: "Three and Half",
}  # float key, string value
decNames[1.5]
decNames[1.5][2:7]

items = {
    ("Parker", "Reynolds", "Camlin"): "pen",
    ("LG", "Whirlpool", "Samsung"): "Refrigerator",
}  # tuple key, string value
items[("LG", "Whirlpool", "Samsung")]

items.keys()
items.values()

romanNums = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}  # string key, int value
# The key should be unique and an immutable object.

# a dictionary with a list as a key is not valid, as the list is mutable:
dict_obj = {["Mango", "Banana"]: "Fruit", ["Blue", "Red"]: "Color"}

emptydict = dict()

numdict = dict(I="one", II="two", III="three")
numdict

# Use the get() method to retrieve the key's value even if keys are not known. It returns None if the key does not exist instead of raising an error.

numNames = {1: "One", 2: "Two", 3: "Three"}
print(numNames.get(1), numNames.get(2), numNames.get(3))

capitals = {"USA": "Washington DC", "France": "Paris", "India": "New Delhi"}
print(capitals.get("USA"), capitals.get("France"))
print(capitals.get(1), capitals.get(2))
print(capitals.get())
capitals.keys()
capitals.keys()[0]  #!!!!!
capitals.items()
capitals.items()[0]  #'dict_items' object is not subscriptable
capitals.values()
for key in capitals:
    print("Key = " + key + ", Value = " + capitals[key])
capitals.update({"Sweden": "Stockholm"})
capitals
dic = capitals.pop("India")
dic
capitals
del capitals["France"]
capitals

##################################################
x = "EVery day is a new day."
dir(x)
x = x.lower()
L = x.split(" ")
L
" ".join(L)
sorted([2, 3, 4321, 24, 5, 6, 6666, 324, 45667, 789, 976])
################################################
article = "In Syria, Trump Distills a Foreign Policy of Impulse, and Faces the Fallout By Peter Baker and Lara Jakes (NYTimes) Oct. 10, 2019 WASHINGTON — No one should have been surprised, and yet it seems that everyone was. President Trump made clear long ago that he wanted to get out of the Middle East, … … … . At the same time, the Kurds have been counterattacking, firing off shells at Turkish border villages as the danger of escalation spiralled."

# Find the most repeated letter.
d = dict()
s = set()

for char in article:
    s.add(char)
for char in s:
    d[char] = 0

for char in article:
    for key in d.keys():
        if char == key:
            d[char] += 1

d

sorted_dic = sorted((value, key) for (key, value) in d.items())
sorted_dic
type(sorted_dic)
sorted_dic[-1:]
[(key, value) for (key, value) in d.items()]

# Another way
d1 = dict()
for char in article:
    if char in d1.keys():
        d1[char] += 1
    else:
        d1[char] = 1

# Note
d1["a"] = d1.get("a", 0) + 1
d1
############################################
import os

os.getcwd()
# os.chdir('c:\\...')
import math

math.pi
dir(math)
help(_ _doc__)

import time

t1 = time.time()
# some code here
t2 = time.time()

t2 - 21  # is the time it takes to run
#############################
import random

x = ['a', 'b', 'c', 'd', 'e']

# random.seed(24)

y = random.choice(x)
print(y)
y = random.choices(x, k = 20)
print(y)
y = random.sample(x, 2)
print(y)
y = random.randint(10, 100)
print(y)
y = random.random() # produces a random number between 0 and 1
print(y)

######################################


a = 1000
b = 20000

# analytical way
# method 1.1

N7 = b//7 - (a-1)//7
NT = b - a + 1

p = N7/NT
print(1 - (1-p)**7 - 7*(p)*(1-p)**6)

1/7
# method 1.2
print(1 - (1-1/7)**7 - 7*(1/7)*(1-1/7)**6)


# method 2 : simaulation with random number generation

# random.seed(25)

N = 10000
r = []

for i in range(N):
    x = random.choices(range(a, b + 1), k = 7)
    
    n = 0
    for e in x:
        if e % 7 == 0:
            n += 1
    
    r.append(n >= 2)
print(sum(r)/N)
#############################################
import numpy as np
a=np.array([1,24,5,6,3,52,35,76,2,3,4,5,7,5])
type(a)
a.dtype
#numpy arrays have only one type.
b=np.array([1,254,67,34,'s'])
b.dtype
b
b.dtype=np.int_
b
c=a<10
c
a[c]
a[a%2==0]
np.mean(a)
np.std(a)
np.random.uniform(0,1,5)
np.random.normal(0.0,1.0,15)
d=np.random.normal(0.0,1.0,15)
d.sort()
d
##########################
(lambda x: x + 1)(2)
add_one = lambda x: x + 1
add_one(2)
""" def add_one(x):
    return x + 1 """
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

