import pandas as pd 
import numpy as np
import datetime
import matplotlib.pyplot as plt

## Reading and Preprocessing Data
df = pd.read_csv('PMCdata_AdityaSir.csv')
# setting first name as index column
new_header = df.iloc[0] 
df = df[1:] 

df.columns = new_header
print(df.columns)
df.rename(columns = {'\nDate\n(All Reports Until   7 pm included)':'Date', '\nTotal Progresive Number of \nDeaths In Pune \nAmongst Covid-19\nPositive Patients':'Deaths','\nNumber Of \nPatients Recovered\n and Discharged on Date': 'Daily Recovered',
	'\nTotal Number of active cases':'Active Cases', '\nNumber of \nCritical Patients':'Critical', '\nTotal Progresive Number of \nPositive Patients \nRecovered/Discharged':'Recovered'}, inplace = True)

df.set_index("Date", inplace = True)



df = df[['Deaths', 'Active Cases', 'Critical', 'Recovered', 'Daily Recovered']]

df.index = pd.to_datetime(df.index)
df['Deaths'] = pd.to_numeric(df['Deaths'],errors = 'coerce')
df['Active Cases'] = pd.to_numeric(df['Active Cases'],errors = 'coerce')
df['Critical'] = pd.to_numeric(df['Critical'],errors = 'coerce')
df['Recovered'] = pd.to_numeric(df['Recovered'],errors = 'coerce')
df['Daily Recovered'] = pd.to_numeric(df['Daily Recovered'],errors = 'coerce')

df = df.loc['2020-01-09':]
# df = df.iloc[:212,:]
print(df.tail(2))
# x_axis = range(122)
# plt.plot(x_axis,df['Daily Pos'],c='red',label='Positive')
# plt.plot(x_axis,df['Daily Recovered'],c='blue',label='Recovered')
# plt.axvline(x=30, color='k', linestyle='--')
# plt.axvline(x=61, color='k', linestyle='--')
# plt.axvline(x=91, color='k', linestyle='--')
# plt.xlabel('Days')
# plt.ylabel('Number')
# plt.legend()
# plt.show()
# plt.clf()





