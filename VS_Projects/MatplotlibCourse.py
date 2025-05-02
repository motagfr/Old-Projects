import arabic_reshaper
import bidi.algorithm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def text_fa(x):
    x = arabic_reshaper.reshape(x)
    x = bidi.algorithm.get_display(x)
    return x


d = pd.read_excel("C:/iran_statscenter_inflation_m12m.xlsx", na_values=["", "-"])

# cleaning years in the first row (index = 0)
for i in range(1, d.shape[1]):
    if pd.isna(d.iloc[0, i]):
        d.iloc[0, i] = d.iloc[0, i - 1] + 1 / 12

year = d.iloc[0, 1:]

for j in range(2, d.shape[0]):
    plt.clf()
    plt.figure(figsize=(14, 6))
    font = {"family": "B Mitra", "size": 21}
    plt.rc("font", **font)
    plt.xticks([x for x in range(1382, 1403, 2)])
    plt.rcParams["axes.titlepad"] = 22
    plt.ylabel(text_fa("نرخ تورم"))

    inflation_bold = d.iloc[j, 1:]
    title = d.iloc[j, 0]

    # plotting the context
    for i in range(2, d.shape[0]):
        inflation = d.iloc[i, 1:]
        plt.plot(year, inflation, linewidth=2, alpha=0.25, c="gray")

    plt.axvline(x=1400, c="royalblue", alpha=0.8, linestyle="--")
    plt.axhline(
        y=max(inflation_bold[year < 1400]), c="royalblue", alpha=0.8, linestyle=":"
    )

    plt.plot(year, inflation_bold, linewidth=3.6, alpha=0.85, c="darkred")
    plt.title(text_fa(title))
    plt.ylim((np.min(inflation_bold) - 5, np.max(inflation_bold) + 8))

    plt.yticks(
        [
            x
            for x in range(
                10 * round(np.min(inflation_bold) / 10) - 5,
                round(np.max(inflation_bold)) + 10,
                10,
            )
        ],
        [
            str(x) + "%"
            for x in range(
                10 * round(np.min(inflation_bold) / 10) - 5,
                round(np.max(inflation_bold)) + 10,
                10,
            )
        ],
    )

    plt.savefig("D:/" + title + ".png")

    print(title)
########################################################

d = pd.read_excel("C:\\countries-pgdp-2020.xlsx")
plt.scatter(d.population, d.gdp, alpha=0.6)
#
plt.clf()
plt.hist(d.population)
plt.xlabel("population")
plt.show()

plt.hist(d.gdp)
plt.xlabel("gdp")
plt.show()
#
d["population_log10"] = np.log10(d.population)
d["gdp_log10"] = np.log10(d.gdp)

plt.hist(d.population_log10)
plt.xlabel("population")
plt.show()

plt.hist(d.gdp_log10)
plt.xlabel("gdp")
plt.show()
#
plt.scatter(d.population_log10, d.gdp_log10, alpha=0.65, s=75, c="steelblue")
#
plt.scatter(d.population_log10, d.gdp_log10, alpha=0.65, s=75, c="steelblue")
plt.xlabel("population")
plt.ylabel("gdp")

plt.scatter(
    d.population_log10[d.iso2c == "IR"],
    d.gdp_log10[d.iso2c == "IR"],
    c="darkred",
    alpha=0.9,
    s=120,
)
plt.text(
    d.population_log10[d.iso2c == "IR"],
    d.gdp_log10[d.iso2c == "IR"],
    "Iran",
)
#
plt.clf()
plt.figure(figsize=(28, 15))

font = {"family": "Garamond", "size": 20}
plt.rc("font", **font)

np.corrcoef(np.log10(d.population), np.log10(d.gdp))

plt.scatter(d.population_log10, d.gdp_log10, alpha=0.65, s=75, c="steelblue")
plt.xlabel("population")
plt.ylabel("gdp")

plt.scatter(
    d.population_log10[d.iso2c == "IR"],
    d.gdp_log10[d.iso2c == "IR"],
    c="darkred",
    alpha=0.9,
    s=120,
)

texts = []
for x, y, s in zip(d.population_log10, d.gdp_log10, d.country):
    texts.append(plt.text(x, y, s, alpha=0.3, horizontalalignment="center"))

