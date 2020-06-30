# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-13 17:09:01
@LastEditTime: 2020-06-30 15:46:55
@LastEditors: Ye Han
@Description: According to the triggers, give the states of PETs(charging, loaded, driving).
@FilePath: \Online_Scheduling\pet_trigger_state.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def pet_trigger_state(pet_state, pet_recommended, pet_pick_up, pet_completed, number_of_pet, charging_state, number_of_pcs):
    pet = pd.DataFrame(np.concatenate(
        [pet_state, pet_recommended, pet_pick_up, pet_completed], axis=1), columns=['state', 'recommended', 'pick_up', 'completed'])
    # pet.loc[pet['put_down'] == 1, 'state'] = 0
    pet.loc[pet['recommended'] == 1, 'state'] = 2
    pet.loc[pet['pick_up'] == 1, 'state'] = 1
    pet.loc[pet['completed'] == 1, 'state'] = 0
    shape_pet_completed = np.tile(pet_completed.T, (number_of_pcs, 1))
    test = np.where((shape_pet_completed == 1), 0, 1)
    charging_state = charging_state * test
    return pet['state'].values.reshape(number_of_pet, 1), charging_state


pass


if __name__ == '__main__':
    number_of_pet = 10
    pet_lat = (40 - 39.4) * np.random.random((number_of_pet, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((number_of_pet, 1)) + 116
    pet_soc = np.random.randint(30, 100, size=[number_of_pet, 1])
    pet_state = np.random.randint(0, 3, size=[number_of_pet, 1])
    pet_pick_up = np.zeros((number_of_pet, 1))
    pet_put_down = np.zeros((number_of_pet, 1))
    pet_completed = np.zeros((number_of_pet, 1))
    pet_recommended = np.zeros((number_of_pet, 1))
    pet_trigger_state(pet_state, pet_put_down,
                      pet_recommended, pet_pick_up, pet_completed)
