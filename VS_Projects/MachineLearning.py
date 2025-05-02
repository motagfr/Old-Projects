from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from imblearn.over_sampling import SMOTE
from sklearn import datasets
from sklearn.datasets import make_classification, make_regression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Lasso, LinearRegression, LogisticRegression, Ridge
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier, MPLRegressor
from sklearn.preprocessing import StandardScaler, minmax_scale
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

#####################################
# KNN CLASSIFIER

iris = datasets.load_iris()
iris
iris.keys()
iris.target_names
iris.feature_names
iris.data
iris.target_names


irisDF = pd.DataFrame(iris.data, columns=iris.feature_names)
irisDF["Target"] = iris.target

plt.figure(figsize=(5, 4))
scatter = plt.scatter(
    irisDF["sepal length (cm)"], irisDF["petal length (cm)"], c=irisDF["Target"]
)
plt.legend(
    handles=scatter.legend_elements()[0],
    labels=["setosa", "versicolor", "virginica"],
    loc="lower right",
    title="Iris Type",
)
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")
plt.tight_layout()
plt.grid()


X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=10
)
X_train
X_test
y_train
y_test
X_train, X_val, y_train, y_val = train_test_split(
    X_train, y_train, test_size=0.2, random_state=10
)

acc = (
    []
)  # or alternatively Neighbors = [1,3,5,7,9,11,13,15,17,19,21,23,25] and n_neighbors=i for i in N.
for i in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred_val = knn.predict(X_val)
    y_pred_val
    y_pred_test = knn.predict(X_test)
    y_pred_test
    print(
        f"Validation prediction accuracy score for K={i}:",
        accuracy_score(y_val, y_pred_val),
    )
    print(
        f"Test prediction accuracy score for K={i}:",
        accuracy_score(y_test, y_pred_test),
    )
    acc.append(accuracy_score(y_val, y_pred_val))
acc
fig, ax = plt.subplots()
ax.plot(range(1, 11), acc, marker="d")
plt.xticks(range(1, 11))
ax.legend()
plt.xlabel("K parameter")
plt.ylabel("Validation Accuracy Score")
plt.title("K vs Predition Accuracy")
plt.tight_layout()
plt.grid()


#################################################
# Linear Regression
X, y = make_regression(
    n_samples=100, n_features=1, n_informative=1, noise=20, bias=50, random_state=10
)
plt.scatter(X, y, color="blue")

plt.xticks()
plt.yticks()

plt.xlabel("x")
plt.ylabel("y")

plt.grid()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)
linreg = LinearRegression()

# Train the model using the training sets
linreg.fit(X_train, y_train)

# Make predictions using the testing set
y_pred_linreg = linreg.predict(X_test)
print(y_pred_linreg)

# The coefficients
print("Intercept: \n", linreg.intercept_)
print("Coefficients: \n", linreg.coef_)


# We cannot calculate accuracy for a Linear/ Multiple regression model. \
# ONLY Mean Squared Error (MSE).Root Mean Squared Error (RMSE).Mean Absolute Error (MAE)\
# We can use it for logistics regression though.

# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred_linreg))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred_linreg))

# Plot outputs
plt.scatter(X_train, y_train, color="black")
plt.scatter(X_test, y_test, color="blue")
plt.scatter(X_test, y_pred_linreg, color="red")

plt.plot(X_test, y_pred_linreg, color="orange", linewidth=2, linestyle="dotted")

plt.xticks()
plt.yticks()

plt.xlabel("x")
plt.ylabel("y")

plt.grid()

# MULTIPLE LINEAR REGRESSION

# Create data set.
X, y = make_regression(
    n_samples=100, n_features=10, n_informative=4, noise=40, bias=20, random_state=10
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)

linreg = LinearRegression()

# Train the model using the training sets
linreg.fit(X_train, y_train)

# Make predictions using the testing set
y_pred_linreg = linreg.predict(X_test)

# The coefficients
print("Intercept: \n", linreg.intercept_)
print("Coefficients: \n", linreg.coef_)

# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred_linreg))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred_linreg))

# LASSO REGULARIZED LINEAR REGRESSION MODEL
lasso = Lasso(alpha=5)

# Train the model using the training sets
lasso.fit(X_train, y_train)

# Make predictions using the testing set
y_pred_lasso = lasso.predict(X_test)

# The coefficients
print("Intercept: \n", lasso.intercept_)
print("Coefficients: \n", lasso.coef_)

# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred_lasso))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred_lasso))

# RIDGE REGULARIZED LINEAR REGRESSION MODEL

ridge = Ridge(alpha=5)

# Train the model using the training sets
ridge.fit(X_train, y_train)

# Make predictions using the testing set
y_pred_ridge = ridge.predict(X_test)

# The coefficients
print("Intercept: \n", ridge.intercept_)
print("Coefficients: \n", ridge.coef_)

# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred_ridge))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred_ridge))

# SUMMARY

print("No regularized linear Coefficients: \n", linreg.coef_)
print()
print("Lasso Coefficients: \n", lasso.coef_)
print()
print("Ridge Coefficients: \n", ridge.coef_)

###################################################### FROM HERE DOWNWARD C IS THE INVERSE OF RHE COEFFICIENT OF REGULARIZATION. THE SMALLER, THE STRONGER THE REG. FUNCTION.
# LOGESTIC REGRESSION

# Modeling-Predicting-Cross validating
C = [0.01, 0.05, 0.1, 0.2, 0.5, 1, 5, 10, 15]
ACC = []
for c in C:
    logReg = LogisticRegression(
        C=c, multi_class="multinomial", solver="sag", random_state=0
    )
    logReg.fit(X_train, y_train)
    y_pred = logReg.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(C, ACC, marker="o")
plt.xlabel("Value of C")
plt.ylabel("Accuracy Score")
plt.title("Finding the right C")
plt.xticks(range(1, 30))
plt.grid()

print("The best C is:", C[np.argmax(ACC)])

# Evaluating the optimum Parameter of C, which is 10.

logReg = LogisticRegression(
    C=10, multi_class="multinomial", solver="sag", random_state=0
)
logReg.fit(X_train, y_train)
y_pred = logReg.predict(X_test)
acc_logReg = accuracy_score(y_test, y_pred)

print("Best Logistic Regression accuracy is: ", acc_logReg)

##########################################
# SVM VECTORS

C = [0.01, 0.05, 0.1, 0.2, 0.5, 1, 5, 10, 15, 20]
ACC = []
for c in C:
    svm = SVC(C=c, kernel="linear", random_state=0)
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

# Plotting

plt.figure(figsize=(8, 6))
plt.plot(C, ACC, marker="o")
plt.xlabel("Value of C")
plt.ylabel("Accuracy Score")
plt.title("Finding the right C")
plt.xticks(range(1, 30))
plt.grid()

print("The best C is:", C[np.argmax(ACC)])

svm = SVC(C=15, kernel="linear", random_state=0)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred)

print("Best SVM accuracy is: ", acc_svm)

###################################################
# Decision Trees

ACC = []
max_depth_options = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for trees in max_depth_options:
    dt = DecisionTreeClassifier(max_depth=trees, random_state=0)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
plt.plot(max_depth_options, ACC, marker="o")
plt.xlabel("Value of max_depth")
plt.ylabel("Accuracy Score")
plt.title("Finding the right max_depth of Tree")
plt.xticks(range(1, 30))
plt.grid()

print(
    "The best max_depth is:", max_depth_options[np.argmax(ACC)]
)  # it's 8. Now we tune other parameters.

CC = []
max_features_options = ["auto", None, "sqrt", 0.95, 0.75, 0.5, 0.25, 0.10]
for trees in max_features_options:
    dt = DecisionTreeClassifier(max_features=trees, max_depth=8, random_state=0)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC


plt.figure(figsize=(8, 6))
pd.Series(ACC, max_features_options).plot(kind="bar", color="darkred", ylim=(0.5, 0.9))
plt.xlabel("Value of max_features")
plt.ylabel("Accuracy Score")
plt.title("Finding the right max_features of Tree")
plt.show()

print(
    "The best max_features is:", max_features_options[np.argmax(ACC)]
)  # The best is None.Now we tune min_samples_leaf_options.

ACC = []
min_samples_leaf_options = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
for trees in min_samples_leaf_options:
    dt = DecisionTreeClassifier(
        min_samples_leaf=trees, max_depth=8, max_features=None, random_state=0
    )

    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

ACC = []
min_samples_leaf_options = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
for trees in min_samples_leaf_options:
    dt = DecisionTreeClassifier(
        min_samples_leaf=trees, max_depth=8, max_features=None, random_state=0
    )

    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
plt.plot(min_samples_leaf_options, ACC, marker="o")
plt.xlabel("Value of min_samples_leaf")
plt.ylabel("Accuracy Score")
plt.title("Finding the right min_samples_leaf of Tree")
plt.grid()

print(
    "The best min_samples_leaf is:", min_samples_leaf_options[np.argmax(ACC)]
)  # is 5.

dt = DecisionTreeClassifier(
    min_samples_leaf=5, max_depth=8, max_features=None, random_state=10
)

dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
acc_dt = accuracy_score(y_test, y_pred)

print("BestDecision Tree accuracy is: ", acc_dt)

##################################################################
# Random Forests

ACC = []
n_estimaor_options = [
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    95,
    100,
]  # number of trees in the jungle.
for trees in n_estimaor_options:
    rf = RandomForestClassifier(n_estimators=trees, random_state=0)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
