# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-10 10:31:30
@LastEditTime: 2020-06-24 11:16:53
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def nearest_pcs_choose(manhattan_pcs_pet, action, charging_test, number_of_pet):
    # pet_charging_random = np.random.randint(0, 2, size=[number_of_pet, 1])
    pet_recommended = charging_test
    charge_index = np.nonzero(pet_recommended)[0]
    for i in charge_index:
        pcs_chosen = np.argmin(manhattan_pcs_pet[:, i])
        action[pcs_chosen, i] = 1
    return action
