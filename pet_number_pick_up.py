# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-15 10:40:36
@LastEditTime: 2020-05-04 18:10:16
@LastEditors: Ye Han
@Description: PET passengers is picked up random.
@FilePath: \Online_Scheduling\pet_number_pick_up.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def pet_number_pick_up(pet_pick_up, number_of_region, pet_region):
    pet = pd.DataFrame(pet_pick_up, columns=['pick_up'])
    pet['region'] = pet_region
    # print(pet_region)
    pick_up_pet = pet.groupby('region')[
        'pick_up'].sum()
    list_pick_up = pick_up_pet.index.tolist()
    for i in range(4):
        if i not in list_pick_up:
            pick_up_pet.loc[i] = 0
    return pick_up_pet.values.reshape(number_of_region, 1)
    pass


if __name__ == '__main__':
    pet_state = np.random.randint(0, 3, size=[10, 1])
    number_of_region = 9
    pet_pick_up = np.random.randint(0, 2, size=[10, 1])
    percentage_of_pick_up_pet = 0.6
    pet_region = np.random.randint(1, 10, size=[10, 1])

    pet_number_pick_up(pet_pick_up, number_of_region, pet_region)
