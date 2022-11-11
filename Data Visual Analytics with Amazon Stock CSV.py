#!/usr/bin/env python
# coding: utf-8

# # `BERCHMANS KEVIN S`
# 
# 

# ## Data Visual Analytics with Amazon Stock CSV

# #### IMPORTING REQUIRED MODULES

# In[1]:


import pandas as pd


# In[2]:


# setting for pretty plots
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.show()


# In[3]:


# Reading in the data
data = pd.read_csv('amazon_stock.csv')


# #### INSPECT TOP 10 ROWS

# In[4]:


data.head()


# #### REMOVE UNWANTED COLUMNS

# In[5]:


# Remove first two columns (none and ticker) as they dont
#add any value to the dataset, 
# Then, print head() to check if removed

data = data.drop(['None','ticker'],axis=1)


# In[6]:


data.head()


# In[7]:


# Look at the datatypes of the various columns , call info()
data.info()


# #### INSPECT THE DATATYPES OF COLUMNS

# In[8]:


data.dtypes


# #### CONVERT  'DATE' STRING COLUMN INTO ACTUAL DATE OBJECT

# In[9]:


data['Date'] = pd.to_datetime(data['Date'])


# In[10]:


data.dtypes


# #### LET US CHECK OUR DATA ONCE AGAIN , WITH HEAD()

# In[11]:


data.head()


# #### SET DATE OBJECT TO BE INDEX

# **Here Date is one of the columns. But we want date to be  the index. So, set date as index for the frame. Make inplace=True'**

# In[12]:


data.set_index(['Date'], inplace=True)


# In[13]:


data.head()


# #### UNDERSTAND STOCK DATA

# In[14]:


data['Adj_Close'].plot(figsize=(12,6), title = 'Adjusted Closing Price')


# #### UNDERSTAND DATE TIMEINDEX

# In[15]:


from datetime import datetime

my_year = 2020
my_month = 5
my_day =1
my_hour = 13
my_minute = 36
my_second = 45

test_date = datetime(my_year, my_month, my_day)
test_date


# In[16]:


test_date = datetime(my_year, my_month, my_day,my_hour, my_minute, my_second)
print("The Day is : ", test_date.day)
print("The Hour is : ", test_date.hour)
print("The Month is : ", test_date.month)


# #### FIND MINIMUM AND MAXIMUM DATES FROM DATA FRAME, CALL INFO() METHOD

# In[17]:


data.info()


# In[18]:


print("Minimum Date : ",data.index.min())
print("Maximum date : ",data.index.max())


# #### RETRIEVE INDEX OF EARLIEST AND LATEST DATES USING ARGMIN AND ARGMAX

# In[19]:


print("Minimum Date Location  : ",data.index.argmin())
print("Maximum date Location : ",data.index.argmax())


# #### 1.RESAMPLING OPERATION

# #### RESAMPLE ENTIRE DATA FRAME

# #### RESAMPLE DATA WITH YEAR END FREQUENCY ('Y') WITH AVERAGE STOCK PRICE

# In[20]:


data.resample('Y').mean()


# #### RESAMPLE A SPECIFIC COLUMN

# #### PLOT A BAR CHART TO SHOW THE YEARLY ( USE 'A') MEAN ADJUSTED CLOSE PRICE

# In[21]:


data['Adj_Close'].resample('A').mean().plot(kind = 'bar', figsize=(10,4))
plt.title(" Yearly Mean Adj close Price for Amazon")
plt.show()


# #### PLOT BAR CHART TO SHOW MONTHLY MAXIMUM (USE 'MS') OPENING PRICE FOR ALL YEARS

# In[22]:


data['Open'].resample('MS').max().plot(kind = 'bar', figsize=(20,4))
plt.title(" Monthly Maximum Opening Price for Amazon")
plt.show()


# #### PLOT BAR CHART OF QUATERLY (USE 'Q') AVERAGE VOLUME FOR ALL YEARS

# In[23]:


data['Volume'].resample('Q').mean().plot(kind = 'bar', figsize=(10,4))
plt.title(" Quarterly Average Volume for Amazon")
plt.show()


# ### 2. TIME SHIFTING OPERATIONS

# #### SHIFTING DATA FORWARD AND BACKWARD

# #### SHOW HEAD OF DATA

# In[24]:


data.head()


# #### SHIFT DATA BY 1 DAY FOWARD

# In[25]:


data.shift(periods = 1).head()


# #### SHIFT DATA BY 1 DAY BACKWARD

# In[26]:


data.shift(periods = -1).head()


# #### SHIFTING TIME INDEX

# In[27]:


data.head(10)


# In[28]:


data.shift(periods = 3,freq='MS')


# #### APPICATION - COMPUTING RETURN ON INVESTMENT

# In[29]:


ROI = 100* (data['Adj_Close'].tshift(periods = - 365, freq ='D')/data['Adj_Close']-1)
ROI.plot(figsize=(16,8))
plt.ylabel('% Return On Investment')


# #### ROLLING WINDOW OR MOVING WINDOW OPERATIONS

# In[30]:


data['Adj_Close'].plot(figsize=(12,8), color='red')


# #### FIND ROLLIMG MEAN FOR 7 DAYS AND SHOW TOP 10 ROWS

# In[31]:


data.rolling(7).mean().head(10)


# #### PLOT A LINE CHART FOR OPEN COLUMN FOLLOWED BY AVERAGE ROLLING WINDOW OF 30 DAYS DAYS ON THE SAME OPEN COLUMN

# In[34]:


data['Open'].plot(figsize=(12,8))
data['Open'].rolling(30).mean().plot(figsize=(12,8), color='red')