plt.plot(n_estimaor_options, ACC, marker="o")
plt.xlabel("Value of n_estimaor")
plt.ylabel("Accuracy Score")
plt.title("Finding the right number of trees")
plt.grid()

print("The best n_estimaor is:", n_estimaor_options[np.argmax(ACC)])  # is 75

ACC = []
max_features_options = ["auto", None, "sqrt", 0.95, 0.75, 0.5, 0.25, 0.10]
for trees in max_features_options:
    rf = RandomForestClassifier(max_features=trees, n_estimators=75, random_state=0)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
pd.Series(ACC, max_features_options).plot(kind="bar", color="darkred", ylim=(0.5, 0.9))
plt.xlabel("Value of max_features")
plt.ylabel("Accuracy Score")
plt.yticks(np.linspace(0.5, 1, 10))
plt.title("Finding the right max_features of Tree")
plt.show()

print("The best max_features is:", max_features_options[np.argmax(ACC)])

ACC = []
min_samples_leaf_options = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
for trees in min_samples_leaf_options:
    rf = RandomForestClassifier(
        min_samples_leaf=trees, max_features=0.95, n_estimators=75, random_state=10
    )
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_valid)
    y_pred = rf.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
plt.plot(min_samples_leaf_options, ACC, marker="o")
plt.xlabel("Value of n_estimaor")
plt.ylabel("Accuracy Score")
plt.title("Finding the right number of trees")
plt.grid()

print("The best min_samples_leaf is:", min_samples_leaf_options[np.argmax(ACC)])

rf = RandomForestClassifier(
    min_samples_leaf=5, max_features=0.95, n_estimators=75, random_state=0
)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred)

print("Best Random Forests accuracy is: ", acc_rf)

####################################################
# XGBOOST


from xgboost import XGBClassifier

ACC = []
n_estimaor_options = [
    20,
    25,
    30,
    35,
    40,
    45,
    50,
    55,
    60,
    65,
    70,
    75,
    80,
    85,
    90,
    95,
    100,
]
for trees in n_estimaor_options:
    xgb = XGBClassifier(
        n_estimators=trees,
        objective="multi:softmaxc",
        eval_metric="merror",
        num_class=4,
        seed=0,
    )
    xgb.fit(X_train, y_train)
    y_pred = xgb.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
plt.plot(n_estimaor_options, ACC, marker="o")
plt.xlabel("Value of n_estimaor")
plt.ylabel("Accuracy Score")
plt.title("Finding the right number of trees")
plt.grid()

print("The best n_estimaor is:", n_estimaor_options[np.argmax(ACC)])

ACC = []
n_max_depth = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for trees in n_max_depth:
    xgb = XGBClassifier(
        max_depth=trees,
        n_estimators=60,
        objective="multi:softmaxc",
        eval_metric="merror",
        num_class=4,
        seed=0,
    )
    xgb.fit(X_train, y_train)
    y_pred = xgb.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))

ACC

plt.figure(figsize=(8, 6))
plt.plot(n_max_depth, ACC, marker="o")
plt.xlabel("Value of n_max_depth")
plt.ylabel("Accuracy Score")
plt.title("Finding the right max depth")
plt.grid()

print("The best n_max_depth is:", n_max_depth[np.argmax(ACC)])

xgb = XGBClassifier(
    max_depth=6, n_estimators=60, objective="multi:softmaxc", num_class=4, seed=0
)

xgb.fit(X_train, y_train)
y_pred = xgb.predict(X_valid)
acc_xgb = accuracy_score(y_valid, y_pred)

print("Best XGBoost accuracy is: ", acc_xgb)

#####################################
# NEURAL NETWORKS

ACC = []
for i in range(2, 7):
    for j in range(2, 7):
        nn = MLPClassifier(hidden_layer_sizes=(i, j), random_state=0)

        nn.fit(X_train, y_train)
        y_pred = nn.predict(X_valid)
        ACC.append(accuracy_score(y_valid, y_pred))
        print(i, j, accuracy_score(y_valid, y_pred))
print(len(ACC))

# Data to plot.
x, y = np.meshgrid(range(2, 7), range(2, 7))
z = np.array(ACC).reshape(len(x), len(y))

fig = plt.figure(figsize=(8, 8))

ax = plt.contourf(y, x, z, origin="upper", extend="both")
fig.colorbar(ax)

plt.xlabel("First Layer Units")
plt.ylabel("Second Layer Units")
plt.yticks(range(2, 7))
plt.xticks(range(2, 7))
plt.title("Finding the right solver")
plt.show()


ACC = []
solvers = ["lbfgs", "sgd", "adam"]
for solver in solvers:
    nn = MLPClassifier(solver=solver, hidden_layer_sizes=(4, 5), random_state=0)

    nn.fit(X_train, y_train)
    y_pred = nn.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))
    print(solver, accuracy_score(y_valid, y_pred))

