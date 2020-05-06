#!/usr/bin/env python
# coding: utf-8



import quandl
#Configuration key for Quandl from where data is accessed
quandl.ApiConfig.api_key='RZCxWTQxvxZLMAzP22Ay'

#For sample case, start_date and end_date are pre defined
limited_dt=quandl.get('AMFI/140249', start_date='2019-07-03', end_date='2019-07-03')
print("LIVE API DATA...")
print(limited_dt)
print()
yr=int(input("Enter year span (non-zero) : "))

print("Displaying the expected return...")

#Applying hypothetical formula on the extracted values
retur=(limited_dt['Net Asset Value'][0]+limited_dt['Net Asset Value'][0]*0.1/yr)

#printing the final result
print(retur)






