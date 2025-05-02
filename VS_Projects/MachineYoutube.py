# %%
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from IPython.display import Image
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import copy
import seaborn
# %%
mg = pd.read_csv("magic04.data")
mg
mg.columns = [
    "fLength",
    "fWidth",
    "fSize",
    "fConc",
    "fConc1",
    "fAsym",
    "fM3Long",
    "fM3Trans",
    "fAlpha",
    "fDist",
    "class",
]
mg

# %% Convert class to int

mg.loc[:, "class"] = (mg["class"] == "g").astype(int)
mg["class"] = pd.to_numeric(mg["class"], errors="coerce")
# Here though values get set to 0-1, the column well
# still have the object form so change the type to int!
# There will be errors later in fitting models!
mg.iloc[:, -1]

# mg["class"].unique()
# (mg["class"] == "g")  # This is a true/false pandas series.
# mg.loc[:, "class"]  # this is a pandas series.
# # y[(y['class']=='g')].astype(int) #This is another way

# %% plot the columns to compare
# plt.hist(mg['fLength'],density=True,)
for label in mg.columns[:-1]:
    plt.hist(
        mg[mg["class"] == 1][label],
        density=True,
        color="blue",
        label="gamma",
        alpha=0.7,
    )
    plt.hist(
        mg[mg["class"] == 0][label], density=True, color="Red", label="gamma", alpha=0.7
    )
    plt.ylabel("Probablity")
    plt.xlabel(label)
    plt.legend()
    plt.show()

# %% train test splitting
mg.sample(frac=1)  # shuffles the data
X = mg.iloc[:, :-1]
y = mg.iloc[:, -1]
type(mg.iloc[:, -1])
# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.25, random_state=0
)

# %% Standardize the X set because some values are extremely large

x = StandardScaler()
X = x.fit_transform(X)

# %% Data us imbalanced
print("Number of zeros:", len(mg[mg["class"] == 0]))
print("Number of ones:", len(mg[mg["class"] == 1]))

# %% We need to balance the data
# y_train = y_train.astype('int')
print("Before Sampling:")
print(y_train.value_counts())
res = RandomOverSampler(random_state=0)
X_train, y_train = res.fit_resample(X_train, y_train)
print("------------------------------")
print("After Sampling:")
print(y_train.value_counts())

# %% KNN Model

for i in [5, 6, 7, 13, 15, 19, 20, 25, 27, 30, 32]:
    knn_model = KNeighborsClassifier(n_neighbors=i)
    knn_model.fit(X_train, y_train)
    y_pred = knn_model.predict(X_test)
    print("N=", i)
    print(classification_report(y_true=y_test, y_pred=y_pred))
    print("\n------------------------------")

# %% Precision and Recall
# https://en.wikipedia.org/wiki/Precision_and_recall?oldformat=true

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Precisionrecall.svg/800px-Precisionrecall.svg.png"  # Replace with your image URL
urllib.request.urlretrieve(image_url, "downloaded_image.jpg")  # Download the image

# Display the image in your notebook
display(Image(filename="downloaded_image.jpg"))

# Image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Precisionrecall.svg/800px-Precisionrecall.svg.png") #This is enough

# %% NAIVE BAYES MODEL
bayes_model = GaussianNB()
bayes_model.fit(X_train, y_train)
y_pred = bayes_model.predict(X_test)
print("Gaussian Naive Bayes")
print(classification_report(y_true=y_test, y_pred=y_pred))

# %% LOGISTIC REGRESSION MODEL
lg_model = LogisticRegression(max_iter=1000)
lg_model.fit(X_train, y_train)
y_pred = lg_model.predict(X_test)
print("Logistic Regression")
print(classification_report(y_true=y_test, y_pred=y_pred))

# %% SVM MODEL
svm_model = SVC()
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)
print("SVM")
print(classification_report(y_true=y_test, y_pred=y_pred))

# %% NEURAL NETWORKS MODEL
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
seoul_bike_sharing_demand = fetch_ucirepo(id=560) 
  
# data (as pandas dataframes) 
X = seoul_bike_sharing_demand.data.features 
y = seoul_bike_sharing_demand.data.targets 
  
# metadata 
print(seoul_bike_sharing_demand.metadata) 
  
# variable information 
print(seoul_bike_sharing_demand.variables) 

#X and y are both dataframes
#I run the part below because code completion doesn't work otherwise. 
# and the columns have names as well.
# import os
# os.getcwd()
X.to_csv('d:\\VS_Projects\\Practice\\X.csv',index=0)
y.to_csv('d:\\VS_Projects\\Practice\\y.csv',index=0)
X=pd.read_csv('d:\\VS_Projects\\Practice\\X.csv')
y=pd.read_csv('d:\\VS_Projects\\Practice\\y.csv')

# %%
X.columns
# %%

# %%
