#!/usr/bin/env python
# encoding: utf-8
"""
scratch.py

"""

import sys
import os
import pandas
import matplotlib.pyplot as plt
from pandas.stats.moments import ewma
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot

def main():
	df = pandas.DataFrame.from_csv("three_year.csv")
	daily_volume = df[" V"].resample("D",how="sum").dropna()
	weekly_volume = df[" V"].resample("W", how="sum")
	
	### Differencing ###
	#delta = volume.diff()
	#delta.plot()
	
	### 10 day EWMA ###
	#e = ewma(v,com=0.25)
	#volume.plot()
	#e.plot()
	

	plt.show()


if __name__ == '__main__':
	main()

