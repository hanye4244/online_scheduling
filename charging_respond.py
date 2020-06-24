# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-04 15:19:25
@LastEditTime: 2020-06-24 10:38:03
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd

import request_soc


def charging_respond(t, pet_soc, number_of_pet, pet_state):
    charging_request_rate = request_soc.request_soc(
        t, pet_soc)
    acceptance = np.array(
        list(map(lambda x: fun(x), charging_request_rate.ravel()))).reshape(number_of_pet, 1)
    charging_request = np.array(
        list(map(charging_state_test, pet_soc, pet_state, acceptance))).reshape(1, number_of_pet)
    # print("charging_request", charging_request)
    return charging_request


def charging_state_test(soc, state, acceptance):
    if ((soc <= 0.15) and (state == 0)):
        charging_test = 1
    elif ((soc > 0.15) and (state == 0)):
        charging_test = acceptance[0]
    else:
        charging_test = 0
    return charging_test


def fun(x):
    p = np.array([x, 1-x])
    a = np.random.choice([1, 0], p=p.ravel())
    return a
