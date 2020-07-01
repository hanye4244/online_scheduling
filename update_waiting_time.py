# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-07-01 09:28:01
@LastEditTime: 2020-07-01 09:32:05
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def update_waiting_time(block_cdq, cdq_arrival_rate, number_of_pcs, cdq_service_rate, waiting_demand, pet_state, number_of_pet, charging_state):
    cdq = pd.DataFrame(block_cdq, columns=['block_cdq'])
    cdq['queue_service'] = cdq_service_rate
    cdq['fact_service'] = cdq.apply(lambda x: x['block_cdq'] if (
        x['queue_service'] > x['block_cdq']) else x['queue_service'], axis=1)
    fact_service = cdq['fact_service'].values.reshape((number_of_pcs, 1))
    shape_fact_service = np.tile(fact_service, (1, number_of_pet))
    serve_demand = (waiting_demand - shape_fact_service) * charging_state
    return serve_demand
