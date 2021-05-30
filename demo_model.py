"""
Python model "demo_model.py"
Translated using PySD version 0.10.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Total Susceptible': 'total_susceptible',
    'Undetected cases 1': 'undetected_cases_1',
    'Undetected cases 0': 'undetected_cases_0',
    'Undetected cases': 'undetected_cases',
    'Total Detected Cases': 'total_detected_cases',
    'Detected cases 1': 'detected_cases_1',
    'Detected cases': 'detected_cases',
    'Detected cases 0': 'detected_cases_0',
    'Asymptomatic undetected recovered 1': 'asymptomatic_undetected_recovered_1',
    'Asymptomatic undetected a 1': 'asymptomatic_undetected_a_1',
    'Asympytomatic undetected c 1': 'asympytomatic_undetected_c_1',
    'Asymptomatic undetected b 1': 'asymptomatic_undetected_b_1',
    'Exposed Second day': 'exposed_second_day',
    'Hospital Recovered': 'hospital_recovered',
    'Hospital Recovered 0': 'hospital_recovered_0',
    'Hospital Recovered 1': 'hospital_recovered_1',
    'Hospitalized': 'hospitalized',
    'Hospitalized 0': 'hospitalized_0',
    'Hospitalized 1': 'hospitalized_1',
    'Severe 1': 'severe_1',
    'Asymptomatic Detected': 'asymptomatic_detected',
    'Asymptomatic Detected 0': 'asymptomatic_detected_0',
    'Asymptomatic Detected 1': 'asymptomatic_detected_1',
    'Susceptible': 'susceptible',
    'Susceptible 0': 'susceptible_0',
    'Dead': 'dead',
    'Dead 0': 'dead_0',
    'Dead 1': 'dead_1',
    'Symptomatic 1': 'symptomatic_1',
    'Symptomatic Detected': 'symptomatic_detected',
    'Symptomatic Detected 0': 'symptomatic_detected_0',
    'Symptomatic Detected 1': 'symptomatic_detected_1',
    'Symptomatic Recovered': 'symptomatic_recovered',
    'Symptomatic Recovered 0': 'symptomatic_recovered_0',
    'Mildly Symptomatic': 'mildly_symptomatic',
    'Mildly Symptomatic 0': 'mildly_symptomatic_0',
    'Mildly Symptomatic 1': 'mildly_symptomatic_1',
    'Exposed Fourth day': 'exposed_fourth_day',
    'Exposed Fourth day 0': 'exposed_fourth_day_0',
    'Exposed Fourth day 1': 'exposed_fourth_day_1',
    'Symptomatic Undetected Recovered 0': 'symptomatic_undetected_recovered_0',
    'Exposed Second day 0': 'exposed_second_day_0',
    'Exposed Second day 1': 'exposed_second_day_1',
    'alpha 0': 'alpha_0',
    'alpha 1': 'alpha_1',
    'Asymptomatic': 'asymptomatic',
    'Asymptomatic 0': 'asymptomatic_0',
    'Asymptomatic 1': 'asymptomatic_1',
    'Total Population': 'total_population',
    'Asympytomatic undetected c': 'asympytomatic_undetected_c',
    'Asympytomatic undetected c 0': 'asympytomatic_undetected_c_0',
    'Asymptomatic Recovered': 'asymptomatic_recovered',
    'Asymptomatic Recovered 0': 'asymptomatic_recovered_0',
    'Asymptomatic Recovered 1': 'asymptomatic_recovered_1',
    'Asymptomatic undetected a': 'asymptomatic_undetected_a',
    'Asymptomatic undetected a 0': 'asymptomatic_undetected_a_0',
    'Symptomatic 0': 'symptomatic_0',
    'Asymptomatic undetected b': 'asymptomatic_undetected_b',
    'Asymptomatic undetected b 0': 'asymptomatic_undetected_b_0',
    'Critical 0': 'critical_0',
    'Asymptomatic undetected recovered': 'asymptomatic_undetected_recovered',
    'Asymptomatic undetected recovered 0': 'asymptomatic_undetected_recovered_0',
    'Exposed first day': 'exposed_first_day',
    'Exposed first day 0': 'exposed_first_day_0',
    'Exposed first day 1': 'exposed_first_day_1',
    'Total Recovered': 'total_recovered',
    'Symptomatic Undetected 1': 'symptomatic_undetected_1',
    'Symptomatic Undetected Recovered': 'symptomatic_undetected_recovered',
    'Susceptible 1': 'susceptible_1',
    'Symptomatic Undetected Recovered 1': 'symptomatic_undetected_recovered_1',
    'Total Population 0': 'total_population_0',
    'Exposed Third day': 'exposed_third_day',
    'Critical': 'critical',
    'Exposed Third day 1': 'exposed_third_day_1',
    'Critical 1': 'critical_1',
    'Severe 0': 'severe_0',
    'Symptomatic': 'symptomatic',
    'Symptomatic Recovered 1': 'symptomatic_recovered_1',
    'Total Population 1': 'total_population_1',
    'Symptomatic Undetected 0': 'symptomatic_undetected_0',
    'Not Critical 0': 'not_critical_0',
    'Recovered': 'recovered',
    'Recovered 0': 'recovered_0',
    'Recovered 1': 'recovered_1',
    'Not Critical': 'not_critical',
    'Symptomatic Undetected': 'symptomatic_undetected',
    'Exposed Third day 0': 'exposed_third_day_0',
    'Not Critical 1': 'not_critical_1',
    'Severe': 'severe',
    'Mortality Percentage': 'mortality_percentage',
    'Mortality Percentage 0': 'mortality_percentage_0',
    'Mortality Percentage 1': 'mortality_percentage_1',
    'alpha': 'alpha',
    'Mortality Rate 0': 'mortality_rate_0',
    'Mortality Rate 1': 'mortality_rate_1',
    'Testing Symptomatic 1': 'testing_symptomatic_1',
    'Percentage Severe 0': 'percentage_severe_0',
    'Critical Ratio': 'critical_ratio',
    'Critical Ratio 0': 'critical_ratio_0',
    'Critical Ratio 1': 'critical_ratio_1',
    'Testing Symptomatic': 'testing_symptomatic',
    'Percentage Severe': 'percentage_severe',
    'Mortality Rate': 'mortality_rate',
    'Percentage Severe 1': 'percentage_severe_1',
    'Testing Asymptomatic 0': 'testing_asymptomatic_0',
    'Testing Asymptomatic 1': 'testing_asymptomatic_1',
    'Testing Asymptomatic': 'testing_asymptomatic',
    'Testing Symptomatic 0': 'testing_symptomatic_0',
    'a1': 'a1',
    'a1 0': 'a1_0',
    'a1 1': 'a1_1',
    'a10': 'a10',
    'a10 0': 'a10_0',
    'a10 1': 'a10_1',
    'a2': 'a2',
    'a2 0': 'a2_0',
    'a2 1': 'a2_1',
    'a3': 'a3',
    'a3 0': 'a3_0',
    'a3 1': 'a3_1',
    'a4': 'a4',
    'a4 0': 'a4_0',
    'a4 1': 'a4_1',
    'a5': 'a5',
    'a5 0': 'a5_0',
    'a5 1': 'a5_1',
    'a6': 'a6',
    'a6 0': 'a6_0',
    'a6 1': 'a6_1',
    'a7': 'a7',
    'a7 0': 'a7_0',
    'a7 1': 'a7_1',
    'a8': 'a8',
    'a8 0': 'a8_0',
    'a8 1': 'a8_1',
    'a9': 'a9',
    'a9 0': 'a9_0',
    'a9 1': 'a9_1',
    'AUD Rate a': 'aud_rate_a',
    'AUD Rate a 0': 'aud_rate_a_0',
    'AUD Rate a 1': 'aud_rate_a_1',
    'AUD Rate b': 'aud_rate_b',
    'AUD Rate b 0': 'aud_rate_b_0',
    'AUD Rate b 1': 'aud_rate_b_1',
    'Critical Recovery Rate': 'critical_recovery_rate',
    'Critical Recovery Rate 0': 'critical_recovery_rate_0',
    'Critical Recovery Rate 1': 'critical_recovery_rate_1',
    'Disease progression Rate': 'disease_progression_rate',
    'Disease progression Rate 0': 'disease_progression_rate_0',
    'Disease progression Rate 1': 'disease_progression_rate_1',
    'Fraction Susceptible': 'fraction_susceptible',
    'Fraction Susceptible 0': 'fraction_susceptible_0',
    'Fraction Susceptible 1': 'fraction_susceptible_1',
    'h1': 'h1',
    'h1 0': 'h1_0',
    'h1 1': 'h1_1',
    'h2': 'h2',
    'h2 0': 'h2_0',
    'h2 1': 'h2_1',
    'h3': 'h3',
    'h3 0': 'h3_0',
    'h3 1': 'h3_1',
    'h4': 'h4',
    'h4 0': 'h4_0',
    'h4 1': 'h4_1',
    'h5': 'h5',
    'h5 0': 'h5_0',
    'h5 1': 'h5_1',
    'h6': 'h6',
    'h6 0': 'h6_0',
    'h6 1': 'h6_1',
    'h7': 'h7',
    'h7 0': 'h7_0',
    'h7 1': 'h7_1',
    'Inf pop': 'inf_pop',
    'Inf pop 0': 'inf_pop_0',
    'Inf pop 1': 'inf_pop_1',
    'm1': 'm1',
    'm1 0': 'm1_0',
    'm1 1': 'm1_1',
    'm2': 'm2',
    'm2 0': 'm2_0',
    'm2 1': 'm2_1',
    'm3': 'm3',
    'm3 0': 'm3_0',
    'm3 1': 'm3_1',
    'Mild to Severe Rate': 'mild_to_severe_rate',
    'Mild to Severe Rate 0': 'mild_to_severe_rate_0',
    'Mild to Severe Rate 1': 'mild_to_severe_rate_1',
    'Not critical Recovery Rate': 'not_critical_recovery_rate',
    'Not critical Recovery Rate 0': 'not_critical_recovery_rate_0',
    'Not critical Recovery Rate 1': 'not_critical_recovery_rate_1',
    'Recovery Rate': 'recovery_rate',
    'Recovery Rate 0': 'recovery_rate_0',
    'Recovery Rate 1': 'recovery_rate_1',
    's1': 's1',
    's1 0': 's1_0',
    's1 1': 's1_1',
    's2': 's2',
    's2 0': 's2_0',
    's2 1': 's2_1',
    's3': 's3',
    's3 0': 's3_0',
    's3 1': 's3_1',
    's4': 's4',
    's4 0': 's4_0',
    's4 1': 's4_1',
    's5': 's5',
    's5 0': 's5_0',
    's5 1': 's5_1',
    'SUD rate': 'sud_rate',
    'SUD rate 0': 'sud_rate_0',
    'SUD rate 1': 'sud_rate_1',
    't1': 't1',
    't1 0': 't1_0',
    't1 1': 't1_1',
    't2': 't2',
    't2 0': 't2_0',
    't2 1': 't2_1',
    't3': 't3',
    't3 0': 't3_0',
    't3 1': 't3_1',
    't4': 't4',
    't4 0': 't4_0',
    't4 1': 't4_1',
    'Total Critical': 'total_critical',
    'Total Deaths': 'total_deaths',
    'Total Undected Cases': 'total_undected_cases',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.10.0"

__data = {'scope': None, 'time': lambda: 0}


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data['time']()


@cache('step')
def total_susceptible():
    """
    Real Name: b'Total Susceptible'
    Original Eqn: b'Susceptible+Susceptible 0+Susceptible 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible() + susceptible_0() + susceptible_1()


