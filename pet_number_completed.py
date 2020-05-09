# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-14 17:11:14
@LastEditTime: 2020-04-28 16:23:13
@LastEditors: Ye Han
@Description: Give the number of charging-completed PETs in each region.
@FilePath: \Online_Scheduling\pet_number_completed.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def number_charging_completed_pet(pet_soc, pet_state, pet_region, pet_completed):
    pet = pd.DataFrame(pet_completed, columns=['completed'])
    pet['region'] = pet_region
    charging_completed_pet = pet.groupby('region')[
        'completed'].sum()
    return charging_completed_pet.values
    pass


if __name__ == '__main__':
    pet_soc = np.random.randint(85, 100, size=[6, 1])
    print(pet_soc)
    pet_state = np.random.randint(0, 3, size=[6, 1])
    print(pet_state)
    pet_lat = (40 - 39.4) * np.random.random((6, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((6, 1)) + 116
    number_charging_completed_pet(pet_soc, pet_state, pet_lat, pet_lon)
