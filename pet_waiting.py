# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-30 09:28:51
@LastEditTime: 2020-06-30 18:39:35
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def pet_waiting(block_cdq, pev_arrival, pet_power_demand, number_of_pet, action, number_of_pcs, waiting_demand, pet_completed):
    # 每辆充电地车辆前面剩余地需求量。
    shape_block_cdq = np.tile(block_cdq, (1, number_of_pet))
    shape_pev_arrival = np.tile(pev_arrival, (1, number_of_pet))
    # 此时到达不算这一时隙调度的需求量。
    shape_pre_charging_demand = shape_block_cdq + shape_pev_arrival
    # 每一辆到达这一充电站的车前面的需求量。
    # 这一时隙到达的需求量。
    pcs_power_demand = pet_power_demand * action
    sum_power_demand = np.zeros((number_of_pcs, number_of_pet))
    # 每一项和前一项求和。
    for i in range(number_of_pet):
        sum_power_demand[:, i] = pcs_power_demand[:,
                                                  0: (i)].sum(axis=1)
    waiting_demand = (sum_power_demand +
                      shape_pre_charging_demand) * action + waiting_demand
    completed_test = np.where((pet_completed == 1), 0, 1).T
    shape_completed_test = np.tile(completed_test, (number_of_pcs, 1))
    waiting_demand = shape_completed_test * waiting_demand
    return waiting_demand


if __name__ == "__main__":
    block_cdq = np.array([[3], [4]])
    pev_arrival = np.array([[3], [4]])
    pet_power_demand = np.array([[3, 3, 6, 8], [4, 4, 6, 8]])
    number_of_pet = 4
    action = np.array([[0, 1, 0, 1], [1, 0, 0, 0]])
    pet_waiting(block_cdq, pev_arrival,
                pet_power_demand, number_of_pet, action, 2)
pass
