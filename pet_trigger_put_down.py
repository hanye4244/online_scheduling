# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-15 17:51:03
@LastEditTime: 2020-05-15 17:22:07
@LastEditors: Ye Han
@Description: PET passenger is put down random.
@FilePath: \Online_Scheduling\pet_trigger_put_down.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def pet_trigger_put_down(pet_state, number_of_pet, pet_soc):
    pet = pd.DataFrame(pet_state, columns=['state'])
    pet['soc'] = pet_soc
    pet['pet_put_down'] = pet.apply(lambda x: np.random.randint(
        0, 2) if (x['state'] == 1) else 0, axis=1)
    pet_put_down = pet.apply(lambda x: 1 if (
        (x['soc'] < 0.15) & (x['state'] == 1)) else x['pet_put_down'], axis=1)
    return pet_put_down.values.reshape(number_of_pet, 1)


if __name__ == '__main__':
    pet_state = np.random.randint(0, 3, size=[6, 1])
    print(pet_state)
    pet_trigger_put_down(pet_state)
