# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-16 16:11:18
@LastEditTime: 2020-05-07 12:58:28
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\pet_trigger_pick_up.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def pet_trigger_pick_up(pet_state, pet_lat, pet_lon, pet_recommended, number_of_region, number_of_pet, pet_region, pet_soc, pet_pick_up_probability):
    pet = pd.DataFrame(pet_state, columns=['state'])
    pet['recommended'] = pet_recommended
    pet['soc'] = pet_soc
    pet['pick_up_probability'] = pet_pick_up_probability
    pet_pick_up = pet.apply(lambda x: np.random.choice(
        [0, 1], p=[1-x['pick_up_probability'], x['pick_up_probability']]) if ((x['state'] == 0) & (x['recommended'] != 1) & (x['soc'] > 40)) else 0, axis=1)
    return pet_pick_up.values.reshape(number_of_pet, 1)
    pass


if __name__ == '__main__':
    pet = pd.DataFrame(columns=['lat', 'lon'])
    pet_lat = (40 - 39.4) * np.random.random(10) + 39.4
    pet_lon = (117 - 116) * np.random.random(10) + 116
    number_of_region = 4
    pet_state = np.random.randint(0, 1, size=[10, 1])
    pet_recommended = np.random.randint(0, 2, size=[10, 1])
    percentage_of_pick_up_pet = np.random.random(10)
    pet_trigger_pick_up(pet_state, pet_lat, pet_lon,
                        pet_recommended, number_of_region)
