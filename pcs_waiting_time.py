# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-20 11:42:28
@LastEditTime: 2020-04-28 16:22:01
@LastEditors: Ye Han
@Description: 
@FilePath: \Online_Scheduling\pcs_waiting_time.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def pcs_waiting_time(cdq_service_rate, block_cdq):
    waiting_time = block_cdq / cdq_service_rate
    return waiting_time


if __name__ == '__main__':
    action = np.random.randint(0, 2, size=[6, 10])
    pet_battery_capacity = np.full((1, 10), 100)
    power_consumption = np.full((1, 6), 0.5)
    manhattan_pcs_pet = np.random.randint(10, 20, size=[6, 10])
    pet_soc = np.random.randint(30, 90, size=[1, 10])
    number_of_pcs = 6
    block_pcs = 40
    queue_service = 8
    pcs_waiting_time(block_pcs, action, pet_battery_capacity, power_consumption,
                     manhattan_pcs_pet, pet_soc, number_of_pcs, queue_service)
