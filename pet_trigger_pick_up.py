# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-16 16:11:18
@LastEditTime: 2020-06-30 23:03:28
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\pet_trigger_pick_up.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import random

import numpy as np
import pandas as pd


def pet_trigger_pick_up(pet_state, pet_recommended, number_of_region, pet_region, pet_soc, pet_pick_up_region, pet_pick_up):
    for j in range(number_of_region):
        pet_available = np.where(((pet_state.flatten() == 0) & (
            pet_recommended.flatten() != 1) & (pet_soc.flatten() > 2) & (pet_region.flatten() == j)), 1, 0)
        # print(pet_available)
        pet_available_index = list(np.nonzero(pet_available)[0])
        # print(pet_pick_up_region)
        pet_choose = random.sample(
            pet_available_index, int(pet_pick_up_region[j]))
        for i in pet_choose:
            pet_pick_up[i] = 1
            pass
        pass
    return pet_pick_up
    pass


if __name__ == '__main__':
    pet = pd.DataFrame(columns=['lat', 'lon'])
    number_of_pet = 10
    number_of_region = 4
    pet_region = np.array([[1], [2], [1], [3], [2], [0], [0], [1], [2], [0]])
    pet_state = np.random.randint(0, 1, size=[10, 1])
    pet_soc = np.random.randint(3, 10, size=[10, 1])
    pet_recommended = np.random.randint(0, 2, size=[10, 1])
    pet_pick_up_probability = np.full((10, 1), 1)
    pet_pick_up_region = np.array([1, 2, 0, 1])
    pet_pick_up = np.zeros((10, 1))
    percentage_of_pick_up_pet = np.random.random(10)
    pet_trigger_pick_up(pet_state, pet_recommended, number_of_region,
                        pet_region, pet_soc, pet_pick_up_region, pet_pick_up)
