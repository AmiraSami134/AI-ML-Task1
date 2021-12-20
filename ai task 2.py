import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#q1-Read the dataset, convert it to DataFrame and display some from it
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset
#q2-2.	Display structure and summary of the data.
dataset.describe()
#q3-3.	Clean the data (null, duplications)
dataset.sort_values("Title", inplace = True)
dataset.drop_duplicates(subset =["Title","Company","Location","Type","Level","YearsExp","Country","Skills"],keep = "first", inplace = True)
dataset
a = dataset.iloc[:, :-1].values
b = dataset.iloc[:, 3].values
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp_mean = imp_mean.fit(a[:, 0:3])
a[:, 0:3] = imp_mean.transform(a[:, 0:3])
print(a)
dataset
#q4-the most demanding companies for jobs?
y=dataset['Company'].value_counts()
print ('the top 3 companies demanding jobs are', y.index[0:3] )
#q5-Show step 4 in a pie chart
plt.pie(y)
plt.show() 
#q6-Find out what are the most popular job titles.
x=dataset['Title'].value_counts()
print ('the top 3 job titles are', x.index[0:3] )
#q7-Show step 6 in bar chart
fig = plt.figure(figsize = (8, 5))
plt.bar(x.index[0:3], x[0:3], color ='maroon',width = 0.2)
plt.xlabel("job titles")
plt.ylabel("Number of popular jobs title")
plt.title("top 3 job titles")
plt.show()
#q8-Find out the most popular areas?
z=dataset['Location'].value_counts()
print ('the Most popular areas are', z.index[0:5] )
#q9-Show step 8 in bar chart
fig = plt.figure(figsize = (8, 5))
plt.bar(z.index[0:3], z[0:3], color ='maroon',width = 0.3)
plt.xlabel("areas")
plt.ylabel("Number of popular areas")
plt.title("top 3 Popular areas")
plt.show()
#q10-Print skills and find out the most important skills required?
S=dataset['Skills'].value_counts() 
dataset.sort_values("Skills", inplace = True)
print(dataset['Skills'])











