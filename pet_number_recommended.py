# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-14 17:10:56
@LastEditTime: 2020-04-28 16:23:58
@LastEditors: Ye Han
@Description: Give the number of charging-recommended PETs of each region.
@FilePath: \Online_Scheduling\pet_number_recommended.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def number_charging_recommended_pet(pet_recommended, pet_region, number_of_region):
    pet = pd.DataFrame(pet_recommended, columns=['recommended'])
    pet['region'] = pet_region
    charging_recommended_region = pet.groupby('region')[
        'recommended'].sum()
    return charging_recommended_region.values.reshape(number_of_region, 1)
    pass


if __name__ == '__main__':
    pet_recommended = np.array([1, 0, 1, 1])
    pet_region = np.array([1, 2, 3, 3])
    number_of_region = 3
    number_charging_recommended_pet(
        pet_recommended, pet_region, number_of_region)