@cache('step')
def undetected_cases_1():
    """
    Real Name: b'Undetected cases 1'
    Original Eqn: b'Asymptomatic undetected a 1+Asympytomatic undetected c 1+Symptomatic Undetected 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_a_1() + asympytomatic_undetected_c_1(
    ) + symptomatic_undetected_1()


@cache('step')
def undetected_cases_0():
    """
    Real Name: b'Undetected cases 0'
    Original Eqn: b'Asymptomatic undetected a 0+Asympytomatic undetected c 0+Symptomatic Undetected 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_a_0() + asympytomatic_undetected_c_0(
    ) + symptomatic_undetected_0()


@cache('step')
def undetected_cases():
    """
    Real Name: b'Undetected cases'
    Original Eqn: b'Asymptomatic undetected a+Asympytomatic undetected c+Symptomatic Undetected'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_a() + asympytomatic_undetected_c() + symptomatic_undetected()


@cache('step')
def total_detected_cases():
    """
    Real Name: b'Total Detected Cases'
    Original Eqn: b'Detected cases+Detected cases 0+Detected cases 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return detected_cases() + detected_cases_0() + detected_cases_1()


@cache('step')
def detected_cases_1():
    """
    Real Name: b'Detected cases 1'
    Original Eqn: b'Asymptomatic Detected 1+Not Critical 1+Symptomatic Detected 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_detected_1() + not_critical_1() + symptomatic_detected_1()


@cache('step')
def detected_cases():
    """
    Real Name: b'Detected cases'
    Original Eqn: b'Asymptomatic Detected+Not Critical+Symptomatic Detected'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_detected() + not_critical() + symptomatic_detected()


@cache('step')
def detected_cases_0():
    """
    Real Name: b'Detected cases 0'
    Original Eqn: b'Asymptomatic Detected 0+Not Critical 0+Symptomatic Detected 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_detected_0() + not_critical_0() + symptomatic_detected_0()


@cache('step')
def asymptomatic_undetected_recovered_1():
    """
    Real Name: b'Asymptomatic undetected recovered 1'
    Original Eqn: b'INTEG ( a10 1+a9 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_recovered_1()


@cache('step')
def asymptomatic_undetected_a_1():
    """
    Real Name: b'Asymptomatic undetected a 1'
    Original Eqn: b'INTEG ( a2 1-a5 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_a_1()


@cache('step')
def asympytomatic_undetected_c_1():
    """
    Real Name: b'Asympytomatic undetected c 1'
    Original Eqn: b'INTEG ( a6 1-a10 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asympytomatic_undetected_c_1()


@cache('step')
def asymptomatic_undetected_b_1():
    """
    Real Name: b'Asymptomatic undetected b 1'
    Original Eqn: b'INTEG ( a5 1-a6 1-a9 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_b_1()


@cache('step')
def exposed_second_day():
    """
    Real Name: b'Exposed Second day'
    Original Eqn: b'INTEG ( t2-a1-m1-t3, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_second_day()


@cache('step')
def hospital_recovered():
    """
    Real Name: b'Hospital Recovered'
    Original Eqn: b'INTEG ( h5+h7, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_hospital_recovered()


@cache('step')
def hospital_recovered_0():
    """
    Real Name: b'Hospital Recovered 0'
    Original Eqn: b'INTEG ( h5 0+h7 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_hospital_recovered_0()


@cache('step')
def hospital_recovered_1():
    """
    Real Name: b'Hospital Recovered 1'
    Original Eqn: b'INTEG ( h5 1+h7 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_hospital_recovered_1()


@cache('step')
def hospitalized():
    """
    Real Name: b'Hospitalized'
    Original Eqn: b'INTEG ( h2-h3-h6, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_hospitalized()


@cache('step')
def hospitalized_0():
    """
    Real Name: b'Hospitalized 0'
    Original Eqn: b'INTEG ( h2 0-h3 0-h6 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_hospitalized_0()


@cache('step')
def hospitalized_1():
    """
    Real Name: b'Hospitalized 1'
    Original Eqn: b'INTEG ( h2 1-h3 1-h6 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_hospitalized_1()


