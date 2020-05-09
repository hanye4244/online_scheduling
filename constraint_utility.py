# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-26 14:58:54
@LastEditTime: 2020-04-28 18:12:33
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def constraint_utility(pet_utility, action, pet_cost_max):
    enable_charging = pet_utility * action
    # FIXME:
    test_array = np.where(((enable_charging < pet_cost_max) |
                           (enable_charging == 0)), 0, 1)
    test_bool = bool(test_array.sum())
    return not test_bool


if __name__ == '__main__':
    pet_lat = (40 - 39.4) * np.random.random((10, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((10, 1)) + 116
    pcs_lat = (40 - 39.4) * np.random.random((6, 1)) + 39.4
    pcs_lon = (117 - 116) * np.random.random((6, 1)) + 116
    action = np.random.randint(0, 2, size=[6, 10])
    pet_battery_capacity = np.full((1, 10), 100)
    power_consumption = np.full((1, 6), 0.5)
    manhattan_pcs_pet = np.random.randint(10, 20, size=[6, 10])
    pet_soc = np.random.randint(30, 90, size=[1, 10])
    number_of_pcs = 6
    block_cdq = 40
    queue_service = 8
    number_of_pet = 10
    number_of_region = 4
    pet_average_revenue = 25
    pcs_region = np.random.randint(0, 4, size=[1, 6])
    pet_region = np.random.randint(0, 4, size=[1, 10])
    average_speed = 0.0001
    pick_up_probability = np.random.random(number_of_region)
    constraint_utility(block_cdq, action, pet_battery_capacity, power_consumption, manhattan_pcs_pet, pet_soc, number_of_pcs,
                       queue_service, number_of_region, number_of_pet, pet_average_revenue, pcs_region, pet_region, pick_up_probability)
