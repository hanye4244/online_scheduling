# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-20 11:22:34
@LastEditTime: 2020-06-30 16:32:09
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
    cdq['fact_service'] = cdq.apply(lambda x: x['block_cdq'] if (
        x['queue_service'] > x['block_cdq']) else x['queue_service'], axis=1)
    fact_service = cdq['fact_service'].values.reshape((number_of_pcs, 1))
    shape_fact_service = np.tile(fact_service, (1, number_of_pet))
    # print('fact_service', fact_service.ravel())
    serve_demand = (waiting_demand - shape_fact_service) * charging_state
    # print('serve_demand', serve_demand)
    # print('shape_fact_service', shape_fact_service)
    # print('waiting_demand', waiting_demand)
    cdq['test'] = cdq.apply(lambda x: 0 if (
        x['queue_service'] > x['block_cdq']) else (x['block_cdq'] - x['queue_service']), axis=1)
    block_cdq = cdq['test'].values.reshape(number_of_pcs, 1) + cdq_arrival_rate
    return block_cdq, serve_demand


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