@cache('step')
def severe_1():
    """
    Real Name: b'Severe 1'
    Original Eqn: b'INTEG ( h1 1-h2 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_severe_1()


@cache('step')
def asymptomatic_detected():
    """
    Real Name: b'Asymptomatic Detected'
    Original Eqn: b'INTEG ( a3-a4, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_detected()


@cache('step')
def asymptomatic_detected_0():
    """
    Real Name: b'Asymptomatic Detected 0'
    Original Eqn: b'INTEG ( a3 0-a4 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_detected_0()


@cache('step')
def asymptomatic_detected_1():
    """
    Real Name: b'Asymptomatic Detected 1'
    Original Eqn: b'INTEG ( a3 1-a4 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_detected_1()


@cache('step')
def susceptible():
    """
    Real Name: b'Susceptible'
    Original Eqn: b'INTEG ( -t1, Total Population)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible()


@cache('step')
def susceptible_0():
    """
    Real Name: b'Susceptible 0'
    Original Eqn: b'INTEG ( -t1 0, Total Population 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_0()


@cache('step')
def dead():
    """
    Real Name: b'Dead'
    Original Eqn: b'INTEG ( h4, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_dead()


@cache('step')
def dead_0():
    """
    Real Name: b'Dead 0'
    Original Eqn: b'INTEG ( h4 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_dead_0()


@cache('step')
def dead_1():
    """
    Real Name: b'Dead 1'
    Original Eqn: b'INTEG ( h4 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_dead_1()


@cache('step')
def symptomatic_1():
    """
    Real Name: b'Symptomatic 1'
    Original Eqn: b'INTEG ( s1 1-h1 1-s2 1-s4 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_1()


@cache('step')
def symptomatic_detected():
    """
    Real Name: b'Symptomatic Detected'
    Original Eqn: b'INTEG ( s2-s3, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_detected()


@cache('step')
def symptomatic_detected_0():
    """
    Real Name: b'Symptomatic Detected 0'
    Original Eqn: b'INTEG ( s2 0-s3 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_detected_0()


@cache('step')
def symptomatic_detected_1():
    """
    Real Name: b'Symptomatic Detected 1'
    Original Eqn: b'INTEG ( s2 1-s3 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_detected_1()


@cache('step')
def symptomatic_recovered():
    """
    Real Name: b'Symptomatic Recovered'
    Original Eqn: b'INTEG ( s3, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_recovered()


@cache('step')
def symptomatic_recovered_0():
    """
    Real Name: b'Symptomatic Recovered 0'
    Original Eqn: b'INTEG ( s3 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_recovered_0()


@cache('step')
def mildly_symptomatic():
    """
    Real Name: b'Mildly Symptomatic'
    Original Eqn: b'INTEG ( m1+m2+m3-s1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_mildly_symptomatic()


@cache('step')
def mildly_symptomatic_0():
    """
    Real Name: b'Mildly Symptomatic 0'
    Original Eqn: b'INTEG ( m1 0+m2 0+m3 0-s1 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_mildly_symptomatic_0()


@cache('step')
def mildly_symptomatic_1():
    """
    Real Name: b'Mildly Symptomatic 1'
    Original Eqn: b'INTEG ( m1 1+m2 1+m3 1-s1 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_mildly_symptomatic_1()


@cache('step')
def exposed_fourth_day():
    """
    Real Name: b'Exposed Fourth day'
    Original Eqn: b'INTEG ( t4-a8-m3, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_fourth_day()


@cache('step')
def exposed_fourth_day_0():
    """
    Real Name: b'Exposed Fourth day 0'
    Original Eqn: b'INTEG ( t4 0-a8 0-m3 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_fourth_day_0()


@cache('step')
def exposed_fourth_day_1():
    """
    Real Name: b'Exposed Fourth day 1'
    Original Eqn: b'INTEG ( t4 1-a8 1-m3 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_fourth_day_1()


@cache('step')
def symptomatic_undetected_recovered_0():
    """
    Real Name: b'Symptomatic Undetected Recovered 0'
    Original Eqn: b'INTEG ( s5 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_undetected_recovered_0()


@cache('step')
def exposed_second_day_0():
    """
    Real Name: b'Exposed Second day 0'
    Original Eqn: b'INTEG ( t2 0-a1 0-m1 0-t3 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_second_day_0()


@cache('step')
def exposed_second_day_1():
    """
    Real Name: b'Exposed Second day 1'
    Original Eqn: b'INTEG ( t2 1-a1 1-m1 1-t3 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_second_day_1()


@cache('run')
def alpha_0():
    """
    Real Name: b'alpha 0'
    Original Eqn: b'0.01'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.01


@cache('run')
def alpha_1():
    """
    Real Name: b'alpha 1'
    Original Eqn: b'0.01'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.01


@cache('step')
def asymptomatic():
    """
    Real Name: b'Asymptomatic'
    Original Eqn: b'INTEG ( a1+a7+a8-a2-a3, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic()


@cache('step')
def asymptomatic_0():
    """
    Real Name: b'Asymptomatic 0'
    Original Eqn: b'INTEG ( a1 0+a7 0+a8 0-a2 0-a3 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_0()


@cache('step')
def asymptomatic_1():
    """
    Real Name: b'Asymptomatic 1'
    Original Eqn: b'INTEG ( a1 1+a7 1+a8 1-a2 1-a3 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_1()


@cache('run')
def total_population():
    """
    Real Name: b'Total Population'
    Original Eqn: b'3.24515e+06'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 3.24515e+06


@cache('step')
def asympytomatic_undetected_c():
    """
    Real Name: b'Asympytomatic undetected c'
    Original Eqn: b'INTEG ( a6-a10, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asympytomatic_undetected_c()


@cache('step')
def asympytomatic_undetected_c_0():
    """
    Real Name: b'Asympytomatic undetected c 0'
    Original Eqn: b'INTEG ( a6 0-a10 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asympytomatic_undetected_c_0()


@cache('step')
def asymptomatic_recovered():
    """
    Real Name: b'Asymptomatic Recovered'
    Original Eqn: b'INTEG ( a4, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_recovered()


@cache('step')
def asymptomatic_recovered_0():
    """
    Real Name: b'Asymptomatic Recovered 0'
    Original Eqn: b'INTEG ( a4 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_recovered_0()


@cache('step')
def asymptomatic_recovered_1():
    """
    Real Name: b'Asymptomatic Recovered 1'
    Original Eqn: b'INTEG ( a4 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_recovered_1()


@cache('step')
def asymptomatic_undetected_a():
    """
    Real Name: b'Asymptomatic undetected a'
    Original Eqn: b'INTEG ( a2-a5, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_a()


@cache('step')
def asymptomatic_undetected_a_0():
    """
    Real Name: b'Asymptomatic undetected a 0'
    Original Eqn: b'INTEG ( a2 0-a5 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_a_0()


@cache('step')
def symptomatic_0():
    """
    Real Name: b'Symptomatic 0'
    Original Eqn: b'INTEG ( s1 0-h1 0-s2 0-s4 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_0()


@cache('step')
def asymptomatic_undetected_b():
    """
    Real Name: b'Asymptomatic undetected b'
    Original Eqn: b'INTEG ( a5-a6-a9, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_b()


@cache('step')
def asymptomatic_undetected_b_0():
    """
    Real Name: b'Asymptomatic undetected b 0'
    Original Eqn: b'INTEG ( a5 0-a6 0-a9 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_b_0()


@cache('step')
def critical_0():
    """
    Real Name: b'Critical 0'
    Original Eqn: b'INTEG ( h3 0-h4 0-h5 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_0()


@cache('step')
def asymptomatic_undetected_recovered():
    """
    Real Name: b'Asymptomatic undetected recovered'
    Original Eqn: b'INTEG ( a10+a9, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_recovered()


