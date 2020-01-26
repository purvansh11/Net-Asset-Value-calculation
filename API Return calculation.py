#!/usr/bin/env python
# coding: utf-8

# In[1]:


import quandl

quandl.ApiConfig.api_key='RZCxWTQxvxZLMAzP22Ay'

limited_dt=quandl.get('AMFI/140249', start_date='2019-07-03', end_date='2019-07-03')
print("LIVE API DATA...")
print(limited_dt)
print()
yr=input("Enter year span: ")

print("Displaying the expected return")

retur=(limited_dt['Net Asset Value'][0]+limited_dt['Net Asset Value'][0]*0.1)
print(retur)


# In[ ]:




