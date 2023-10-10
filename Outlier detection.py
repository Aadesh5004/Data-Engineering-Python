import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Value': [12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 45, 80, 100, 120, -8, -10, -15, -18]
})
outliers = []
## finding the outliers in this dataset using the concept of IQR (inter quartile range)
def find_outliers(data):
    sorted_data = data.sort_values(by = 'Value', ascending = True)
    q1, q3 = np.percentile(sorted_data, [25,75])
    IQR = q3-q1
    lower_bracket = q1 - (1.5*IQR)
    upper_bracket = q3 + (1.5*IQR)
    for i in data['Value']:
        outliers.append(i) if i < lower_bracket or i > upper_bracket else False
    
    print(outliers)
    
find_outliers(data)

        