@cache('step')
def asymptomatic_undetected_recovered_0():
    """
    Real Name: b'Asymptomatic undetected recovered 0'
    Original Eqn: b'INTEG ( a10 0+a9 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_asymptomatic_undetected_recovered_0()


@cache('step')
def exposed_first_day():
    """
    Real Name: b'Exposed first day'
    Original Eqn: b'INTEG ( t1-t2, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_first_day()


@cache('step')
def exposed_first_day_0():
    """
    Real Name: b'Exposed first day 0'
    Original Eqn: b'INTEG ( t1 0-t2 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_first_day_0()


@cache('step')
def exposed_first_day_1():
    """
    Real Name: b'Exposed first day 1'
    Original Eqn: b'INTEG ( t1 1-t2 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_first_day_1()


@cache('step')
def total_recovered():
    """
    Real Name: b'Total Recovered'
    Original Eqn: b'Recovered+Recovered 0+Recovered 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return recovered() + recovered_0() + recovered_1()


@cache('step')
def symptomatic_undetected_1():
    """
    Real Name: b'Symptomatic Undetected 1'
    Original Eqn: b'INTEG ( s4 1-s5 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_undetected_1()


@cache('step')
def symptomatic_undetected_recovered():
    """
    Real Name: b'Symptomatic Undetected Recovered'
    Original Eqn: b'INTEG ( s5, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_undetected_recovered()


@cache('step')
def susceptible_1():
    """
    Real Name: b'Susceptible 1'
    Original Eqn: b'INTEG ( -t1 1, Total Population 1)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_susceptible_1()


@cache('step')
def symptomatic_undetected_recovered_1():
    """
    Real Name: b'Symptomatic Undetected Recovered 1'
    Original Eqn: b'INTEG ( s5 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_undetected_recovered_1()


@cache('run')
def total_population_0():
    """
    Real Name: b'Total Population 0'
    Original Eqn: b'6.34194e+06'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 6.34194e+06


@cache('step')
def exposed_third_day():
    """
    Real Name: b'Exposed Third day'
    Original Eqn: b'INTEG ( t3-a7-m2-t4, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_third_day()


@cache('step')
def critical():
    """
    Real Name: b'Critical'
    Original Eqn: b'INTEG ( h3-h4-h5, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical()


@cache('step')
def exposed_third_day_1():
    """
    Real Name: b'Exposed Third day 1'
    Original Eqn: b'INTEG ( t3 1-a7 1-m2 1-t4 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_third_day_1()


@cache('step')
def critical_1():
    """
    Real Name: b'Critical 1'
    Original Eqn: b'INTEG ( h3 1-h4 1-h5 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_critical_1()


@cache('step')
def severe_0():
    """
    Real Name: b'Severe 0'
    Original Eqn: b'INTEG ( h1 0-h2 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_severe_0()


@cache('step')
def symptomatic():
    """
    Real Name: b'Symptomatic'
    Original Eqn: b'INTEG ( s1-h1-s2-s4, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic()


@cache('step')
def symptomatic_recovered_1():
    """
    Real Name: b'Symptomatic Recovered 1'
    Original Eqn: b'INTEG ( s3 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_recovered_1()


@cache('run')
def total_population_1():
    """
    Real Name: b'Total Population 1'
    Original Eqn: b'846251'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 846251


@cache('step')
def symptomatic_undetected_0():
    """
    Real Name: b'Symptomatic Undetected 0'
    Original Eqn: b'INTEG ( s4 0-s5 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_undetected_0()


@cache('step')
def not_critical_0():
    """
    Real Name: b'Not Critical 0'
    Original Eqn: b'INTEG ( h6 0-h7 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_not_critical_0()


@cache('step')
def recovered():
    """
    Real Name: b'Recovered'
    Original Eqn: b'Asymptomatic Recovered+Hospital Recovered+Symptomatic Recovered'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_recovered() + hospital_recovered() + symptomatic_recovered()


@cache('step')
def recovered_0():
    """
    Real Name: b'Recovered 0'
    Original Eqn: b'Asymptomatic Recovered 0+Hospital Recovered 0+Symptomatic Recovered 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_recovered_0() + hospital_recovered_0() + symptomatic_recovered_0()


@cache('step')
def recovered_1():
    """
    Real Name: b'Recovered 1'
    Original Eqn: b'Asymptomatic Recovered 1+Hospital Recovered 1+Symptomatic Recovered 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_recovered_1() + hospital_recovered_1() + symptomatic_recovered_1()


@cache('step')
def not_critical():
    """
    Real Name: b'Not Critical'
    Original Eqn: b'INTEG ( h6-h7, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_not_critical()


@cache('step')
def symptomatic_undetected():
    """
    Real Name: b'Symptomatic Undetected'
    Original Eqn: b'INTEG ( s4-s5, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_symptomatic_undetected()


@cache('step')
def exposed_third_day_0():
    """
    Real Name: b'Exposed Third day 0'
    Original Eqn: b'INTEG ( t3 0-a7 0-m2 0-t4 0, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_exposed_third_day_0()


@cache('step')
def not_critical_1():
    """
    Real Name: b'Not Critical 1'
    Original Eqn: b'INTEG ( h6 1-h7 1, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_not_critical_1()


@cache('step')
def severe():
    """
    Real Name: b'Severe'
    Original Eqn: b'INTEG ( h1-h2, 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return _integ_severe()


@cache('run')
def mortality_percentage():
    """
    Real Name: b'Mortality Percentage'
    Original Eqn: b'0.1'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def mortality_percentage_0():
    """
    Real Name: b'Mortality Percentage 0'
    Original Eqn: b'0.15'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.15


@cache('run')
def mortality_percentage_1():
    """
    Real Name: b'Mortality Percentage 1'
    Original Eqn: b'0.2'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.2


@cache('run')
def alpha():
    """
    Real Name: b'alpha'
    Original Eqn: b'0.01'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.01


@cache('run')
def mortality_rate_0():
    """
    Real Name: b'Mortality Rate 0'
    Original Eqn: b'1/16'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 16


@cache('run')
def mortality_rate_1():
    """
    Real Name: b'Mortality Rate 1'
    Original Eqn: b'1/16'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 16


@cache('run')
def testing_symptomatic_1():
    """
    Real Name: b'Testing Symptomatic 1'
    Original Eqn: b'0.1'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def percentage_severe_0():
    """
    Real Name: b'Percentage Severe 0'
    Original Eqn: b'0.2'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.2


@cache('run')
def critical_ratio():
    """
    Real Name: b'Critical Ratio'
    Original Eqn: b'0.4'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def critical_ratio_0():
    """
    Real Name: b'Critical Ratio 0'
    Original Eqn: b'0.4'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.4


@cache('run')
def critical_ratio_1():
    """
    Real Name: b'Critical Ratio 1'
    Original Eqn: b'0.6'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.6


@cache('run')
def testing_symptomatic():
    """
    Real Name: b'Testing Symptomatic'
    Original Eqn: b'0.15'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.15


@cache('run')
def percentage_severe():
    """
    Real Name: b'Percentage Severe'
    Original Eqn: b'0.1'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('run')
def mortality_rate():
    """
    Real Name: b'Mortality Rate'
    Original Eqn: b'1/16'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 16


@cache('run')
def percentage_severe_1():
    """
    Real Name: b'Percentage Severe 1'
    Original Eqn: b'0.2'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.2


@cache('run')
def testing_asymptomatic_0():
    """
    Real Name: b'Testing Asymptomatic 0'
    Original Eqn: b'0.05'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.05


@cache('run')
def testing_asymptomatic_1():
    """
    Real Name: b'Testing Asymptomatic 1'
    Original Eqn: b'0.05'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.05


@cache('run')
def testing_asymptomatic():
    """
    Real Name: b'Testing Asymptomatic'
    Original Eqn: b'0.05'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.05


@cache('run')
def testing_symptomatic_0():
    """
    Real Name: b'Testing Symptomatic 0'
    Original Eqn: b'0.1'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 0.1


@cache('step')
def a1():
    """
    Real Name: b'a1'
    Original Eqn: b'(0.2*Exposed Second day)*(0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.2 * exposed_second_day()) * (0.2)


