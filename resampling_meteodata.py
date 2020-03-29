# This codes works perfectly fine to import and plot meteo data.
# Check after the data has been importet if it is correct by opening it 
# in an excel!

# Import necessary packages
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import earthpy as et
import statsmodels.api as sm
import scipy.stats as sp

# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Use white grid plot background from seaborn. This is just to make the plots better looking :).
sns.set(font_scale=1.5, style="whitegrid")

## IMPORTING:

abra_hourly_2011_2019 = pd.read_csv('abra_hourly_2011_2019.csv',
                                   delimiter=';',
                                    dayfirst = True,
                                   parse_dates=['Date'],
                                   index_col=['Date'],
                                   na_values=['NA'])


# Resampling
abra_DAILY_2012_2018 = abra_hourly_2012_2018.resample('D').mean()
abra_MONTHLY_2012_2018 = abra_hourly_2012_2018.resample('M').mean()
abra_YEARLY_2012_2018 = abra_hourly_2012_2018.resample('Y').mean()

# To try if the dataset does not start at the first of January:
gol_hourly = gol_hourly.['2013-09-26': '2020-10-02'].resample('D').mean()
