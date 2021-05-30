import pandas as pd 
import pysd
import matplotlib.pyplot as plt
from lmfit import Parameters, minimize, fit_report
import numpy as np
from param_best import *
from graph import *

def add_to_df(result, sim_df, test_val):
	res2 = list(result['Total Detected Cases'])
	res3 = list(result['Total Deaths'])
	res5 = list(result['Total Recovered'])
	res4 = list(result['Total Critical'])
	res7= list(result['Total Susceptible'])
	

	for i in range(0, len(result['Total Deaths'])):
		sim_df = sim_df.append(pd.Series([res3[i], res2[i]+res4[i], res4[i], res5[i],res7[i]], index=['Total Deaths','Total Cases','Total Critical', 'Total Recovered','Total Susceptible']), ignore_index=True)

	return sim_df	


## Reading and Preprocessing Data
df = pd.read_csv('PMCdata_AdityaSir.csv')
# setting first name as index column
new_header = df.iloc[0] 
df = df[1:] 
df.columns = new_header

df.rename(columns = {'\nDate\n(All Reports Until   7 pm included)':'Date', '\nTotal Progresive Number of \nDeaths In Pune \nAmongst Covid-19\nPositive Patients':'Deaths',
	'\nTotal Number of active cases':'Active Cases', '\nNumber of \nCritical Patients':'Critical', '\nTotal Progresive Number of \nPositive Patients \nRecovered/Discharged':'Recovered'}, inplace = True)

df.set_index("Date", inplace = True)
df = df[['Deaths', 'Active Cases', 'Critical', 'Recovered']]
df.index = pd.to_datetime(df.index)
df['Deaths'] = pd.to_numeric(df['Deaths'],errors = 'coerce')
df['Active Cases'] = pd.to_numeric(df['Active Cases'],errors = 'coerce')
df['Critical'] = pd.to_numeric(df['Critical'],errors = 'coerce')
df['Recovered'] = pd.to_numeric(df['Recovered'],errors = 'coerce')


df = df.loc['2020-01-09':]
#df = df.iloc[:242,:]

#data = df.iloc[:30, :]
## Read the SD Model
model = pysd.read_vensim('demo_model.mdl')

# #Inital Parameter
params={ 
		'testing_asymptomatic':0.05,
		'testing_asymptomatic_0':0.05,
		'testing_asymptomatic_1':0.05,
		'testing_symptomatic':0.125,
		'testing_symptomatic_0':0.125,
		'testing_symptomatic_1':0.125,

		'alpha':0.037,
		'alpha_0':0.041,
		'alpha_1':0.037,

		'percentage_severe':0.08,
		'percentage_severe_0':0.1,
		'percentage_severe_1':0.15,

		'critical_ratio':0.045,
		'critical_ratio_0':0.065,
		'critical_ratio_1':0.085,

		'mortality_percentage':0.25,
		'mortality_percentage_0':0.5,
		'mortality_percentage_1':0.6,

		'recovery_rate': 0.1,
		'recovery_rate_0': 0.1,
		'recovery_rate_1':0.1,


		'not_critical_recovery_rate' : 0.067,
		'not_critical_recovery_rate_0' : 0.067,
		'not_critical_recovery_rate_1' : 0.067,
}                    
								


 		

## Inital Values for the stocks
init_vals = (0,{
		'susceptible':2596118,
		'susceptible_0':5073548,
		'susceptible_1':677000,

		'exposed_first_day':5000,
		'exposed_first_day_0':5000,
		'exposed_first_day_1':5000,

		'exposed_second_day':1000,
		'exposed_second_day_0':1000,
		'exposed_second_day_1':1000,

		'exposed_third_day':2000,
		'exposed_third_day_0':2000,
		'exposed_third_day_1':2000,		

		'exposed_fourth_day':1000,
		'exposed_fourth_day_0':1000,
		'exposed_fourth_day_1':1000,

		'mildly_symptomatic':12000,
		'mildly_symptomatic_0':17000,
		'mildly_symptomatic_1':14000,

		'severe':900,
		'severe_0':1650,
		'severe_1':1900,

		'symptomatic_undetected':15000,
		'symptomatic_undetected_0':25000,
		'symptomatic_undetected_1':10000,
		'asymptomatic_undetected_a':3000,
		'asymptomatic_undetected_a_0':7000,
		'asymptomatic_undetected_a_1':2000,
		'asymptomatic_undetected_c':2000,
		'asymptomatic_undetected_c_0':5000,
		'asymptomatic_undetected_c_1':1000,




		'critical':200,
		'critical_0':300,
		'critical_1':390,
		'not_critical': 300,
		'not_critical_0':400,
		'not_critical_1':193,

		'dead': 432,
		'dead_0':800,
		'dead_1':1100,


		'symptomatic_recovered_1': 79489,
		'symptomatic_detected_0' : 13644

 })


cols = ['Total Deaths', 'Total Cases', 'Total Critical','Total Recovered']
model_ret_cols = ['Total Deaths','Total Detected Cases','Total Critical','Total Recovered','Total Susceptible']
sim_df = pd.DataFrame(columns = cols)

result = model.run(params = params,initial_condition=init_vals,return_columns=model_ret_cols,
					return_timestamps=np.linspace(0, 30, num=30))

sim_df = add_to_df(result, sim_df, 0.3)

result = model.run(params = get_params("Oct"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(30, 61, num=31))

sim_df = add_to_df(result, sim_df, 0.05)

result = model.run(params = get_params("Nov"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(61, 91, num=30))

sim_df = add_to_df(result, sim_df, 0.1)
result = model.run(params = get_params("Dec"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(91, 122, num=31))

sim_df = add_to_df(result, sim_df, 0.1)

result = model.run(params = get_params("Jan"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(122, 153, num=31))

sim_df = add_to_df(result, sim_df, 0.1)

result = model.run(params = get_params("Feb"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(153, 181, num=28))

sim_df = add_to_df(result, sim_df, 0.1)

result = model.run(params = get_params("Mar"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(181, 212, num=31))

sim_df = add_to_df(result, sim_df, 0.1)

result = model.run(params = get_params("Apr"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(212, 242, num=30))

sim_df = add_to_df(result, sim_df, 0.1)

result = model.run(params = get_params("May"),initial_condition='current',return_columns=model_ret_cols,
					return_timestamps=np.linspace(242, 267, num=25))

sim_df = add_to_df(result, sim_df, 0.1)

plot_graph(sim_df, df, 267)

print(sim_df.tail(2))