@cache('step')
def a1_0():
    """
    Real Name: b'a1 0'
    Original Eqn: b'(0.2*Exposed Second day 0)*(0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.2 * exposed_second_day_0()) * (0.2)


@cache('step')
def a1_1():
    """
    Real Name: b'a1 1'
    Original Eqn: b'(0.2*Exposed Second day 1)*(0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.2 * exposed_second_day_1()) * (0.2)


@cache('step')
def a10():
    """
    Real Name: b'a10'
    Original Eqn: b'Asympytomatic undetected c*AUD Rate b'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asympytomatic_undetected_c() * aud_rate_b()


@cache('step')
def a10_0():
    """
    Real Name: b'a10 0'
    Original Eqn: b'Asympytomatic undetected c 0*AUD Rate b 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asympytomatic_undetected_c_0() * aud_rate_b_0()


@cache('step')
def a10_1():
    """
    Real Name: b'a10 1'
    Original Eqn: b'Asympytomatic undetected c 1*AUD Rate b 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asympytomatic_undetected_c_1() * aud_rate_b_1()


@cache('step')
def a2():
    """
    Real Name: b'a2'
    Original Eqn: b'Asymptomatic*(1-Testing Asymptomatic)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic() * (1 - testing_asymptomatic())


@cache('step')
def a2_0():
    """
    Real Name: b'a2 0'
    Original Eqn: b'Asymptomatic 0*(1-Testing Asymptomatic 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_0() * (1 - testing_asymptomatic_0())


@cache('step')
def a2_1():
    """
    Real Name: b'a2 1'
    Original Eqn: b'Asymptomatic 1*(1-Testing Asymptomatic 1)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_1() * (1 - testing_asymptomatic_1())


@cache('step')
def a3():
    """
    Real Name: b'a3'
    Original Eqn: b'Asymptomatic*Testing Asymptomatic'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic() * testing_asymptomatic()


@cache('step')
def a3_0():
    """
    Real Name: b'a3 0'
    Original Eqn: b'Asymptomatic 0*Testing Asymptomatic 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_0() * testing_asymptomatic_0()


@cache('step')
def a3_1():
    """
    Real Name: b'a3 1'
    Original Eqn: b'Asymptomatic 1*Testing Asymptomatic 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_1() * testing_asymptomatic_1()


@cache('step')
def a4():
    """
    Real Name: b'a4'
    Original Eqn: b'Asymptomatic Detected*Recovery Rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_detected() * recovery_rate()


@cache('step')
def a4_0():
    """
    Real Name: b'a4 0'
    Original Eqn: b'Asymptomatic Detected 0*Recovery Rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_detected_0() * recovery_rate_0()


@cache('step')
def a4_1():
    """
    Real Name: b'a4 1'
    Original Eqn: b'Asymptomatic Detected 1*Recovery Rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_detected_1() * recovery_rate_1()


@cache('step')
def a5():
    """
    Real Name: b'a5'
    Original Eqn: b'Asymptomatic undetected a*AUD Rate a'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_a() * aud_rate_a()


@cache('step')
def a5_0():
    """
    Real Name: b'a5 0'
    Original Eqn: b'Asymptomatic undetected a 0*AUD Rate a 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_a_0() * aud_rate_a_0()


@cache('step')
def a5_1():
    """
    Real Name: b'a5 1'
    Original Eqn: b'Asymptomatic undetected a 1*AUD Rate a 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_a_1() * aud_rate_a_1()


@cache('step')
def a6():
    """
    Real Name: b'a6'
    Original Eqn: b'Asymptomatic undetected b*0.6'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_b() * 0.6


@cache('step')
def a6_0():
    """
    Real Name: b'a6 0'
    Original Eqn: b'Asymptomatic undetected b 0*0.6'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_b_0() * 0.6


@cache('step')
def a6_1():
    """
    Real Name: b'a6 1'
    Original Eqn: b'Asymptomatic undetected b 1*0.6'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_b_1() * 0.6


@cache('step')
def a7():
    """
    Real Name: b'a7'
    Original Eqn: b'(0.75*Exposed Third day)*(0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.75 * exposed_third_day()) * (0.2)


@cache('step')
def a7_0():
    """
    Real Name: b'a7 0'
    Original Eqn: b'(0.75*Exposed Third day 0)*(0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.75 * exposed_third_day_0()) * (0.2)


@cache('step')
def a7_1():
    """
    Real Name: b'a7 1'
    Original Eqn: b'(0.75*Exposed Third day 1)*(0.2)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.75 * exposed_third_day_1()) * (0.2)


@cache('step')
def a8():
    """
    Real Name: b'a8'
    Original Eqn: b'Exposed Fourth day*0.2'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_fourth_day() * 0.2


@cache('step')
def a8_0():
    """
    Real Name: b'a8 0'
    Original Eqn: b'Exposed Fourth day 0*0.2'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_fourth_day_0() * 0.2


@cache('step')
def a8_1():
    """
    Real Name: b'a8 1'
    Original Eqn: b'Exposed Fourth day 1*0.2'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_fourth_day_1() * 0.2


@cache('step')
def a9():
    """
    Real Name: b'a9'
    Original Eqn: b'Asymptomatic undetected b*0.4'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_b() * 0.4


@cache('step')
def a9_0():
    """
    Real Name: b'a9 0'
    Original Eqn: b'Asymptomatic undetected b 0*0.4'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_b_0() * 0.4


@cache('step')
def a9_1():
    """
    Real Name: b'a9 1'
    Original Eqn: b'Asymptomatic undetected b 1*0.4'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return asymptomatic_undetected_b_1() * 0.4


@cache('run')
def aud_rate_a():
    """
    Real Name: b'AUD Rate a'
    Original Eqn: b'1/10'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 10


@cache('run')
def aud_rate_a_0():
    """
    Real Name: b'AUD Rate a 0'
    Original Eqn: b'1/10'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 10


@cache('run')
def aud_rate_a_1():
    """
    Real Name: b'AUD Rate a 1'
    Original Eqn: b'1/10'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 10


@cache('run')
def aud_rate_b():
    """
    Real Name: b'AUD Rate b'
    Original Eqn: b'1/4'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 4


@cache('run')
def aud_rate_b_0():
    """
    Real Name: b'AUD Rate b 0'
    Original Eqn: b'1/4'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 4


@cache('run')
def aud_rate_b_1():
    """
    Real Name: b'AUD Rate b 1'
    Original Eqn: b'1/4'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 4


@cache('run')
def critical_recovery_rate():
    """
    Real Name: b'Critical Recovery Rate'
    Original Eqn: b'1/21'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 21


@cache('run')
def critical_recovery_rate_0():
    """
    Real Name: b'Critical Recovery Rate 0'
    Original Eqn: b'1/21'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 21


@cache('run')
def critical_recovery_rate_1():
    """
    Real Name: b'Critical Recovery Rate 1'
    Original Eqn: b'1/21'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 21


@cache('run')
def disease_progression_rate():
    """
    Real Name: b'Disease progression Rate'
    Original Eqn: b'1/3'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 3


@cache('run')
def disease_progression_rate_0():
    """
    Real Name: b'Disease progression Rate 0'
    Original Eqn: b'1/3'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 3


@cache('run')
def disease_progression_rate_1():
    """
    Real Name: b'Disease progression Rate 1'
    Original Eqn: b'1/3'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 3


@cache('step')
def fraction_susceptible():
    """
    Real Name: b'Fraction Susceptible'
    Original Eqn: b'Susceptible/Total Population'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible() / total_population()


@cache('step')
def fraction_susceptible_0():
    """
    Real Name: b'Fraction Susceptible 0'
    Original Eqn: b'Susceptible 0/Total Population 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_0() / total_population_0()


@cache('step')
def fraction_susceptible_1():
    """
    Real Name: b'Fraction Susceptible 1'
    Original Eqn: b'Susceptible 1/Total Population 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return susceptible_1() / total_population_1()


