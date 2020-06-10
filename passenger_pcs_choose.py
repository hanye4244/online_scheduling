# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-27 17:28:23
@LastEditTime: 2020-06-09 17:50:29
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''


def passenger_pcs_choose(max_soc):
    pet_recommended = np.where(
        ((pet_soc < max_soc) & (pet_state == 0)), 1, 0)
    charge_index = np.nonzero(pet_recommended)[0]
    for i in charge_index:
        pcs_chosen = np.argmin(manhattan_pcs_pet[:, i])
        action[pcs_chosen, i] = 1
