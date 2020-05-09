# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-19 16:02:17
@LastEditTime: 2020-05-07 18:14:06
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\passenger_demand.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np

# def fun(x):
# if x < 87:
#     a = 1
# if (x < 156) & (x >= 87):
#     a = 2
# if (x >= 156) & (x < 225):
#     a = 3
# if (x >= 225) & (x < 294):
#     a = 4
# if(x >= 294):
#     a = 5
# return a


def passenger_demand(number_of_region, t):
    passenger_demand = np.array([[1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 5], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
                                0, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 3, 3, 3, 2, 3, 3, 5], [1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 1]])
    passenger_demand_slot = passenger_demand[:, t]
    return passenger_demand_slot.reshape(number_of_region, 1)


if __name__ == '__main__':
    number_of_region = 4
    passenger_demand(number_of_region, 1)
