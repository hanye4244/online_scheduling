# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-21 10:02:07
@LastEditTime: 2020-04-28 18:09:02
@LastEditors: Ye Han
@Description: 
@FilePath: \Online_Scheduling\constraint_soc.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def constraint_soc(action, pet_power_demand):
    enable_driving = pet_power_demand * action
    test_array = np.where((enable_driving > 0) | (enable_driving == 0), 0, 1)
    test_bool = bool(np.array(test_array).sum())
    return not test_bool


if __name__ == '__main__':
    pet_lat = (40 - 39.4) * np.random.random((10, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((10, 1)) + 116
    pcs_lat = (40 - 39.4) * np.random.random((6, 1)) + 39.4
    pcs_lon = (117 - 116) * np.random.random((6, 1)) + 116
    pet_soc = np.random.randint(50, 100, 10)
    average_speed = 0.001
    action = np.random.randint(0, 2, size=[6, 10])
    constraint_soc(action, pet_lat, pet_lon, pcs_lat,
                   pcs_lon, pet_soc, average_speed, 6, 10)
