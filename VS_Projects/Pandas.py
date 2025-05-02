import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import scipy.stats as ss
import statsmodels as st


# Pandas Course
pd.__version__

# pd.Series(data, index=index) data can be a list, ndarray, a dictionary or a constant.
mySeries = pd.Series([1, 2, 3, 4, 5, 6], index=["a", "b", "c", "d", "e", "f"])
mySeries
s1 = pd.Series((1, 2, 3, 4, 5, 6))
s1
type(s1)
mySeries["c"]
s1[2]
s1[2:5]
mySeries["c":"f"]  # when you index by string it is stop-inclusive
population_dict = {
    "Ardabil": 1284000,
    "Busheshr": 1174000,
    "Fars": 4904000,
    "Isfahan": 5136000,
    "Tehran": 13323000,
    "Yazd": 1156000,
}

population = pd.Series(population_dict)
population
print(population["Ardabil":"Isfahan"])

print(population["Isfahan":"Ardabil"])
print(population["Isfahan":"Ardabil":-1])

population_dict_2 = {
    "Ardabil": 1284000,
    "Tehran": 13323000,
    "Yazd": 1156000,
    "Isfahan": 5136000,
    "Busheshr": 1174000,
    "Fars": 4904000,
}

population_2 = pd.Series(population_dict_2)

print(population_2.index[2], population_2.values[2])  # چاپ عنصری که در خانه ۲ است
population_2.values #Numpy ndarray.
population_2.index #index type
print(population.index[2], population.values[2])  # چاپ عنصری که در خانه ۲ است
print(population_2["Ardabil":"Isfahan"])
pd.Series(np.random.rand(6))
area_dict = {
    "Ardabil": 17800,
    "Busheshr": 22743,
    "Fars": 122608,
    "Isfahan": 107029,
    "Tehran": 18814,
    "Gilan": 76469,
}

area = pd.Series(area_dict)
area
province = pd.DataFrame({"Population": population, "Area": area_dict})
province
countries = {
    "Country": ["Belgium", "India", "Brazil"],
    "Capital": ["Brussels", "New Delhi", "Brassilia"],
    "Population": [1234, 1234, 1234],
}
countriesDF = pd.DataFrame(countries)
countriesDF
print(type(countries))
print(type(countriesDF))
countriesDF.index
pd.DataFrame(np.arange(0, 10))
df1 = pd.DataFrame(np.resize(np.arange(0, 10), (5, 4)))
df1
df1[:, 1:3]  # KeyError: (slice(None, None, None), slice(1, 3, None))
df1.index
df1.index = ["Ports", "Staff", "Cameras", "Cargo Trucks", "Working Hours"]
df1.index
df1.columns
df1.columns = ["Gate1", "Gate2", "Gate3", "Gate4"]
df1
df2 = df1.T
df2
df2.sort_values("Cameras", inplace=True)
# df2.to_csv("D:\\Federal_Stimulus_Data.csv")
df2
# Below is how you can use numpy and pandas together.
n = np.arange(1000, 10000)
df2 = pd.DataFrame(index=n, dtype=np.float64)
df2
df2["Linear"] = n + 10
df2["Square"] = n**2 - n + 10
df2["nlog(n)"] = n * np.log2(n) + 10
df2
plt.plot(n, df2["Linear"], label="Linear")
plt.plot(n, df2["Square"], label="Square")
plt.plot(n, df2["nlog(n)"], label="nlog(n)")
plt.legend()
# plt.xscale("log")
plt.xscale("linear")
# plt.yscale("log", base=2)
plt.yscale("linear")
fd = pd.read_csv("c:\\Federal_Stimulus_Data.csv")
fd.to_csv("D:\\Federal_Stimulus_Data11.csv")#here an unnncessary index column is added. use below two codes to fix this.
fd = pd.read_csv("D:\\Federal_Stimulus_Data11.csv")
fd #you can see the extra added column here. instead:
fd.to_csv("D:\\Federal_Stimulus_Data.csv",index=False)#doesn't include a 0-indexed column.
# fd = pd.read_csv("D:\\Federal_Stimulus_Data.csv",index_col=0)
fd
# fd = pd.read_csv("D:\\Federal_Stimulus_Data.csv",index_col=[0,1])#multi-indexed
fd.columns
fd.columns=fd.columns.str.strip()#remove spaces from the left and right of a string.
fd.columns
fd.columns=fd.columns.str.replace(' ','')
fd.columns
fd.columns=fd.columns.str.replace('/','or')
fd.columns=fd.columns.str.replace('%','Percent')
fd.columns=fd.columns.str.replace('#','Number')
fd.columns
fd.RevisedContractEndDate

