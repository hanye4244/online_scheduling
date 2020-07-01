# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-20 11:22:34
@LastEditTime: 2020-07-01 09:29:41
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\queue_pcs.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def queue_cdq(block_cdq, cdq_arrival_rate, number_of_pcs, cdq_service_rate, waiting_demand, pet_state, number_of_pet, charging_state):
    cdq = pd.DataFrame(block_cdq, columns=['block_cdq'])
    cdq['queue_service'] = cdq_service_rate
    cdq['test'] = cdq.apply(lambda x: 0 if (
        x['queue_service'] > x['block_cdq']) else (x['block_cdq'] - x['queue_service']), axis=1)
    block_cdq = cdq['test'].values.reshape(number_of_pcs, 1) + cdq_arrival_rate
    return block_cdq


if __name__ == '__main__':
    action = np.random.randint(0, 2, size=[6, 10])
    pet_battery_capacity = np.full((1, 10), 100)
    power_consumption = np.full((6, 1), 0.5)
    manhattan_pcs_pet = np.random.randint(10, 20, size=[6, 10])
    pet_soc = np.random.randint(30, 90, size=[1, 10])
    number_of_pcs = 6
    block_cdq = np.random.randint(8, 50, size=[6, 1])
    cdq_arrival_rate = np.random.randint(10, 20, size=[6, 1])
    number_of_plug = 8
    charging_rate_of_each = 20
    queue_cdq(block_cdq, cdq_arrival_rate, number_of_plug,
              charging_rate_of_each, number_of_pcs)
