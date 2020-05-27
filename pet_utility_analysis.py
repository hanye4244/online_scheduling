# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-26 10:51:25
@LastEditTime: 2020-05-27 12:01:05
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def pet_utility_analysis(revenue_gap, pet_cost, pet_soc, action, number_of_pcs):
    revenue_gap_test = np.where(((revenue_gap <= 0) | (pet_soc < 0.1)), 0, 1)
    pet_cost_test = np.where(((pet_cost <= 0) | (pet_soc < 0.1)), 0, 1)
    # test = revenue_gap_test + pet_cost_test
    test = pet_cost_test
    reject_index = np.nonzero(test)[0]
    for i in reject_index:
        action[:, i] = np.zeros(number_of_pcs)
    return action
