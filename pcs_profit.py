# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-22 11:47:05
@LastEditTime: 2020-04-29 16:51:35
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np


def pcs_profit(service_fee, pcs_cost):
    profit = service_fee - pcs_cost
    return profit


if __name__ == '__main__':
    action = np.random.randint(0, 2, size=[6, 10])
    print(action)
    pet_battery_capacity = np.full((1, 10), 100)
    power_consumption = np.full((1, 6), 0.5)
    manhattan_pcs_pet = np.random.randint(10, 20, size=[6, 10])
    pet_soc = np.random.randint(30, 90, size=[1, 10])
    number_of_pcs = 6
    omega_0 = 0.5
    omega_1 = 2000
    pcs_profit(20, 8, action, pet_battery_capacity, power_consumption,
               manhattan_pcs_pet, pet_soc, number_of_pcs, omega_0, omega_1)
