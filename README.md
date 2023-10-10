# Data-Engineering-Python
This Repo contains python codes to manipulate the data.

[Outliers.ipynb]
This notebook contains python functions, which detects and (detects and deletes) the outliers from pandas data frame with Interquartile Range concept.

Formula used:
'''
for 25 (Q3) and 75 (Q1) quartile, numpy was used,
IQR = Q3 - Q1
Lower Bracket = Q1 - 1.5 ( IQR )
Upper Bracket = Q3 + 1.5 ( IQR )
'''

Outliers are selected when the value is beyond the upper and lower bracket.

# comments are given in each line of code to show the process flow
