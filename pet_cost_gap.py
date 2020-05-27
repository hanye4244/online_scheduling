# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-26 12:01:41
@LastEditTime: 2020-05-26 16:32:00
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''


import numpy as np


def pet_cost_gap(manhattan_pcs_pet, number_of_pcs,
                 number_of_pet, action, shape_waiting_time, charging_time, pet_average_revenue, pet_recommended):
    action_near = np.zeros((number_of_pcs, number_of_pet))
    charge_index = np.nonzero(pet_recommended)[0]
    for i in charge_index:
        pcs_chosen = np.argmin(manhattan_pcs_pet[:, i])
        action_near[pcs_chosen, i] = 1
    pet_cost_near = np.sum(
        ((shape_waiting_time + charging_time) * action_near), axis=0)
    pet_cost = np.sum(((shape_waiting_time + charging_time) * action), axis=0)
    gap_pet_cost = pet_cost - pet_cost_near
    pet_cost_rev = gap_pet_cost * pet_average_revenue
    return pet_cost_rev
