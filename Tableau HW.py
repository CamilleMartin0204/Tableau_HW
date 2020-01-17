#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Jersey City Citibike Program 2019 - get 2019May-July tripdata
import pandas as pd
import datetime
import numpy as np
import os


# In[ ]:


# Get Jersey City Citibike tripdata csv files from 201901 to 201907
filepath1 = os.path.join("Resources" ,"JC-201901-citibike-tripdata.csv")
filepath2 = os.path.join("Resources" ,"JC-201902-citibike-tripdata.csv")
filepath3 = os.path.join("Resources" ,"JC-201903-citibike-tripdata.csv")
filepath4 = os.path.join("Resources" ,"JC-201904-citibike-tripdata.csv")
filepath5 = os.path.join("Resources" ,"JC-201905-citibike-tripdata.csv")
filepath6 = os.path.join("Resources" ,"JC-201906-citibike-tripdata.csv")
filepath7 = os.path.join("Resources" ,"JC-201907-citibike-tripdata.csv")

JCbike_201901 = pd.read_csv(filepath1)
JCbike_201902 = pd.read_csv(filepath2)
JCbike_201903 = pd.read_csv(filepath3)
JCbike_201904 = pd.read_csv(filepath4)
JCbike_201905 = pd.read_csv(filepath5)
JCbike_201906 = pd.read_csv(filepath6)
JCbike_201907 = pd.read_csv(filepath7)


# In[ ]:


JCbike_201901.head(5)


# In[ ]:


JCbike_2019all = pd.concat([JCbike_201901,JCbike_201902,JCbike_201903,JCbike_201904,JCbike_201905,JCbike_201906,JCbike_201907])


# In[ ]:


JCbike_2019all.count()


# In[ ]:


tripduration               214214
starttime                  214214
stoptime                   214214
start station id           214214
start station name         214214
start station latitude     214214
start station longitude    214214
end station id             214214
end station name           214214
end station latitude       214214
end station longitude      214214
bikeid                     214214
usertype                   214214
birth year                 214214
gender                     214214
dtype: int64


# In[ ]:


filepath2019= os.path.join("Resources" ,"JCbike_2019all.csv")
JCbike_2019all.to_csv(filepath2019,index=False)
JCbike_2019all.head()

