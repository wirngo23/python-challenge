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

#print('Dataset dimensions of Budget Data financial records of my company:')
#print(budget_data_df.shape)
#print()

net_total_amount_profit_losses = budget_data_df['Profit/Losses'].sum()

# Calculating the difference between two rows
changes_in_profit_losses_over_the_entire_period = budget_data_df['Profit/Losses'].diff()

print('changes_in_profit_losses_over_the_entire_period')
print(changes_in_profit_losses_over_the_entire_period)
print()

average_of_changes = changes_in_profit_losses_over_the_entire_period.mean()
average_of_changes_rounded = round(average_of_changes, 2)
greatest_increase_in_profits = changes_in_profit_losses_over_the_entire_period.max()
greatest_decrease_in_profits = changes_in_profit_losses_over_the_entire_period.min()

greatest_increase_in_profits_index = changes_in_profit_losses_over_the_entire_period[changes_in_profit_losses_over_the_entire_period == greatest_increase_in_profits].index
greatest_decrease_in_profits_index = changes_in_profit_losses_over_the_entire_period[changes_in_profit_losses_over_the_entire_period == greatest_decrease_in_profits].index

print('greatest_increase_in_profits_index')
print(greatest_increase_in_profits_index)
print()

print('greatest_decrease_in_profits_index')
print(greatest_decrease_in_profits_index)
print()

print('type(greatest_increase_in_profits_index)')
print(type(greatest_increase_in_profits_index))
print()

print('greatest_increase_in_profits_index.tolist()')
print(greatest_increase_in_profits_index.tolist())
print()

print('greatest_decrease_in_profits_index.tolist()')
print(greatest_decrease_in_profits_index.tolist())
print()


greatest_increase_in_profits_month = budget_data_df.loc[greatest_increase_in_profits_index.tolist()[0]]['Date']
greatest_decrease_in_profits_month = budget_data_df.loc[greatest_decrease_in_profits_index.tolist()[0]]['Date']

greatest_increase_in_profits_string = 'Greatest Increase in Profits: {} ({})'.format(greatest_increase_in_profits_month, greatest_increase_in_profits)
greatest_decrease_in_profits_string = 'Greatest Decrease in Profits: {} ({})'.format(greatest_decrease_in_profits_month, greatest_decrease_in_profits)

# Results as mandated by module 3:
print('Financial Analysis')
print('----------------------------')
print('Total Months:', budget_data_df.shape[0])
print('Total:', net_total_amount_profit_losses)
print('Average Change: $%.2f' % average_of_changes)
#print('Average Change:', average_of_changes_rounded)
print('Greatest Increase in Profits: {} ({})'.format(greatest_increase_in_profits_month, greatest_increase_in_profits))
print('Greatest Decrease in Profits: {} ({})'.format(greatest_decrease_in_profits_month, greatest_decrease_in_profits))

analysis_results_output = 'Total Months:' + str(budget_data_df.shape[0]) + '\n' \
          + 'Total:' + str(net_total_amount_profit_losses) + '\n' \
          + 'Average Change:' + str(average_of_changes_rounded) + '\n' \
          + str(greatest_increase_in_profits_string) + '\n' \
          + str(greatest_decrease_in_profits_string)

the_output_filepath = os.path.join(os.path.dirname(__file__) + '\\analysis\\', 'analysis_results.txt')
print('the_output_filepath')
print(the_output_filepath)
print()

# Per instruction from professor, write results to text file:
with open(the_output_filepath, 'w') as f:
    f.write(analysis_results_output)
    f.close()