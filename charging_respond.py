# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-04 15:19:25
@LastEditTime: 2020-06-04 16:12:48
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def charging_respond(pet_soc, number_of_pet, pet_state):
    charging_request = np.array(
        list(map(charging_state_test, pet_soc, pet_state))).reshape(1, number_of_pet)
    # print("charging_request", charging_request)
    return charging_request


def charging_state_test(soc, state):
    if soc >= 0.5:
        charging_test = 0
    elif ((soc < 0.5) and (soc >= 0.15) and (state == 0)):
        charging_test = np.random.randint(0, 2)
    elif ((soc < 0.15) and (state == 0)):
        charging_test = 1
    else:
        charging_test = 0
    return charging_test