@cache('step')
def h1():
    """
    Real Name: b'h1'
    Original Eqn: b'Symptomatic*Percentage Severe'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic() * percentage_severe()


@cache('step')
def h1_0():
    """
    Real Name: b'h1 0'
    Original Eqn: b'Symptomatic 0*Percentage Severe 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_0() * percentage_severe_0()


@cache('step')
def h1_1():
    """
    Real Name: b'h1 1'
    Original Eqn: b'Symptomatic 1*Percentage Severe 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_1() * percentage_severe_1()


@cache('step')
def h2():
    """
    Real Name: b'h2'
    Original Eqn: b'Severe*Mild to Severe Rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return severe() * mild_to_severe_rate()


@cache('step')
def h2_0():
    """
    Real Name: b'h2 0'
    Original Eqn: b'Severe 0*Mild to Severe Rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return severe_0() * mild_to_severe_rate_0()


@cache('step')
def h2_1():
    """
    Real Name: b'h2 1'
    Original Eqn: b'Severe 1*Mild to Severe Rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return severe_1() * mild_to_severe_rate_1()


@cache('step')
def h3():
    """
    Real Name: b'h3'
    Original Eqn: b'Hospitalized*Critical Ratio'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return hospitalized() * critical_ratio()


@cache('step')
def h3_0():
    """
    Real Name: b'h3 0'
    Original Eqn: b'Hospitalized 0*Critical Ratio 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return hospitalized_0() * critical_ratio_0()


@cache('step')
def h3_1():
    """
    Real Name: b'h3 1'
    Original Eqn: b'Hospitalized 1*Critical Ratio 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return hospitalized_1() * critical_ratio_1()


@cache('step')
def h4():
    """
    Real Name: b'h4'
    Original Eqn: b'Critical*Mortality Percentage*Mortality Rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical() * mortality_percentage() * mortality_rate()


@cache('step')
def h4_0():
    """
    Real Name: b'h4 0'
    Original Eqn: b'Critical 0*Mortality Percentage 0*Mortality Rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_0() * mortality_percentage_0() * mortality_rate_0()


@cache('step')
def h4_1():
    """
    Real Name: b'h4 1'
    Original Eqn: b'Critical 1*Mortality Percentage 1*Mortality Rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_1() * mortality_percentage_1() * mortality_rate_1()


@cache('step')
def h5():
    """
    Real Name: b'h5'
    Original Eqn: b'Critical*Critical Recovery Rate*(1-Mortality Percentage)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical() * critical_recovery_rate() * (1 - mortality_percentage())


@cache('step')
def h5_0():
    """
    Real Name: b'h5 0'
    Original Eqn: b'Critical 0*Critical Recovery Rate 0*(1-Mortality Percentage 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_0() * critical_recovery_rate_0() * (1 - mortality_percentage_0())


@cache('step')
def h5_1():
    """
    Real Name: b'h5 1'
    Original Eqn: b'Critical 1*Critical Recovery Rate 1*(1-Mortality Percentage 1)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical_1() * critical_recovery_rate_1() * (1 - mortality_percentage_1())


@cache('step')
def h6():
    """
    Real Name: b'h6'
    Original Eqn: b'Hospitalized*(1-Critical Ratio)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return hospitalized() * (1 - critical_ratio())


@cache('step')
def h6_0():
    """
    Real Name: b'h6 0'
    Original Eqn: b'Hospitalized 0*(1-Critical Ratio 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return hospitalized_0() * (1 - critical_ratio_0())


@cache('step')
def h6_1():
    """
    Real Name: b'h6 1'
    Original Eqn: b'Hospitalized 1*(1-Critical Ratio 1)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return hospitalized_1() * (1 - critical_ratio_1())


@cache('step')
def h7():
    """
    Real Name: b'h7'
    Original Eqn: b'Not Critical*Not critical Recovery Rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return not_critical() * not_critical_recovery_rate()


@cache('step')
def h7_0():
    """
    Real Name: b'h7 0'
    Original Eqn: b'Not Critical 0*Not critical Recovery Rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return not_critical_0() * not_critical_recovery_rate_0()


@cache('step')
def h7_1():
    """
    Real Name: b'h7 1'
    Original Eqn: b'Not Critical 1*Not critical Recovery Rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return not_critical_1() * not_critical_recovery_rate_1()


@cache('step')
def inf_pop():
    """
    Real Name: b'Inf pop'
    Original Eqn: b'Inf pop 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return inf_pop_0()


@cache('step')
def inf_pop_0():
    """
    Real Name: b'Inf pop 0'
    Original Eqn: b'Total Undected Cases'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return total_undected_cases()


@cache('step')
def inf_pop_1():
    """
    Real Name: b'Inf pop 1'
    Original Eqn: b'Inf pop 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return inf_pop_0()


@cache('step')
def m1():
    """
    Real Name: b'm1'
    Original Eqn: b'(0.2*Exposed Second day)*(0.8)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.2 * exposed_second_day()) * (0.8)


@cache('step')
def m1_0():
    """
    Real Name: b'm1 0'
    Original Eqn: b'(0.2*Exposed Second day 0)*(0.8)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.2 * exposed_second_day_0()) * (0.8)


@cache('step')
def m1_1():
    """
    Real Name: b'm1 1'
    Original Eqn: b'(0.2*Exposed Second day 1)*(0.8)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.2 * exposed_second_day_1()) * (0.8)


@cache('step')
def m2():
    """
    Real Name: b'm2'
    Original Eqn: b'(0.75*Exposed Third day)*(0.8)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.75 * exposed_third_day()) * (0.8)


@cache('step')
def m2_0():
    """
    Real Name: b'm2 0'
    Original Eqn: b'(0.75*Exposed Third day 0)*(0.8)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.75 * exposed_third_day_0()) * (0.8)


@cache('step')
def m2_1():
    """
    Real Name: b'm2 1'
    Original Eqn: b'(0.75*Exposed Third day 1)*(0.8)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return (0.75 * exposed_third_day_1()) * (0.8)


@cache('step')
def m3():
    """
    Real Name: b'm3'
    Original Eqn: b'Exposed Fourth day*0.8'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_fourth_day() * 0.8


@cache('step')
def m3_0():
    """
    Real Name: b'm3 0'
    Original Eqn: b'Exposed Fourth day 0*0.8'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_fourth_day_0() * 0.8


@cache('step')
def m3_1():
    """
    Real Name: b'm3 1'
    Original Eqn: b'Exposed Fourth day 1*0.8'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_fourth_day_1() * 0.8


@cache('run')
def mild_to_severe_rate():
    """
    Real Name: b'Mild to Severe Rate'
    Original Eqn: b'1/6'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 6


@cache('run')
def mild_to_severe_rate_0():
    """
    Real Name: b'Mild to Severe Rate 0'
    Original Eqn: b'1/6'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 6


@cache('run')
def mild_to_severe_rate_1():
    """
    Real Name: b'Mild to Severe Rate 1'
    Original Eqn: b'1/6'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 6


@cache('run')
def not_critical_recovery_rate():
    """
    Real Name: b'Not critical Recovery Rate'
    Original Eqn: b'1/18'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 18


@cache('run')
def not_critical_recovery_rate_0():
    """
    Real Name: b'Not critical Recovery Rate 0'
    Original Eqn: b'1/18'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 18


@cache('run')
def not_critical_recovery_rate_1():
    """
    Real Name: b'Not critical Recovery Rate 1'
    Original Eqn: b'1/18'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 18


@cache('run')
def recovery_rate():
    """
    Real Name: b'Recovery Rate'
    Original Eqn: b'1/14'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 14


@cache('run')
def recovery_rate_0():
    """
    Real Name: b'Recovery Rate 0'
    Original Eqn: b'1/14'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 14


@cache('run')
def recovery_rate_1():
    """
    Real Name: b'Recovery Rate 1'
    Original Eqn: b'1/14'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 14


