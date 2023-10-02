# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:06:00 2023

@author: Utilisateur
"""

import pandas as pd


"Import datas"
table = pd.read_csv('life_expectancy.csv',index_col=0)

"one data"

print(table['1980'][17])

"plot of datas"
table.plot.scatter('1960','2014')
table2 = table.transpose()
pd.plot()