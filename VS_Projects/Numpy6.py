import matplotlib.pyplot as plt
import numpy as np



def g(x):
    return (
        -(x**6)
        + 21.7 * x**5
        - 52.54 * x**4
        - 1312.59 * x**3
        + 5684.24 * x**2
        + 12929.7 * x
        - 29729.3
    )


# Q1

x = np.arange(-8, 13, 0.01)
y = np.zeros_like(x)
compare = g(x) > y
compare = compare.astype(int)
diff_arr = np.diff(compare)  # is one element smaller than compare
indexes = np.where((diff_arr == -1) | (diff_arr == 1))[0] + 1
indexes
print(indexes)
plt.plot(x, g(x), label="g(x)")
plt.plot(x, x * 0, label="Y=0")
plt.scatter(x[indexes], y[indexes], c="black")
plt.legend()

# Q2
roots = x[indexes]
g_values = np.array([g(i) for i in x])
g_values.shape
extremum = np.array([])
extremum
# print(extremum)
for i in range(5):
    if i % 2 == 0:
        g_between_roots = g_values[indexes[i]: indexes[i + 1]]
        extremum = np.append(
            extremum, np.max(g_between_roots)
        )  # this is how you append to an array
    else:
        g_between_roots = g_values[indexes[i]: indexes[i + 1]]
        extremum = np.append(extremum, np.min(g_between_roots))
        # there is also np.insert(arr,[1,2,3])
extremum
extremum_sum = sum(extremum)
extremum_sum

# Q3

indexes2 = np.where(
    np.isin(g_values, extremum)
)  # returns a tuple whose second element can't be accessed!
plt.plot(x, g(x), label="g(x)")
plt.plot(x, x * 0, label="Y=0")
plt.scatter(x[indexes], y[indexes], c="black")
# plt.scatter(x[indexes], 0, c="black") ValueError: x and y must be the same size
plt.scatter(x[indexes2], extremum, c="red")
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("G(x) with roots and extremums")

# Q4

MAX = np.max(extremum)
