# coding=utf-8
'''
@Author: Ye Han
@Date: 20,20,-0,4-25 18:12:24
@LastEditTime: 2020-05-07 16:31:21
@LastEditors: Ye Han
@Description:
@Copyright (c) 20,20, - Ye Han
All rights reserved.
'''
import numpy as np


def constraint_soc_range(pet_recommended, action, number_of_pet, pet_soc, number_of_pcs, pet_state, manhattan_pcs_pet):
    test_array = np.where(
        ((pet_soc < 15) & (pet_recommended == 0) & (pet_state != 2)), 1, 0)
    test_array_nonzero = np.nonzero(test_array)[0]
    for i in test_array_nonzero:
        # chosen_pcs = np.argmin(manhattan_pcs_pet[:, i])
        chosen_pcs = np.random.randint(number_of_pcs)
        action[chosen_pcs, i] = 1
    return action
