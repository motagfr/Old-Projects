a = 10


def change_variables(a):
    a = a**2


change_variables(a=a)
a


def change_variables2(a):
    a = a**2
    return a


a = change_variables2(a=a)
a
# How to change global variables in Python

counter = 0


def increment():
    global counter
    counter += 1


increment()
counter
increment()
counter

b = 20


def change_globals():
    globals()["b"] = 250


change_globals()
b