fd.head(2)
fd.index
fd.select_dtypes(exclude='object')#returns only numeric data.
fd.shape
fd.columns
fd.index
fd.to_csv("D:\\Federal_Stimulus_Data.csv",index=False)
# in the read csv assign the header parameter as 0/none and see what happens. df.shape
#Below remove spaces from the names of columns so that you can use column names as attributes.
# ro remove spaces from the beginning and end of a column name use df.col.str.strip()

#Handling Time in CSV files
fd = pd.read_csv("c:\\Federal_Stimulus_Data.csv",header=2)#First method
fd.head(2)
fd = pd.read_csv("c:\\Federal_Stimulus_Data.csv")#First method
fd.head(2)
fd.info()#here you see time treated as object. below is one solution
fd = pd.read_csv("c:\\Federal_Stimulus_Data.csv",parse_dates=['Estimated Start Date','Actual Start Date','Actual Completion Date'])
fd.info()

fd = pd.read_csv("c:\\Federal_Stimulus_Data.csv")#Second method
fd['Estimated Start Date']=pd.to_datetime(fd['Estimated Start Date'])
fd.info()
#check also pd.to_numeric() pd.to_timedelta()
########################################################
fd = pd.read_csv("D:\\Federal_Stimulus_Data.csv")
fd["StimulusThreshold"]=fd["StimulusFunding"]>500000000
type(fd["StimulusThreshold"])
#you can write like this, but don't!Because it's naive.
fd["StimulusThreshold2"]='NO'
fd.loc[fd["StimulusFunding"]>500000000,"StimulusThreshold2"]='Yes'
fd.head()
fd["StimulusThreshold2"]=fd["StimulusThreshold2"].map({'Yes':True,'No':False})
fd.head()
##################################################
#creating a plot can be done directly using Pandas without using Matplotlib!
df_out=(fd.query('0<StimulusFunding<1000000').groupby(['ProjectName'])[['StimulusFunding']].mean().sort_values('StimulusFunding'))
df_out
ax=df_out.plot(kind='bar',y='StimulusFunding',title='Funding per Project') #You write x='blobblob' for non-index columns.
ax=df_out.plot(kind='scatter',x='ProjectName',y='StimulusFunding',title='Funding per Project') #this is educational only, with error!
fd.columns
#or you can use Matplotlib
fig,ax=plt.subplots()
plt.scatter(x=fd.StimulusTrackerID,y=fd.StimulusFunding)
ax.grid()
ax.set_title('BlobBlobBlob')
plt.show()
################################################


fd.columns
fd.StimulusTrackerID.values  #numpy.ndarray
fd.StimulusTrackerID.value_counts() #pandas.core.series.Series
fd.StimulusTrackerID.nunique(dropna=False)
fd.StimulusTrackerID.nunique()
fd.count()#Number of non-NA elements in a DataFrame.Returns Series.
fd.nunique() ##Number of non-NA unique elements in a DataFrame.Returns Series.
fd.ContractValue.value_counts()#How many of each value in a column.Gives series.
fd.ProjectName.value_counts() #pandas.core.series.Series
fd.ProjectName.value_counts().index
Ratio=fd.nunique()/fd.count()
Ratio[Ratio>=.02] #pandas.core.series.Series
fd.describe()

fd.columns.unique()
fd.columns.nunique()
fd.values #ndarray
fd.nunique(axis=1)
fd.iloc[13548] # pandas.core.series.Series
fd.iloc[13548].values #ndarray
fd.iloc[13548].values.shape
fd.iloc[13548].unique() #ndarray
len(fd.iloc[13548].unique()) #ndarray
fd.iloc[13548].nunique() #ndarray NaN's are excluded

fd['PaymentRecipientInitials']=fd["PaymentRecipient"].str[0:1]#1 is excluded
# fd["Payment Recipient"].str[0]
type(fd["PaymentRecipient"])
fd.PaymentRecipientInitials
fd.PaymentRecipient.index

fd.info()
fd.count()
fd.count().sort_values()
fd.count().sort_index()
fd.isna().sum()#Number of Null values in the Dataframe.
fd=fd.fillna(method='ffill')
# fd=fd.fillna(0)
fd=fd.reset_index()
fd
fd.isna().sum()
fd.to_csv("D:\\Federal_Stimulus_FillNa.csv")
#######################################
fd = pd.read_csv("c:\\Federal_Stimulus_Data.csv")