@cache('step')
def s1():
    """
    Real Name: b's1'
    Original Eqn: b'Mildly Symptomatic*Disease progression Rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return mildly_symptomatic() * disease_progression_rate()


@cache('step')
def s1_0():
    """
    Real Name: b's1 0'
    Original Eqn: b'Mildly Symptomatic 0*Disease progression Rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return mildly_symptomatic_0() * disease_progression_rate_0()


@cache('step')
def s1_1():
    """
    Real Name: b's1 1'
    Original Eqn: b'Mildly Symptomatic 1*Disease progression Rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return mildly_symptomatic_1() * disease_progression_rate_1()


@cache('step')
def s2():
    """
    Real Name: b's2'
    Original Eqn: b'Symptomatic*(1-Percentage Severe)*(Testing Symptomatic)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic() * (1 - percentage_severe()) * (testing_symptomatic())


@cache('step')
def s2_0():
    """
    Real Name: b's2 0'
    Original Eqn: b'Symptomatic 0*(1-Percentage Severe 0)*(Testing Symptomatic 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_0() * (1 - percentage_severe_0()) * (testing_symptomatic_0())


@cache('step')
def s2_1():
    """
    Real Name: b's2 1'
    Original Eqn: b'Symptomatic 1*(1-Percentage Severe 1)*(Testing Symptomatic 1)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_1() * (1 - percentage_severe_1()) * (testing_symptomatic_1())


@cache('step')
def s3():
    """
    Real Name: b's3'
    Original Eqn: b'Symptomatic Detected*Recovery Rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_detected() * recovery_rate()


@cache('step')
def s3_0():
    """
    Real Name: b's3 0'
    Original Eqn: b'Symptomatic Detected 0*Recovery Rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_detected_0() * recovery_rate_0()


@cache('step')
def s3_1():
    """
    Real Name: b's3 1'
    Original Eqn: b'Symptomatic Detected 1*Recovery Rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_detected_1() * recovery_rate_1()


@cache('step')
def s4():
    """
    Real Name: b's4'
    Original Eqn: b'Symptomatic*(1-Percentage Severe)*(1-Testing Symptomatic)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic() * (1 - percentage_severe()) * (1 - testing_symptomatic())


@cache('step')
def s4_0():
    """
    Real Name: b's4 0'
    Original Eqn: b'Symptomatic 0*(1-Percentage Severe 0)*(1-Testing Symptomatic 0)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_0() * (1 - percentage_severe_0()) * (1 - testing_symptomatic_0())


@cache('step')
def s4_1():
    """
    Real Name: b's4 1'
    Original Eqn: b'Symptomatic 1*(1-Percentage Severe 1)*(1-Testing Symptomatic 1)'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_1() * (1 - percentage_severe_1()) * (1 - testing_symptomatic_1())


@cache('step')
def s5():
    """
    Real Name: b's5'
    Original Eqn: b'Symptomatic Undetected*SUD rate'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_undetected() * sud_rate()


@cache('step')
def s5_0():
    """
    Real Name: b's5 0'
    Original Eqn: b'Symptomatic Undetected 0*SUD rate 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_undetected_0() * sud_rate_0()


@cache('step')
def s5_1():
    """
    Real Name: b's5 1'
    Original Eqn: b'Symptomatic Undetected 1*SUD rate 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return symptomatic_undetected_1() * sud_rate_1()


@cache('run')
def sud_rate():
    """
    Real Name: b'SUD rate'
    Original Eqn: b'1/14'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 14


@cache('run')
def sud_rate_0():
    """
    Real Name: b'SUD rate 0'
    Original Eqn: b'1/14'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 14


@cache('run')
def sud_rate_1():
    """
    Real Name: b'SUD rate 1'
    Original Eqn: b'1/14'
    Units: b''
    Limits: (None, None)
    Type: constant

    b''
    """
    return 1 / 14


@cache('step')
def t1():
    """
    Real Name: b't1'
    Original Eqn: b'Fraction Susceptible*Inf pop*alpha'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_susceptible() * inf_pop() * alpha()


@cache('step')
def t1_0():
    """
    Real Name: b't1 0'
    Original Eqn: b'Fraction Susceptible 0*Inf pop 0*alpha 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_susceptible_0() * inf_pop_0() * alpha_0()


@cache('step')
def t1_1():
    """
    Real Name: b't1 1'
    Original Eqn: b'Fraction Susceptible 1*Inf pop 1*alpha 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return fraction_susceptible_1() * inf_pop_1() * alpha_1()


@cache('step')
def t2():
    """
    Real Name: b't2'
    Original Eqn: b'Exposed first day'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_first_day()


@cache('step')
def t2_0():
    """
    Real Name: b't2 0'
    Original Eqn: b'Exposed first day 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_first_day_0()


@cache('step')
def t2_1():
    """
    Real Name: b't2 1'
    Original Eqn: b'Exposed first day 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_first_day_1()


@cache('step')
def t3():
    """
    Real Name: b't3'
    Original Eqn: b'0.8*Exposed Second day'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 0.8 * exposed_second_day()


@cache('step')
def t3_0():
    """
    Real Name: b't3 0'
    Original Eqn: b'0.8*Exposed Second day 0'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 0.8 * exposed_second_day_0()


@cache('step')
def t3_1():
    """
    Real Name: b't3 1'
    Original Eqn: b'0.8*Exposed Second day 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return 0.8 * exposed_second_day_1()


@cache('step')
def t4():
    """
    Real Name: b't4'
    Original Eqn: b'Exposed Third day*0.25'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_third_day() * 0.25


@cache('step')
def t4_0():
    """
    Real Name: b't4 0'
    Original Eqn: b'Exposed Third day 0*0.25'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_third_day_0() * 0.25


@cache('step')
def t4_1():
    """
    Real Name: b't4 1'
    Original Eqn: b'Exposed Third day 1*0.25'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return exposed_third_day_1() * 0.25


@cache('step')
def total_critical():
    """
    Real Name: b'Total Critical'
    Original Eqn: b'Critical+Critical 0+Critical 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return critical() + critical_0() + critical_1()


