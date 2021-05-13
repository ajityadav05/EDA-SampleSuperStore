#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation #GRIPMAY21

# ## Name:- Ajit Yadav
# ## Task:- Exploratory Data Analysis - Retail
# ### Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore

# #### Data URL:- https://bit.ly/3i4rbWl

# ### Objective:
# #### ● As a business manager, try to find out the weak areas where you can work to make more profit. 
# #### ● What all business problems you can derive by exploring the data? 

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


#importing the data
data = pd.read_csv("C:\\Users\\lenovo\Desktop\\The Sparks Foundation\\SampleSuperstoreData.csv")


# In[ ]:


#understanding the data
data.head()


# In[ ]:


data.tail()


# In[ ]:


data.dtypes


# In[ ]:


data.shape


# In[ ]:


data.describe()


# In[ ]:


data.columns


# In[ ]:


data.nunique()


# In[ ]:


data['Ship Mode'].unique()


# In[ ]:


data['Segment'].unique()


# In[ ]:


data['Region'].unique()


# In[ ]:


data['Category'].unique()


# In[ ]:


data['Sub-Category'].unique()


# In[ ]:


# Cleaning the data
data.isnull().sum()


# In[ ]:


#to cehck presence of duplicates
data.duplicated().sum()


# In[ ]:


data.drop_duplicates(inplace=True)


# In[ ]:


data.shape


# In[ ]:


data1 = data.drop(['Country','Postal Code'],axis=1)


# In[ ]:


data1.head()


# In[ ]:


# Demand for each segment
data1['Segment'].value_counts()


# In[ ]:


data1['Segment'].value_counts()/len(data1['Segment'])*100


# In[ ]:


(data1['Segment'].value_counts()/len(data1['Segment'])*100).plot(kind='bar')
plt.title('Demand Of Segments')
plt.xlabel('Segment')
plt.ylabel('Percentages')


# ##### Consumer Segment has more demand in USA followed by Corporate and Home Office.

# In[ ]:


# Demand for each ship mode
(data1['Ship Mode'].value_counts()/len(data1['Ship Mode'])*100).plot(kind='bar')
plt.title('Demand Of Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Percentages')


# ##### Standard Class ship mode has more demand than others.

# In[ ]:


# Demand for each category
(data1['Category'].value_counts()/len(data1['Category'])*100).plot(kind='bar')
plt.title('Demand Of Categories')
plt.xlabel('Categories')
plt.ylabel('Percentages')


# ###### Office Supplies has more demand than Furniture and Technology.

# In[ ]:


#demand from various states
(data1['State'].value_counts()/len(data1['State'])*100).plot(kind='bar',figsize=(20,7))
plt.title('Demand For Products From Various States')
plt.xlabel('States')
plt.ylabel('Percentages')


# ##### There are more customers from California followed by New York and Texas.

# In[ ]:


#demand for sub-categories
(data1['Sub-Category'].value_counts()/len(data1['Sub-Category'])*100).plot.pie(radius=2,autopct='%1.i%%')
plt.title('Demand Of Sub-categories')


# ##### Binders have more demand followed by Paper and Furnishings.

# In[ ]:


# Demand for categories from different region
sns.countplot(x=data['Region'],hue=data['Category'])


# ##### West USA has more demand for all the categories followed by East, Central and South region of USA.

# In[ ]:


# Relationship Analysis
# Correlation matrix 
cor = data1.corr()
sns.heatmap(cor,xticklabels = cor.columns,yticklabels = cor.columns,annot = True)


# ##### Here, we can see that Profit and Sales have Moderately Positive Relationship .
# ##### Profit and Discount have (Weak) Negative Relationship.

# In[ ]:


sns.pairplot(data1)


# In[ ]:


#category wise profit and sales
p=data.groupby('Category')['Profit','Sales'].agg('sum')
print(p)
p.plot.bar()
plt.title('Category-wise Profit & Sales')


# In[ ]:


p=data.groupby('Sub-Category')['Profit','Sales'].agg('sum')
print(p)
p.plot.bar(figsize=(15,5))
plt.title('Sub-Category wise Profit & Sales')


# In[ ]:


q=data.groupby('Segment')['Profit','Sales'].agg('sum')
print(q)
q.plot.bar()
plt.title('Segment-wise Profit & Sales')


# In[ ]:


r=data.groupby('Ship Mode')['Profit','Sales'].agg('sum')
print(r)
r.plot.bar(figsize=(10,5))
plt.title('ShipMode-wise Profit & Sales')


# In[ ]:


s=data.groupby('State')['Profit','Sales'].agg('sum')
print(s)
s.plot.bar(figsize=(15,7))
plt.title('State-wise Profit & Sales')


# In[ ]:


p=data.groupby('Region')['Profit','Sales'].agg('sum')
print(p)
p.plot.bar(figsize=(10,5))
plt.title('Region-wise Profit & Sales')


# ##### •	From the Categories, Technology has more sales and returns more profit followed by Office Supplies and Furniture.
# ##### •	From the Sub-Categories, Phones and Chairs have more sales but in terms of profit Accessories and Copiers are preferable.  Also, Tables, Supplies and Bookcases are in loss despite of having good number of sales.
# ##### •	If we analyze Segment-wise, Consumer segment has more sales and profit followed by Corporate and Home Office segments.
# ##### •	California has highest sales and returns maximum profit followed by New York. Texas has the third highest sales but it does not returns good profit.
# ##### •	There are more sales in West region of USA and returns more profit followed by East, Central and South region.
# 

# In[ ]:


# Segmentwise distribution of profit
plt.bar(data1['Segment'],data1['Profit'])
plt.title("Segment-wise Profit")
plt.xlabel('Segment')
plt.ylabel('Profit')


# In[ ]:


# Ship Mode wise distribution of profit
plt.bar(data1['Ship Mode'],data1['Profit'])
plt.title("Ship Mode-wise Profit")
plt.xlabel('Ship Mode')
plt.ylabel('Profit')


# In[ ]:


#Category wise distribution of profit
plt.bar(data1['Category'],data1['Profit'])
plt.title("Category-wise Profit")
plt.xlabel('Category')
plt.ylabel('Profit')


# In[ ]:


# Sub-Category wise distribution of profit
plt.figure(figsize=(15,5))
plt.bar(data1['Sub-Category'],data1['Profit'])
plt.title("Sub-Category-wise Profit")
plt.xlabel('Sub-Category')
plt.ylabel('Profit')


# In[ ]:


# Region wise distribution of profit
plt.bar(data1['Region'],data1['Profit'])
plt.title("Region-wise Profit")
plt.xlabel('Region')
plt.ylabel('Profit')


# In[ ]:


sns.distplot(data1['Profit'])


# ##### Since from above charts, we can easily say that profit is concentrated towards zero. 

# In[ ]:


plt.bar(data1['Discount'],data1['Profit'])
plt.title("Profit v/s Discount")
plt.xlabel('Discount')
plt.ylabel('Profit')


# In[ ]:


data1.pivot_table(values='Sales',index='Segment',columns='Discount',aggfunc='median')


# In[ ]:


data1.pivot_table(values='Profit',index='Segment',columns='Discount',aggfunc='median')


# In[ ]:


temp = data1.loc[(data1['Segment']=='Consumer') & (data1['Discount']<0.3)]
temp['Profit'].plot.hist()


# In[ ]:


temp1 = data1.loc[(data1['Segment']=='Corporate') & (data1['Discount']<0.3)]
temp1['Profit'].plot.hist()


# In[ ]:


temp2 = data1.loc[(data1['Segment']=='Home Office') & (data1['Discount']<0.2)]
temp2['Profit'].plot.hist()


# In[ ]:


data1.pivot_table(values='Sales',index='Category',columns='Discount',aggfunc='median')


# In[ ]:


data1.pivot_table(values='Profit',index='Category',columns='Discount',aggfunc='median')


# In[ ]:


temp3 = data1.loc[(data1['Category']=='Furniture') & (data1['Discount']<0.3)]
temp3['Profit'].plot.hist()


# In[ ]:


temp4 = data1.loc[(data1['Category']=='Office Supplies') & (data1['Discount']<0.3)]
temp4['Profit'].plot.hist()


# In[ ]:


temp5 = data1.loc[(data1['Category']=='Technology') & (data1['Discount']<=0.3)]
temp5['Profit'].plot.hist()


# In[ ]:


data1.pivot_table(values='Sales',index='Sub-Category',columns='Discount',aggfunc='median')


# In[ ]:


data1.pivot_table(values='Profit',index='Sub-Category',columns='Discount',aggfunc='median')


# In[ ]:


temp3 = data1.loc[(data1['Sub-Category']=='Tables') & (data1['Discount']<0.3)]
temp3['Profit'].plot.hist()


# In[ ]:


temp3 = data1.loc[(data1['Sub-Category']=='Machines') & (data1['Discount']<=0.3)]
temp3['Profit'].plot.hist()


# ### Conclusion:
# ##### •	For all the segments, the discount should be strictly less than 0.30 in order to earn maximum profit.
# ##### •	For the categories, Office Supplies and Furniture should have discount less than 0.30 but for technology discount should be less than or equal to 0.30.
# ##### •	For all the sub-categories except Machines, discount should be strictly less then 0.30 and for Machines, discount should be less than or equal to 0.30.
# 