fd.columns=fd.columns.str.strip()#remove spaces from the left and right of a string.
fd.columns=fd.columns.str.replace(' ','')
fd.columns=fd.columns.str.replace('/','or')
fd.columns=fd.columns.str.replace('%','Percent')
fd.columns=fd.columns.str.replace('#','Number')

fd['BigFundingProjects']=fd.StimulusFunding>100000000
fd.head(2)
fd.drop('BigFundingProjects',axis=1,inplace=True)
fd.StimulusFunding[fd.StimulusFunding>100000000].sort_values(ascending=False)
dff=fd.StimulusFunding[fd.AllOtherFunding>10000000000].sort_values(ascending=False)
dff.index
df2=fd.iloc[dff.index]
# df2.set_index('')
fd.iloc[9207]
fd['OverallFuning']=fd.StimulusFunding+fd.AllOtherFunding
df=fd.query('StimulusFunding>=100000000 and AllOtherFunding<=100000000').sort_values('OverallFuning')
df
#Apply function and its vectorised substitue.
fd.apply(lambda row:row['StimulusFunding']/1000000,axis=1)#pandas.core.series.Series
fd.StimulusFunding/1000000 #this is the vectorised version of the above
######
#Copy method for modifying a slice of the DataFrame.
fd.columns
fd_peanut=fd.query('StimulusFunding<1000000')
fd_peanut['InfrastructureHelp']=fd.query('FundingCategory=Infrastructure')#this gives error use below instead.
fd_peanut=fd.query('StimulusFunding<1000000').copy()
fd_peanut
condition=fd_peanut['FundingCategory']=='Infrastructure'
fd_peanut['InfrastructureHelp']=fd_peanut[condition].loc[:,['FundingCategory']]
fd_peanut[condition].loc[:,['FundingCategory']]
fd_peanut.query('FundingCategory=="Infrastructure"')


##########################################
#try to chain commands instead of creating a dataframe for each command. Use a paranthesis for putting all inside.
df_out=(fd.query('0<StimulusFunding<1000000').groupby(['ProjectName'])[['StimulusFunding']].mean().sort_values('StimulusFunding'))
df_out
#############################################

#HOW TO  USE QUERIES
# total_rows['ColumnID'] = total_rows['ColumnID'].astype(str)
fd = pd.read_csv("D:\\Federal_Stimulus_Data.csv")
fd.head(2)
fd.duplicated().sum()
type(fd.duplicated())
fd[:, 3:6]  # error
data = fd.values
data[:, 3:6]  # not error
fd.loc[
    0:10,
    [
        "ProjectName",
        "ProjectDescription",
        "FundingSource",
        "StimulusFunding",
        "PercentofFundsSpent",
        "FinalSpendingDeadline",
    ]
]
fd[fd["StimulusFunding"] > 500000000].loc[
    :, ["ProjectName", "ProjectDescription", "StimulusFunding"]
]
fd[
    (fd["StimulusFunding"] > 5000000)
    & (fd["PaymentDescription"] == "preventionServices")
]
type(fd["StimulusFunding"] > 500000000) #Series
fd["PaymentDescription"].unique()
fd[
    (fd["StimulusFunding"] > 50000)
    & (fd["PaymentDescription"] == "INFORMATION TECHNOLOGY                  ")
]

fd.loc[fd["StimulusFunding"]>100000000]['FundingSource']
fd[fd["StimulusFunding"]>100000000]['FundingSource']
fd.loc[:,'NewColumn']=fd["FundingSource"] #here the loc property creates a new column.
fd.head(1)

#use query method instead of the above!
AntiEvictFunds=fd.query('ProjectName=="Anti-Eviction Legal Services (DHS)" and StimulusFunding >= 100000')
type(AntiEvictFunds)
AntiEvictFunds.shape
AntiEvictFunds
AntiEvictFunds.to_csv("D:\\Federal_Stimulus_AntiEviction.csv",index=False)
min_fund=10000000
max_fund=200000000
fd.query('StimulusFunding>=@min_fund and StimulusFunding<=@max_fund')
#########################################################
#USE PANDAS STR METHOD INSTEAD OF LAMBDA FUNCTION.
fd.columns
fd["FundingCategory"].apply(lambda x:str(x).upper()) 
fd["FundingCategory"].str.lower()
fd["FundingCategory"].str.capitalize()
#########################################################
 #Don't write the same code for various dataframes.Instead write a function:
 
