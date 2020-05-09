# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-20 09:16:06
@LastEditTime: 2020-04-28 16:10:33
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\constraint_action_column.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def constraint_action_column(action, number_of_pet):
    pet_charging_decision = action.sum(axis=0)
    test_array = np.where((pet_charging_decision < 1)
                          | (pet_charging_decision == 1), 0, 1)
    test_bool = bool(np.array(test_array).sum())
    return not test_bool


if __name__ == '__main__':
    action = np.array([[1, 0, 1], [1, 0, 0]])
    print(action)
    number_of_pet = 3
    constraint_action_column(action, number_of_pet)
