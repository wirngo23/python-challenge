#***********************************************************************
# @file
#
# Module 3 Challenge
#
# @note None
#
# @warning  None
#
#  Created: December 4, 2023
#   Author: Emile Wirngo
#**********************************************************************/
#!/usr/bin/env python

import os, sys
import math
import numpy as np
from numpy import inf
import pandas as pd 

pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.options.mode.chained_assignment = None

# For logarithm divide-by-zero warnings
np.seterr(divide = 'ignore') 
#np.seterr(divide = 'warn') 

print('Hello, my name is Emile Wirngo')
print()

print('os.path.dirname(__file__):')
print(os.path.dirname(__file__))
print()

the_path = os.path.join(os.path.dirname(__file__) + '\\Resources\\', 'budget_data.csv')
print('the_path')
print(the_path)
print()

# Reference: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
budget_data_df = pd.read_csv(the_path)
print(budget_data_df)
print()

print('Dataset dimensions of Budget Data financial records of my company:')
print(budget_data_df.shape)
print()

# Results as mandated by module 3:
print('Financial Analysis')
print('----------------------------')
print('Total Months:', budget_data_df.shape[0])