def process_data(df):
    df['StandardStimulusFunding']=(df['StimulusFunding']-
                                   df['StimulusFunding'].min())/(
                                       df['StimulusFunding'].max()-
                                       df['StimulusFunding'].min())
    return df
process_data(fd)
process_data(fd_peanut)
####################################################
# you can use two ways to rename columns but the second way is best:
#df.columns=['dfds','sdfsdf','dsfsdf',....]
#df=df.rename({'oldcolumnname1':'newcolumnsname1,'oc2':'oc2new',...})
############################################


fd.isnull().sum()
fd.nunique()
dup=fd.duplicated()
type(dup)
fd[dup]
fd[[True,False]]
fd.nunique()/fd.shape[0]
type(fd.nunique())
import sklearn.feature_selection as fs
fd[]
fd["Vendor Name"]
fd["Vendor Name"].is_unique()
fd["Vendor Name"].unique()
fd["Vendor Name"].isin(
    [
        "Legal Aid Society",
        "ARK Systems Electric Corp.",
        "Tycoon Construction, Corp",
        "AMC United Inc.",
        "Kordun Construction Corp.",
    ]
)
specialVedors = fd["Vendor Name"].isin(
    [
        "Legal Aid Society",
        "ARK Systems Electric Corp.",
        "Tycoon Construction, Corp",
        "AMC United Inc.",
        "Kordun Construction Corp.",
    ]
)
fd[specialVedors].to_csv("D:\\Selected Federal Vendors.csv",)


def just_f(x):
    return x // 2

##################################
#Some notes about sorting etc.

# A z-score, also known as a standard score, 
# is a statistical measurement that describes
# how many standard deviations a value is from the mean
# of a group of values. Z-scores are calculated
# by subtracting the population mean from an individual
# raw score and then dividing the difference by the population
# standard deviation.
"""
Z-scores are positive when the raw score is above the mean,
and negative when the raw score is below the mean. 
The z-score for a 95% confidence interval will lie 
between 2 and -2 on the normal distribution curve. 
"""

