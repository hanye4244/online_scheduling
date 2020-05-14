# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-16 15:46:28
@LastEditTime: 2020-05-11 16:36:30
@LastEditors: Ye Han
@Description: 
@FilePath: \Online_Scheduling\pet_trigger_completed.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def pet_trigger_completed(pet_soc, pet_state, number_of_pet):
    pet = pd.DataFrame(pet_state, columns=['state'])
    pet['soc'] = pet_soc
    pet_completed = pet.apply(
        lambda x: 1 if ((x['soc'] > 8.5) & (x['state'] == 2.0)) else 0, axis=1)
    pet['completed'] = pet_completed
    return pet['completed'].values.reshape(number_of_pet, 1)
    pass


if __name__ == '__main__':
    pet_soc = np.random.randint(90, 100, size=[6, 1])
    pet_state = np.random.randint(0, 3, size=[6, 1])
    pet_trigger_completed(pet_soc, pet_state)