@cache('step')
def total_deaths():
    """
    Real Name: b'Total Deaths'
    Original Eqn: b'Dead 0+Dead 1+Dead'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return dead_0() + dead_1() + dead()


@cache('step')
def total_undected_cases():
    """
    Real Name: b'Total Undected Cases'
    Original Eqn: b'Undetected cases+Undetected cases 0+Undetected cases 1'
    Units: b''
    Limits: (None, None)
    Type: component

    b''
    """
    return undetected_cases() + undetected_cases_0() + undetected_cases_1()


@cache('run')
def final_time():
    """
    Real Name: b'FINAL TIME'
    Original Eqn: b'100'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b'The final time for the simulation.'
    """
    return 100


@cache('run')
def initial_time():
    """
    Real Name: b'INITIAL TIME'
    Original Eqn: b'0'
    Units: b'Day'
    Limits: (None, None)
    Type: constant

    b'The initial time for the simulation.'
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: b'SAVEPER'
    Original Eqn: b'TIME STEP'
    Units: b'Day'
    Limits: (0.0, None)
    Type: component

    b'The frequency with which output is stored.'
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: b'TIME STEP'
    Original Eqn: b'1'
    Units: b'Day'
    Limits: (0.0, None)
    Type: constant

    b'The time step for the simulation.'
    """
    return 1


_integ_asymptomatic_undetected_recovered_1 = functions.Integ(lambda: a10_1() + a9_1(), lambda: 0)

_integ_asymptomatic_undetected_a_1 = functions.Integ(lambda: a2_1() - a5_1(), lambda: 0)

_integ_asympytomatic_undetected_c_1 = functions.Integ(lambda: a6_1() - a10_1(), lambda: 0)

_integ_asymptomatic_undetected_b_1 = functions.Integ(lambda: a5_1() - a6_1() - a9_1(), lambda: 0)

_integ_exposed_second_day = functions.Integ(lambda: t2() - a1() - m1() - t3(), lambda: 0)

_integ_hospital_recovered = functions.Integ(lambda: h5() + h7(), lambda: 0)

_integ_hospital_recovered_0 = functions.Integ(lambda: h5_0() + h7_0(), lambda: 0)

_integ_hospital_recovered_1 = functions.Integ(lambda: h5_1() + h7_1(), lambda: 0)

_integ_hospitalized = functions.Integ(lambda: h2() - h3() - h6(), lambda: 0)

_integ_hospitalized_0 = functions.Integ(lambda: h2_0() - h3_0() - h6_0(), lambda: 0)

_integ_hospitalized_1 = functions.Integ(lambda: h2_1() - h3_1() - h6_1(), lambda: 0)

_integ_severe_1 = functions.Integ(lambda: h1_1() - h2_1(), lambda: 0)

_integ_asymptomatic_detected = functions.Integ(lambda: a3() - a4(), lambda: 0)

_integ_asymptomatic_detected_0 = functions.Integ(lambda: a3_0() - a4_0(), lambda: 0)

_integ_asymptomatic_detected_1 = functions.Integ(lambda: a3_1() - a4_1(), lambda: 0)

_integ_susceptible = functions.Integ(lambda: -t1(), lambda: total_population())

_integ_susceptible_0 = functions.Integ(lambda: -t1_0(), lambda: total_population_0())

_integ_dead = functions.Integ(lambda: h4(), lambda: 0)

_integ_dead_0 = functions.Integ(lambda: h4_0(), lambda: 0)

_integ_dead_1 = functions.Integ(lambda: h4_1(), lambda: 0)

_integ_symptomatic_1 = functions.Integ(lambda: s1_1() - h1_1() - s2_1() - s4_1(), lambda: 0)

_integ_symptomatic_detected = functions.Integ(lambda: s2() - s3(), lambda: 0)

_integ_symptomatic_detected_0 = functions.Integ(lambda: s2_0() - s3_0(), lambda: 0)

_integ_symptomatic_detected_1 = functions.Integ(lambda: s2_1() - s3_1(), lambda: 0)

_integ_symptomatic_recovered = functions.Integ(lambda: s3(), lambda: 0)

_integ_symptomatic_recovered_0 = functions.Integ(lambda: s3_0(), lambda: 0)

_integ_mildly_symptomatic = functions.Integ(lambda: m1() + m2() + m3() - s1(), lambda: 0)

_integ_mildly_symptomatic_0 = functions.Integ(lambda: m1_0() + m2_0() + m3_0() - s1_0(), lambda: 0)

_integ_mildly_symptomatic_1 = functions.Integ(lambda: m1_1() + m2_1() + m3_1() - s1_1(), lambda: 0)

_integ_exposed_fourth_day = functions.Integ(lambda: t4() - a8() - m3(), lambda: 0)

_integ_exposed_fourth_day_0 = functions.Integ(lambda: t4_0() - a8_0() - m3_0(), lambda: 0)

_integ_exposed_fourth_day_1 = functions.Integ(lambda: t4_1() - a8_1() - m3_1(), lambda: 0)

_integ_symptomatic_undetected_recovered_0 = functions.Integ(lambda: s5_0(), lambda: 0)

_integ_exposed_second_day_0 = functions.Integ(lambda: t2_0() - a1_0() - m1_0() - t3_0(), lambda: 0)

_integ_exposed_second_day_1 = functions.Integ(lambda: t2_1() - a1_1() - m1_1() - t3_1(), lambda: 0)

_integ_asymptomatic = functions.Integ(lambda: a1() + a7() + a8() - a2() - a3(), lambda: 0)

_integ_asymptomatic_0 = functions.Integ(lambda: a1_0() + a7_0() + a8_0() - a2_0() - a3_0(),
                                        lambda: 0)

_integ_asymptomatic_1 = functions.Integ(lambda: a1_1() + a7_1() + a8_1() - a2_1() - a3_1(),
                                        lambda: 0)

_integ_asympytomatic_undetected_c = functions.Integ(lambda: a6() - a10(), lambda: 0)

_integ_asympytomatic_undetected_c_0 = functions.Integ(lambda: a6_0() - a10_0(), lambda: 0)

_integ_asymptomatic_recovered = functions.Integ(lambda: a4(), lambda: 0)

_integ_asymptomatic_recovered_0 = functions.Integ(lambda: a4_0(), lambda: 0)

_integ_asymptomatic_recovered_1 = functions.Integ(lambda: a4_1(), lambda: 0)

_integ_asymptomatic_undetected_a = functions.Integ(lambda: a2() - a5(), lambda: 0)

_integ_asymptomatic_undetected_a_0 = functions.Integ(lambda: a2_0() - a5_0(), lambda: 0)

_integ_symptomatic_0 = functions.Integ(lambda: s1_0() - h1_0() - s2_0() - s4_0(), lambda: 0)

_integ_asymptomatic_undetected_b = functions.Integ(lambda: a5() - a6() - a9(), lambda: 0)

_integ_asymptomatic_undetected_b_0 = functions.Integ(lambda: a5_0() - a6_0() - a9_0(), lambda: 0)

_integ_critical_0 = functions.Integ(lambda: h3_0() - h4_0() - h5_0(), lambda: 0)

_integ_asymptomatic_undetected_recovered = functions.Integ(lambda: a10() + a9(), lambda: 0)

_integ_asymptomatic_undetected_recovered_0 = functions.Integ(lambda: a10_0() + a9_0(), lambda: 0)

_integ_exposed_first_day = functions.Integ(lambda: t1() - t2(), lambda: 0)

_integ_exposed_first_day_0 = functions.Integ(lambda: t1_0() - t2_0(), lambda: 0)

_integ_exposed_first_day_1 = functions.Integ(lambda: t1_1() - t2_1(), lambda: 0)

_integ_symptomatic_undetected_1 = functions.Integ(lambda: s4_1() - s5_1(), lambda: 0)

_integ_symptomatic_undetected_recovered = functions.Integ(lambda: s5(), lambda: 0)

_integ_susceptible_1 = functions.Integ(lambda: -t1_1(), lambda: total_population_1())

_integ_symptomatic_undetected_recovered_1 = functions.Integ(lambda: s5_1(), lambda: 0)

_integ_exposed_third_day = functions.Integ(lambda: t3() - a7() - m2() - t4(), lambda: 0)

_integ_critical = functions.Integ(lambda: h3() - h4() - h5(), lambda: 0)

_integ_exposed_third_day_1 = functions.Integ(lambda: t3_1() - a7_1() - m2_1() - t4_1(), lambda: 0)

_integ_critical_1 = functions.Integ(lambda: h3_1() - h4_1() - h5_1(), lambda: 0)

_integ_severe_0 = functions.Integ(lambda: h1_0() - h2_0(), lambda: 0)

_integ_symptomatic = functions.Integ(lambda: s1() - h1() - s2() - s4(), lambda: 0)

_integ_symptomatic_recovered_1 = functions.Integ(lambda: s3_1(), lambda: 0)

_integ_symptomatic_undetected_0 = functions.Integ(lambda: s4_0() - s5_0(), lambda: 0)

_integ_not_critical_0 = functions.Integ(lambda: h6_0() - h7_0(), lambda: 0)

_integ_not_critical = functions.Integ(lambda: h6() - h7(), lambda: 0)

_integ_symptomatic_undetected = functions.Integ(lambda: s4() - s5(), lambda: 0)

_integ_exposed_third_day_0 = functions.Integ(lambda: t3_0() - a7_0() - m2_0() - t4_0(), lambda: 0)

_integ_not_critical_1 = functions.Integ(lambda: h6_1() - h7_1(), lambda: 0)

_integ_severe = functions.Integ(lambda: h1() - h2(), lambda: 0)
