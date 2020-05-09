# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-21 16:55:16
@LastEditTime: 2020-05-08 10:05:39
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def queue_plq(block_plq, plq_arrival_rate, plq_servic_rate, number_of_region):
    plq = pd.DataFrame(block_plq, columns=['block_plq'])
    plq['queue_service'] = plq_servic_rate
    plq['test'] = plq.apply(lambda x: 0 if (
        x['queue_service'] > x['block_plq']) else (x['block_plq'] - x['queue_service']), axis=1)
    block_plq = plq['test'].values.reshape(
        number_of_region, 1) + plq_arrival_rate
    return block_plq


if __name__ == '__main__':
    block_plq = 0
    number_of_pet = 10
    number_of_region = 4
    pet_state = np.random.randint(0, 3, size=[number_of_pet, 1])
    pet_lat = (40 - 39.4) * np.random.random((number_of_pet, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((number_of_pet, 1)) + 116
    pet_region = region_id.region_id(pet_lat, pet_lon)
    pet_recommended = np.zeros((number_of_pet, 1))
    queue_plq(block_plq, number_of_region, pet_state, pet_lat,
              pet_lon, pet_recommended, number_of_pet, pet_region,)
