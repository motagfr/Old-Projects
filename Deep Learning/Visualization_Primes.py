#%%
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import plotly.express as px

data = pd.read_csv(
    "C:\\Users\\M\\Desktop\\Deep Learning\\First_1000_Prime_Numbers.txt",
    sep=",",
    header=None,
)
data.iloc[0]
type(data.iloc[0])
data = np.array(data.iloc[0])
len(data)
np.max(data)
type(data)


def plot_distribution_in_interval(interval_beginning, interval_end) -> plt.show:
    i = int(interval_beginning)
    j = int(interval_end)
    # l=[0] * (j-i)
    # l
    # print(i, j, j - i)
    l = np.zeros(j - i)
    for p in data:
        if p > j:
            break
        elif p >= i:
            l[p - i] = p

    index_primes = np.where(l != 0)[0]
    distribution_primes = [index_primes[0]]
    for i in range(1, len(index_primes)):
        distribution_primes += [index_primes[i] - index_primes[i - 1]]

    plt.plot(l[np.where(l != 0)], distribution_primes)
    plt.scatter(l[np.where(l != 0)], distribution_primes, color="red", s=10)
    plt.grid()
    plt.text(
        0.3,
        0.9,
        f"The greatest prime gap is: {np.max(distribution_primes)}",
        ha="center",
        va="center",
        fontsize=12,
        transform=plt.gca().transAxes,
    )


def multiple_intervals_plot(i, j):
    plt.figure(figsize=(12, 12))
    plt.suptitle(f"{i}-{j}", size=20)
    plt.subplot(2, 2, 1)
    plot_distribution_in_interval(i, i + (j - i) / 4)
    plt.title(f"{i}-{i+(j - i) / 4}")
    # plt.xticks([])
    plt.subplot(2, 2, 2)
    plot_distribution_in_interval(i + (j - i) / 4 + 1, i + 2 * (j - i) / 4)
    plt.title(f"{i+(j - i) / 4+1}-{i+2*(j - i) / 4}")
    plt.subplot(2, 2, 3)
    plot_distribution_in_interval(i + 2 * (j - i) / 4, i + 3 * (j - i) / 4)
    plt.title(f"{i+2*(j - i) / 4+1}-{i+3*(j - i) / 4}")
    plt.subplot(2, 2, 4)
    plot_distribution_in_interval(i + 3 * (j - i) / 4 + 1, j)
    plt.title(f"{i+3*(j - i)/4+1}-{j}")
    plt.tight_layout()
    plt.show()


def show_histogram_distances(interval_beginning, interval_end, normalize=False):
    i = int(interval_beginning)
    j = int(interval_end)
    # l=[0] * (j-i)
    # l
    # print(i, j, j - i)
    l = np.zeros(j - i)
    for p in data:
        if p > j:
            break
        elif p >= i:
            l[p - i] = p

    index_primes = np.where(l != 0)[0]
    distribution_primes = [index_primes[0]]
    for i in range(1, len(index_primes)):
        distribution_primes += [index_primes[i] - index_primes[i - 1]]
        # distribution_primes.append(distance_primes[i]-distance_primes[i-1])
    element_counts = Counter(distribution_primes)
    sorted_counter = sorted(element_counts.items())
    values, frequencies = zip(*element_counts.items())
    if normalize == True:
        total_count = sum(frequencies)
        normalized_frequencies = [freq / total_count for freq in frequencies]
        frequencies = normalized_frequencies
    plt.bar(values, frequencies)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.title("Histogram of Values")


def histogram_intervals_plot(i, j, normalize=False):
    normalize1 = normalize
    plt.figure(figsize=(5, 5))
    plt.suptitle(f"{i}-{j}", size=20)
    plt.subplot(2, 2, 1)
    show_histogram_distances(i, i + (j - i) / 4, normalize=normalize1)
    plt.title(f"{i}-{i+(j - i) / 4}")
    plt.subplot(2, 2, 2)
    show_histogram_distances(
        i + (j - i) / 4 + 1, i + 2 * (j - i) / 4, normalize=normalize1
    )
    plt.title(f"{i+(j - i) / 4+1}-{i+2*(j - i) / 4}")
    plt.subplot(2, 2, 3)
    show_histogram_distances(
        i + 2 * (j - i) / 4, i + 3 * (j - i) / 4, normalize=normalize1
    )
    plt.title(f"{i+2*(j - i) / 4+1}-{i+3*(j - i) / 4}")
    plt.subplot(2, 2, 4)
    show_histogram_distances(i + 3 * (j - i) / 4 + 1, j, normalize=normalize1)
    plt.title(f"{i+3*(j - i)/4+1}-{j}")
    plt.tight_layout()
    plt.show()
#%%
multiple_intervals_plot(1, 4000)
histogram_intervals_plot(1, 4000)
#%%
multiple_intervals_plot(1, 8000)
histogram_intervals_plot(1, 8000, True)
#%%
multiple_intervals_plot(1, 800)
histogram_intervals_plot(1, 800)
#%%

#
# ax[0,1].plot_distribution_in_interval(11,20)
# ax[0,1].set_title('11-20')
# ax[1,0]=plot_distribution_in_interval(21,30)
# ax[1,0].set_title('21-30')
# ax[1,1]=
# ax[1,1].set_title('31-40')
# plt.tight_layout()
# plt.show()


# fig,ax=plt.subplots(2,2)
# original_width, original_height = fig.get_size_inches()
# new_width = original_width * 1.5  # Increase width by 50%
# new_height = original_height * 1.5
# fig.set_size_inches(new_width, new_height)
# ax[0,0].set_title('1-10')
# ax[0,0]=plot_distribution_in_interval(1,10)

# fig, ax = plt.subplots()

# # Plot some data
# ax.plot([1, 2, 3], [2, 4, 3])

# # Enlarge the figure while maintaining aspect ratio
# original_width, original_height = fig.get_size_inches()
# new_width = original_width * 1.5  # Increase width by 50%
# new_height = original_height * 1.5
# fig.set_size_inches(new_width, new_height)

# plt.tight_layout()
# plt.show()

# plt.scatter(range(i, j), l, color="red", s=10)
# plt.show()

# def convert_to_boolean(l):
#     return [int(bool(x)) for x in l]

# l2 = convert_to_boolean(l)
# # l2
# # np.argsort(l)
# type(np.where(l!=0)) #Tuple


# import tensorflow as tf; print(tf.__version__)
# from tensorboard import version; print(version.VERSION)

# # Create a random vector of size 10
# vec = np.random.uniform(low=0, high=1, size=10)
# print("Array: ", vec)
# # Find the index of the maximum value
# max_index = np.argsort(vec)[-1]
# # np.sort(vec)
# # Replace the maximum value by 0
# vec[max_index] = 0
# print("Final_Array: ", vec)
