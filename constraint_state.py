# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-22 16:38:43
@LastEditTime: 2020-04-28 16:11:19
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def constraint_state(pet_state, action):
    pet_charging_decision = action.sum(axis=0)
    pet = pd.DataFrame(pet_charging_decision, columns=[
                       'pet_charging_decision'])
    pet['state'] = pet_state
    test = pet.apply(lambda x: 1 if ((x['state'] != 0)
                                     & (x['pet_charging_decision'] == 1)) else 0, axis=1)
    test_bool = bool(test.sum())
    return not test_bool


if __name__ == '__main__':
    number_of_pet = 3
    pet_state = np.random.randint(2, 4, size=[number_of_pet, 1])
    print(pet_state)
    action = np.array([[0, 0, 0], [0, 1, 1]])
    constraint_state(pet_state, action)
