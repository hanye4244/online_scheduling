'''
@Author: Ye Han
@Date: 2019-11-15 10:25:01
@LastEditTime: 2020-05-04 17:56:25
@LastEditors: Ye Han
@Description:
@FilePath: \data_analysis\Spatio_temporal_load.py
@Copyright (c) 2019 - Ye Han
@All rights reserved.
'''

import os

import pandas as pd

# Import Data.
path = 'C:\\Users\\hanye\\Documents\\Data'
files = os.listdir(path)
num = list()
for file in files:
    taxi_data = pd.read_csv(
        path + '\\' + file, names=['state', "lng", 'lat'], engine='python', usecols=[2, 4, 5])
    # The region division. Get one region for our analysis.
    taxi_data = taxi_data[(taxi_data['lng'] > 116.35) & (taxi_data['lng'] < 116.4) & (
        taxi_data['lat'] > 39.95) & (taxi_data['lat'] < 40)]
    # Get the passenger load of the chosen region.
    taxi_data = taxi_data[taxi_data['state'] == 0]
    num.append(taxi_data.shape[0])
    pass
print(num)
# taxi_data = pd.read_csv(
#     'C:\\Users\\hanye\\Documents\\Data\\20121101070001.txt', names=['id'], engine='python', usecols=[0])
# taxi_data = taxi_data.drop_duplicates().values
# # print(taxi_data.values)
# print(taxi_data.shape[0])