plt.figure(figsize=(8, 6))
pd.Series(ACC, solvers).plot(kind="bar", color="darkred", ylim=(0.5, 0.9))
plt.xlabel("Solver")
plt.ylabel("Accuracy Score")
plt.yticks(np.linspace(0, 1, 10))
plt.title("Finding the right solver")
plt.show()

print("The best solver is:", solvers[np.argmax(ACC)])

ACC = []
activations = ["identity", "logistic", "tanh", "relu"]
for function in activations:
    nn = MLPClassifier(
        activation=function, solver="adam", hidden_layer_sizes=(4, 5), random_state=0
    )

    nn.fit(X_train, y_train)
    y_pred = nn.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))
    print(function, accuracy_score(y_valid, y_pred))

plt.figure(figsize=(8, 6))
pd.Series(ACC, activations).plot(kind="bar", color="darkred", ylim=(0.5, 0.9))
plt.xlabel("Activation Functions")
plt.ylabel("Accuracy Score")
plt.yticks(np.linspace(0, 1, 10))
plt.title("Finding the right activation function")
plt.show()

print("The best activation function is:", activations[np.argmax(ACC)])

ACC = []
rates = [0.001, 0.01, 0.05, 0.1, 0.5, 1]
for rate in rates:
    nn = MLPClassifier(
        learning_rate_init=rate,
        activation="relu",
        solver="adam",
        hidden_layer_sizes=(4, 5),
        random_state=0,
    )

    nn.fit(X_train, y_train)
    y_pred = nn.predict(X_valid)
    ACC.append(accuracy_score(y_valid, y_pred))
    print(rate, accuracy_score(y_valid, y_pred))

plt.figure(figsize=(8, 6))
pd.Series(ACC, rates).plot(kind="bar", color="darkred", ylim=(0.5, 0.9))
plt.xlabel("Learning Rates")
plt.ylabel("Accuracy Score")
plt.yticks(np.linspace(0, 1, 10))
plt.title("Finding the right learning rate")
plt.show()

print("The best learning rate is:", rates[np.argmax(ACC)])

nn = MLPClassifier(
    learning_rate_init=0.01,
    activation="relu",
    solver="adam",
    hidden_layer_sizes=(4, 5),
    random_state=0,
)

nn.fit(X_train, y_train)
y_pred = nn.predict(X_test)
acc_nn = accuracy_score(y_test, y_pred)
print("Best Neural Network accuracy is: ", acc_nn)

print("Number of layers in this neural network:", len(nn.coefs_))

for i in range(len(nn.coefs_)):
    print("Matrix size of layer ", i, " is:", nn.coefs_[i].shape)

nn.coefs_[1]

nn.intercepts_[1]

################################################
# FINDING THE BEST MODEL

# ------------>Accuracy Comparison<------------
models = ["KNN", "LogReg", "SVM", "DT", "RF", "XGB", "NN"]
acc_scores = [acc_knn, acc_logReg, acc_svm, acc_dt, acc_rf, acc_xgb, acc_nn]
print("Models\tAccuracy")
print("-------\t-------")
for i in range(7):
    print(str(models[i]) + "\t" + str(acc_scores[i]), end="\n")

# ------------>Finding the Best Algorithm<----------

plt.rcParams["figure.figsize"] = (12, 9)
plt.bar(
    models, acc_scores, color=["blue", "green", "red", "yellow", "purple", "orange"]
)
plt.ylabel("accuracy scores")
plt.title("Model Comparison based on Accuracy")
plt.show()

################################################
# SAVING THE MODEL

import pickle

pickle.dump(nn, open("d:\\myNNmodel.pickle", "wb"))
newNN = pickle.load(open("myNNmodel.pickle", "rb"))

newNN

newNN.coefs_[0]

###################################
# IMBALANCE DATASET SMOTE only done on train set
from collections import Counter

from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification

X, y = make_classification(
    n_classes=2,
    class_sep=2,
    weights=[0.1, 0.9],
    n_informative=3,
    n_redundant=1,
    flip_y=0,
    n_features=20,
    n_clusters_per_class=1,
    n_samples=1000,
    random_state=10,
)
print(
    "Original dataset shape %s" % Counter(y)
)  # Original dataset shape Counter({1: 900, 0: 100})
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)
print(
    "Resampled dataset shape %s" % Counter(y_res)
)  # Resampled dataset shape Counter({0:900, 1: 900})


############################################
# STANDARDIZING A DATAFRAME...These functions belong to sklearn.preprocessing so can take DataFrames as input.


sc = StandardScaler()
X = sc.fit_transform(X)

X = minmax_scale(
    X,
    feature_range=(0, 1),
    copy=False,
)  # Doesn't make mean=0 and std=1.The above model does so.

[(X[:, i].mean(), X[:, i].std()) for i in range(0, 20)]

####################################################
