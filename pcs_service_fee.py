# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-16 15:04:11
@LastEditTime: 2020-04-28 16:17:48
@LastEditors: Ye Han
@Description: Calculate the service fee of each PCS.
@FilePath: \Online_Scheduling\pcs_service_fee.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def pcs_service_fee(cdq_arrival_rate, per_service_fee):
    service_fee = cdq_arrival_rate * per_service_fee
    return service_fee
    pass


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
    pcs_service_fee(action, pet_battery_capacity, power_consumption,
                    manhattan_pcs_pet, pet_soc, number_of_pcs, omega_0, omega_1)
