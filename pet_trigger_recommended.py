# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-16 15:46:00
@LastEditTime: 2020-04-28 16:48:15
@LastEditors: Ye Han
@Description: 
@FilePath: \Online_Scheduling\pet_trigger_recommended.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def pet_trigger_recommended(number_of_pet, action):
    pet_charging_decision = action.sum(axis=0).reshape(number_of_pet, 1)
    return pet_charging_decision


if __name__ == '__main__':
    number_of_pet = 3
    action = np.array([[0, 0, 0], [0, 1, 1]])
    pet_trigger_recommended(number_of_pet, action)
