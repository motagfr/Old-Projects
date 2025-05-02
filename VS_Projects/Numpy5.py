import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (
        x**5
        - 11.7 * x**4
        - 64.46 * x**3
        + 667.992 * x**2
        + 995.68 * x
        - 2972.93
    )


# Q1
# x = np.linspace(-10, 15, endpoint=True, num=2500)
x = np.arange(-10, 15, 0.01)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, x * 0, label="Y=0")
plt.legend()

# Q2

y = np.zeros_like(x)
compare = f(x) > y
compare = compare.astype(int)
diff_arr = np.diff(compare)
indexes = np.where((diff_arr == -1) | (diff_arr == 1))[0] + 1
x[indexes]
root_sum = np.sum(x[indexes])

# Q3
x = np.arange(-10, 15, 0.01)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, x * 0, label="Y=0")
plt.legend()
plt.scatter(x[indexes], y[indexes], c="black")


# np.diff calculates the difference of two adjacent cells of an array.
# it returns an array with one cell smaller than the original.
# c = np.array([0, 1, 1])
# diff_arr1 = np.diff(c)
# np.where(diff_arr1==1)
# len(c)
# len(diff_arr1)
