# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-19 11:01:41
@LastEditTime: 2020-06-30 22:41:20
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\pet_soc_time_slot.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def pet_soc_time_slot(pet_state, pet_soc, number_of_pet, waiting_demand):
    charging_test = waiting_demand.sum(axis=0).reshape(number_of_pet, 1)
    # print('charging_test', charging_test.ravel())
    pet = pd.DataFrame(np.concatenate(
        [pet_state, pet_soc, charging_test], axis=1), columns=['state', 'soc',  'charging_test'])
    pet['soc'] = pet.apply(lambda x: (x['soc'] - 0.5)
                           if (x['state'] == 0) else x['soc'], axis=1)
    pet['soc'] = pet.apply(lambda x: (x['soc'] - 0.5)
                           if (x['state'] == 1) else x['soc'], axis=1)
    pet['soc'] = pet.apply(lambda x: (x['soc'] + 1.5)
                           if ((x['state'] == 2) & (x['charging_test'] <= 0)) else x['soc'], axis=1)
    pet['soc'] = pet.apply(lambda x: 9.9 if (
        x['soc'] > 9.9) else x['soc'], axis=1)
    #     (x['soc'] < 15) & (x['state'] != 2)) else x['soc'], axis=1)
    # print(pet)
    return pet['soc'].values.reshape(number_of_pet, 1)


if __name__ == '__main__':
    pet = pd.DataFrame(columns=['state', 'soc'])
    pet_soc = np.random.randint(50, 100, size=10)
    pet_state = np.random.randint(0, 3, size=10)
    pet['state'] = pet_state
    pet['soc'] = pet_soc
    pet_soc_time_slot(pet)
