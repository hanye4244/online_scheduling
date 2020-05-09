# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-15 18:00:27
@LastEditTime: 2020-04-29 20:39:02
@LastEditors: Ye Han
@Description: Give the arrival rate of each PCS including PETs and PEVs.
@FilePath: \Online_Scheduling\pcs_arrival.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np


def pcs_arrival(action, pet_power_demand, number_of_pcs, number_of_pet, pev_arrival_rate):
    '''
    There, we assume that the charging demand of each PEV is 60. The number of the arrived PEVs is random.
    '''
    pet_arrival_rate = pet_power_demand * action
    pet_shape_arrival_rate = pet_arrival_rate.sum(
        axis=1).reshape(number_of_pcs, 1)
    # print('pet_shape_arrival_rate =', pet_shape_arrival_rate)
    pcs_arrival_rate = pet_shape_arrival_rate + pev_arrival_rate
    return pcs_arrival_rate
    pass


if __name__ == '__main__':
    action = np.random.randint(0, 2, size=[6, 10])
    pet_battery_capacity = np.full((1, 10), 100)
    power_consumption = np.full((1, 10), 0.5)
    manhattan_pcs_pet = np.random.randint(10, 20, size=[6, 10])
    pet_soc = np.random.randint(30, 90, size=[10, 1])
    number_of_pcs = 6
    number_of_pet = 10
    pcs_arrival(action, pet_battery_capacity, power_consumption,
                manhattan_pcs_pet, pet_soc, number_of_pcs, number_of_pet)
