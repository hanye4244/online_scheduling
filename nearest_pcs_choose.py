# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-10 10:31:30
@LastEditTime: 2020-05-26 16:11:16
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def nearest_pcs_choose(pet_soc, manhattan_pcs_pet, number_of_pet, action, pet_state):
    # pet_charging_random = np.random.randint(0, 2, size=[number_of_pet, 1])
    pet_recommended = np.where(
        ((pet_soc < 0.1) & (pet_state == 0)), 1, 0)
    charge_index = np.nonzero(pet_recommended)[0]
    for i in charge_index:
        pcs_chosen = np.argmin(manhattan_pcs_pet[:, i])
        action[pcs_chosen, i] = 1
    return action, pet_recommended