standardizedStimulus = ss.zscore(fd[["StimulusFunding"]])  # returns DataFrame
standardizedStimulus
plt.plot(standardizedStimulus)
standardizedStimulus.sort_values(ascending=False)
np.sort(standardizedStimulus)
standardizedStimulus = ss.zscore(fd["Stimulus Funding"])  # returns Series
standardizedStimulus.sorted_values(ascending=False)  # Error
fd["Stimulus Funding"].apply(just_f)
fd["Stimulus Funding"].sort_values(ascending=False)
fd["Stimulus Funding"].apply(
    ss.zscore
)  # This gives error because zscore gets a series not single values.
fd["Stimulus Funding"].apply(lambda x: x // 2)
fd.columns
fd["StimulusFunding"] / fd["ContractValue"]
(fd["StimulusFunding"] / fd["ContractValue"]).isna()
pd.DataFrame([1, 2, 0, 4, 5]) / pd.DataFrame([0, 2, 4, 7, 0])
(pd.DataFrame([1, 2, 0, 4, 5]) / pd.DataFrame([0, 2, 4, 7, 0])).isnull()
pd.options.mode.use_inf_as_na = True
(pd.DataFrame([1, 2, 0, 4, 5]) / pd.DataFrame([0, 2, 4, 7, 0])).isnull()
fd.sort_values("StimulusFunding", ascending=False)
fd.sort_values(["StimulusFunding", "AllOtherFunding"], ascending=[False, True])
fd.loc[
    0:200,
    ["ProjectName", "ProjectDescription", "StimulusFunding", "AllOtherFunding"],
].sort_values(["StimulusFunding", "AllOtherFunding"], ascending=[False, True])
# Remember row 1 in pandas begins two steps under that of the CSV file. CSV file assigns 1 to headers( the first line).ُSo when you get a row number in Pandas go two steps forward to find it in the csv file.
#####################################
#GROUPING

# Grouping DataFrame.groupby([columns])[target columns].function()
# DataFrame.groupby([columns])[target columns].agg()
fd.groupby(["ProjectName"])["StimulusFunding"].agg(['mean', 'std', 'min', 'max'])
fd.aggregate({'StimulusFunding':'mean','AllOtherFunding':'sum'})
f = fd.groupby("ProjectName")["StimulusFunding"]  # shows nothing
fd.groupby("ProjectName")["StimulusFunding"].mean().sort_values(ascending=False)
fd.groupby("ProjectName")["StimulusFunding"].mean().sort_values(
    ascending=False
).to_csv("D:\\Federal Mean Help.csv")
fd["PaymentValue"].dropna(inplace=True)#inplace is not recommended anywhere.
fd.groupby(["ProjectName", "StimulusFunding"]).agg(
    {"PaymentValue": ["max", "min", "mean"]}
)
fd.groupby(["ProjectName", "StimulusFunding"]).agg(
    {"PaymentValue": ["max", "min", "mean"]}
).to_csv("D:\\Federal Mean Help.csv")
u = fd.groupby(["ProjectName", "StimulusFunding"]).agg(
    {"PaymentValue": ["mean", "max", "min"]}
)
u
u.sort_values(
    by=("PaymentValue", "mean"), ascending=False, inplace=True
)  # the second tuple in the sort method is redundant because it has unique values.
type(u)
u
u.to_csv("D:\\Federal Mean Help Sorted.csv")

fd.select_dtypes('number')
df=fd.select_dtypes('number')
df.agg(('sum','mean'))
#######################################
#These methods are good to know:
fd['PercentChange']=fd.StimulusFunding.pct_change() #Calculates the rate of change between to consecutive rows.
fd['PercentChange']
plt.plot(fd['PercentChange'])
fd['Change']=fd.StimulusFunding.diff()#The difference between two adjacent rows.
fd['Change']
#####################################
#How to save large data files with less space than CSV, which is awfully spacious!
#There are built in methods to write to different files types which carry their respective names:

fd.to_parquet()
fd.to_feather()
fd.to_pickle("D:\\Federal.pickle")
df=pd.read_pickle("D:\\Federal.pickle")
df
##########################################
#Pandas DataFrames have a style attribute for excel-like formatting.
fd.sort_values('StimulusFunding',
               ascending=False).head()[['ProjectName',
                                        'StimulusFunding']].reset_index(drop=True).style.background_gradient(cmap='Reds')
fd.head()[['ProjectName','StimulusFunding']].sort_values('StimulusFunding',ascending=True).reset_index(drop=True).style.background_gradient(cmap='Reds')
fd.StimulusFunding.background

# Create a sample DataFrame
df = pd.DataFrame(np.random.randn(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
df
# Apply a gradient color scheme to the DataFrame
df.style.background_gradient()
df.style.background_gradient().to_excel("D:\\FederalStyled.xlsx", index=False)

# Create a sample DataFrame
df = pd.DataFrame(np.random.randn(5, 5), columns=['A', 'B', 'C', 'D', 'E'])

# Apply multiple Styler methods to the DataFrame
styled_df = df.style.background_gradient().highlight_max(axis=0).set_caption('Random Data')
# Display the styled DataFrame
styled_df

#Style.text_gradient....
#style.format

# Create a sample DataFrame
df = pd.DataFrame({'A': [1000, 2000, 3000], 'B': [0.1234, 0.5678, 0.9101]})
df
# Apply formatting to the values in the DataFrame. It's huge check it online.
df.style.format({'A': '{:,}', 'B': '{:.2%}'})


##Finally a backslash allows tou to press Enter anywhere in the code! Check the example below.



tomato = pd.read_csv("c:\\Tomato First.csv")
type(tomato)
tomato
tomato.to_csv("D:\\Tomato First_copy.csv", index=False)
tomato.groupby(["Source","Sweet", "Price", "Avg of Totals"])\
    .agg(
    {"Price": "mean", "Avg of Totals": np.mean}
)
tomato.groupby(["Source"]).agg({"Price": "mean", "Avg of Totals": np.sum})
tomato.groupby(["Source"])
tomato["Source"].describe()
tomato.groupby(["Sweet"])[["Source", "Price"]].agg({"Price": "max"})
tomato.groupby(["Sweet", "Source"])[["Price"]].agg(
    {"Price": "max"}
)  # Doesn't creat another column named Price
tomato.groupby(["Sweet", "Source", "Price"]).agg(
    {"Price": "max"}
)  # another column named price is created.
Source = tomato.groupby(["Source", "Sweet"]).agg(
    {"Price": "max"}
)  # Columns within the parathesis become indexes of the new dataframe so they won't be included among columns and can't be used without proper methods.
Source
Source.columns
Source.index
Source.to_csv("D:\\Tomato First Without Indexes.csv", index=False)
Source.to_csv("D:\\Tomato First With Indexes.csv")
tomato.sort_values(["Source", "Sweet"], ascending=False).loc[:, ["Source", "Sweet"]]
tomato.loc[:, ["Source", "Sweet", "Price"]]
tomato.loc[:, ["Source", "Sweet", "Price"]].sort_values(["Price"])
tomato.sort_values(["Price"], ascending=False, inplace=True)
source = (
    tomato.groupby(["Source", "Sweet"])[["Price"]]
    .aggregate({"Price": "max"})
    .sort_values(["Price"], ascending=False)
)
source
type(source)
source.columns  # Here the column 'Sweet' is not included in the dataframe below is the solution.

plt.plot(source[["Sweet"]])
tomato.groupby(["Source", "Sweet"])[["Price"]].aggregate({"Price": "max"})
tomato.loc[:, ["Source", "Sweet", "Price", "Avg of Totals"]].aggregate(
    {"Avg of Totals": "mean"}
)
tomato
tomato.head(2)
tomato.tail()
tomato.shape
tomato.shape[0]
tomato.info()
tomato.info
tomato.describe()
tomato.count()
tomato.nunique()
tomato.nunique(dropna=True)
tomato["Color"].nunique()
tomato["Color"].unique()
tomato["Color"]
tomato.Color
tomato[5:10]  # gives rows
tomato[5:10][2:5]  # gives another selected rows from the new dataframe
tomato[0:3, 2:3]  # gives error use below instead
tomato.iloc[0:3, 2:6]  # Gives access to rows
tomato.iloc[[1, 6, 12], [0, 3, 7]]
tomato.loc[[1, 6, 12], ["Sweet", "Round", "Source"]]  # gives access to rows
tomato.columns
tomato["Source"]  # Gives series
type(tomato["Source"])
tomato[["Source"]]  # Gives DataFrame
type(tomato[["Source"]])
tomato[tomato["Source"] == "Whole Foods"]
priceFrequency = tomato["Price"].value_counts()
priceFrequency
priceFrequency[3.99]
type(priceFrequency)
priceFrequency.shape
plt.bar(
    priceFrequency.index,
    priceFrequency.values,
)
tomato.rename(columns={"Sweet": "Sweetness", "Source": "Seller"}, inplace=True)
tomato
tomato.columns = [col.lower() for col in tomato]
tomato.columns
type(tomato.columns)  # it's index type but can use list comprehension
tomato.dtypes
tomato["round"] = tomato["round"].astype(np.float64)
tomato.dtypes
tomato.duplicated(keep="first")
tomato.drop_duplicates(keep="last", inplace=True)
tomato.isnull()
tomato.isnull().sum()
tomato.dropna(inplace=True, axis=0)
tomato.shape
tomato
tomatoNew = tomato.drop(["round", "acid"], axis=1)
tomatoNew = tomato.drop(["round", "acid"], axis=0)
tomatoNew = tomato.drop(["round", "acid"])  # Error. By default it's rows axis=0
# tomatoNew=tomato.drop(columns=['round','acid'])
tomatoNew
df = pd.DataFrame({"col1": [1, 2, 3], "col2": [2, 3, 4]})
df
df.sum(axis=0)
df.sum(axis=1)
arr = np.array([[1, 2, 3], [2, 3, 4]])
arr
np.sum(arr, axis=0)
np.sum(arr, axis=1)
df2 = pd.DataFrame(arr, columns=["col1", "col2", "col3"], index=["i0", "i1"])
df2  # Turn np arrays into DataFrame as it is, like rows.
df2.sum(
    axis=0
)  # This equals np.sum(arr, axis=0) like when it sums down the columns in numpy.
#############################################
s3 = pd.Series(list('abcde'), pd.date_range('now', periods=5, freq='M'))
s3.loc['2021-03':'2021-04']
# Sometimes we want to mix label and positional indexing methods for the rows and columns,
# somehow combining the capabilities of loc and iloc.

df = pd.DataFrame(np.arange(25).reshape(5, 5), index=list('abcde'),columns=['x','y','z', 8, 9])
df.iloc[:df.index.get_loc('c') + 1, :4]
######################################

fd=pd.read_csv("D:\\Selected Federal Vendors.csv",usecols=['IQ', 'Scores'])