# plt.savefig('D:\\countries-scatter-Iran-01.png')
#
MIN = np.log10(65 * 10**6)
MAX = np.log10(100 * 10**6)
similar_countries = np.logical_and(MIN < d.population_log10, d.population_log10 < MAX)
for x, y, s in zip(
    d.population_log10[similar_countries],
    d.gdp_log10[similar_countries],
    d.country[similar_countries],
):
    texts.append(
        plt.text(x, y, s, alpha=0.95, horizontalalignment="center", fontweight="bold")
    )
texts
type(plt.text)
type(plt.text(x, y, s, alpha=0.95, horizontalalignment="center", fontweight="bold"))
plt.axvline(MIN, linestyle="dashed", alpha=0.4)
plt.axvline(MAX, linestyle="dashed", alpha=0.4)

plt.savefig("D:\\countries-scatter-Iran-02.png")
d.country[similar_countries]
#
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

#####################################################
p_china = [
    612,
    660,
    724,
    828,
    926,
    1000,
    1076,
    1177,
    1241,
    1291,
    1331,
    1369,
    1407,
    1414,
    1421,
    1428,
    1434,
    1439,
]
year_china = [
    1955,
    1960,
    1965,
    1970,
    1975,
    1980,
    1985,
    1990,
    1995,
    2000,
    2005,
    2010,
    2015,
    2016,
    2017,
    2018,
    2019,
    2020,
]
plt.plot(year_china, p_china)
plt.plot(
    year_china, p_china, c="#FE0000"
)  # c is Hex code of the color and can have aliases as well.
plt.plot(year_china, p_china, c="darkred")
plt.plot(year_china, p_china, c="hotpink")
plt.plot(
    year_china, p_china, marker="|"
)  # shows datapoints on the plot with a shape.(o,d,x,X,+,<,*,^,p,P,1,2,...,',',..)

year_india = [
    2020,
    2019,
    2018,
    2017,
    2016,
    2015,
    2010,
    2005,
    2000,
    1995,
    1990,
    1985,
    1980,
    1975,
    1970,
    1965,
    1960,
    1955,
]
p_india = [
    1380,
    1366,
    1353,
    1339,
    1325,
    1310,
    1234,
    1148,
    1057,
    964,
    873,
    784,
    699,
    623,
    555,
    499,
    451,
    410,
]
plt.clf()  # will be written when you deploy a python file not in interactive mode.It clear what's been shown before.
plt.plot(year_china, p_china, c="darkred", marker="x", label="China")
plt.plot(year_india, p_india, c="darkorange", marker="+", label="India")
plt.legend()
plt.ylabel("Million")
plt.title("Population Over Time")
# plt.yticks([500, 750, 1000, 1250],
#            ['500 M', '750 M', '1000 M', '1250 M'])
# or
plt.yticks(
    [x for x in range(500, 1500, 100)], [str(x) + " M" for x in range(500, 1500, 100)]
)
plt.xticks([x for x in range(1955, 2020, 5)], rotation=-20)
plt.text(
    1993, 430, "data source: worldometers"
)  # Note that the location is determined by the ticks.
# plt.text(1995, 150, 'data source: worldometers')#Show info outside the plot area.
plt.show()  # will be written when you deploy a python file not in interactive mode.It outputs what's been drawn so far.

year_china_future = [2020, 2030, 2040, 2050]
p_china_future_projection = [1439, 1420, 1380, 1310]
year_india_future = [2020, 2030, 2040, 2050]
p_india_future_projection = [1380, 1510, 1610, 1670]
plt.clf()
plt.plot(year_china, p_china, c="darkred", label="China")
plt.plot(year_india, p_india, c="darkorange", label="India")
plt.plot(year_china_future, p_china_future_projection, c="darkred", linestyle="--")
plt.plot(year_india_future, p_india_future_projection, c="darkorange", linestyle="--")
plt.legend()
plt.ylabel("Population")
plt.title("Population Over Time and Future Projection")
plt.show()

d = pd.read_excel("C:/iran_statscenter_inflation_m12m.xlsx", na_values=["", "-"])
d
for i in range(1, d.shape[1]):
    if pd.isna(d.iloc[0, i]):
        d.iloc[0, i] = d.iloc[0, i - 1] + 1 / 12

