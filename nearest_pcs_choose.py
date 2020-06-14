# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-10 10:31:30
@LastEditTime: 2020-06-11 20:47:56
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def nearest_pcs_choose(pet_soc, manhattan_pcs_pet, number_of_pet, action, pet_state, max_soc):
    charging_request = np.array(
        list(map(charging_state_test, pet_soc, pet_state)))
    charge_index = np.nonzero(charging_request)[0]
    for i in charge_index:
        pcs_chosen = np.argmin(manhattan_pcs_pet[:, i])
        action[pcs_chosen, i] = 1
    return action, charging_request.reshape(number_of_pet, 1)


def charging_state_test(soc, state):
    if soc >= 0.5:
        charging_test = 0
    elif ((soc < 0.5) and (soc >= 0.15) and (state == 0)):
        charging_test = np.random.randint(0, 2)
    elif ((soc < 0.15) and (state == 0)):
        charging_test = 1
    else:
        charging_test = 0
    return charging_test