inflation = d.iloc[2, 1:]
year = d.iloc[0, 1:]
plt.plot(year, inflation)
plt.show()
# plt.clf()
# plt.figure(figsize = (10, 6)) #makes the figure with specified width and length to give better visuals.
# plt.plot(year, inflation)
# plt.xticks([x for x in range(1382, 1403, 2)])
# plt.yticks([x for x in range(10, 60, 10)], [str(x) + "%" for x in range(10, 60, 10)])
# # plt.tight_layout()  # tight_layout automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
# font = {"family": "Garamond", "size": 21}
# plt.rc(
#     "font", **font
# )  # This equals plt.rc(group = 'font', family = 'Garamond', size = 21)
# plt.savefig("D:/inflation_total.png")


# Subplots

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(
    1, 2, 1
)  # the figure has 1 row, 2 columns, and this plot is the first plot.
plt.plot(x, y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(
    1, 2, 2
)  # the figure has 1 row, 2 columns, and this plot is the second plot.
plt.plot(x, y)
plt.show()

# So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x, y)

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x, y)

plt.show()

# Using context to draw
plt.clf()
plt.rcParams
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x = np.arange(0, 10, 0.2)
y = x**2
z = np.sin(x)
x
y
with plt.rc_context(
    {"axes.grid": True, "grid.linewidth": 0.75, "lines.linestyle": "dashed"}
):
    plt.subplot(121)
    plt.plot(x, y)

plt.subplot(122)
plt.plot(x, z)
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

d = pd.read_excel("C:/countries-pgdp-2020.xlsx")
d
d.population
plt.scatter(d.population, d.gdp, alpha=0.6)
plt.clf()
plt.hist(d.population)
plt.xlabel("population")
plt.show()

plt.hist(d.gdp)
plt.xlabel("gdp")
plt.show()

################################################
###########################################################
# Create some data for the scatter plot
x = np.random.randn(100)
y = np.random.randn(100)
group = np.random.choice([1, 2, 3], size=100)
type(group)
print(group)
# Create a scatter plot with different colors for each group
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=group)
cbar = plt.colorbar(scatter)
# Get the handles and labels for the legend
handles, labels = scatter.legend_elements()
# Create the legend
ax.legend(
    handles, labels, loc="lower right"
)  # you assign labels yourself :labels = ['setosa','versicolor','virginica']

plt.show()
##############################################

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.rand(100)

# Create a scatter plot with color based on the z variable
fig, ax = plt.subplots()
# scatter = ax.scatter(x, y, c=z, cmap='viridis')
# scatter = ax.scatter(x, y, c=z, cmap='plasma')
scatter = ax.scatter(x, y, c=z, cmap="coolwarm")

# Add a color bar to the plot
cbar = plt.colorbar(scatter)

plt.show()
###############################################
# Create a frequency plot

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# fig, ax = plt.subplots()

df = pd.DataFrame({"numbers": [2, 4, 1, 4, 3, 2, 1, 3, 2, 4]})
# df['numbers'].value_counts().plot(ax=ax, kind='bar', xlabel='numbers', ylabel='frequency')
df["numbers"].value_counts().plot(kind="bar", xlabel="numbers", ylabel="frequency")

plt.show()
###################################
# Below simulation creates a function of data point.Remember that.
X, y = make_regression(
    n_samples=100, n_features=1, n_informative=1, noise=20, bias=50, random_state=10
)
data = pd.DataFrame(pd.Series(X))  # Error
X
list = [float(i) for i in X]
list
df = pd.DataFrame(pd.Series(list))
df[0].value_counts().plot(kind="bar", xlabel="numbers", ylabel="frequency")

df2 = pd.DataFrame(pd.Series(y))
df2.value_counts().plot(kind="bar", xlabel="numbers", ylabel="frequency")

df3 = pd.concat([df, df2], axis=1)
df3.columns = ["X", "y"]
df3
df3.nunique()
#############################################
# Finding correlation

import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv("dataset.csv")

# Compute the correlation matrix using Pearson correlation coefficient
corr_matrix = df.corr(method="pearson")


# second

import matplotlib.pyplot as plt
import seaborn as sns

# Create a heatmap of the correlation matrix
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

# Show the plot
plt.show()
