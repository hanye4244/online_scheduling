# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-02 12:28:50
@LastEditTime: 2020-06-03 12:30:12
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def fun(x):
    p = np.array([x, 1-x])
    index = np.random.choice([0, 1], p=p.ravel())
    return index


def fun_soc(x, y):
    if (x < 0.3):
        return 0
    else:
        return y


def pet_acceptance(manhattan_pcs_pet, pet_soc, block_plq, action, number_of_pet, revenue_gap, number_of_pcs):
    pet_recommended = action.sum(axis=0).reshape(number_of_pet, 1)
    manhattan_pcs_pet = np.sum(
        (manhattan_pcs_pet * action), axis=0).reshape(number_of_pet, 1)
    if ((np.max(manhattan_pcs_pet) - np.min(manhattan_pcs_pet)) != 0):
        manhattan_pcs_pet = (manhattan_pcs_pet -
                             np.min(manhattan_pcs_pet)) / (np.max(manhattan_pcs_pet) - np.min(manhattan_pcs_pet))
    pet_revenue = np.sum((revenue_gap * action),
                         axis=0).reshape(number_of_pet, 1)
    if ((np.max(pet_revenue) - np.min(pet_revenue)) != 0):
        pet_revenue = (pet_revenue -
                       np.min(pet_revenue)) / (np.max(pet_revenue) - np.min(pet_revenue))
    pet_soc_test = pet_soc * pet_recommended
    if ((np.max(pet_soc_test) - np.min(pet_soc_test)) != 0):
        pet_soc_test = (pet_soc_test -
                        np.min(pet_soc_test)) / (np.max(pet_soc_test) - np.min(pet_soc_test))
    acceptance = - pet_soc_test - manhattan_pcs_pet + pet_revenue
    if ((np.max(acceptance) - np.min(acceptance)) != 0):
        acceptance = (acceptance -
                      np.min(acceptance)) / (np.max(acceptance) - np.min(acceptance))
    acceptance = acceptance * pet_recommended
    test = np.array(list(map(fun, acceptance))) * pet_recommended.flatten()
    test = np.array(list(map(fun_soc, pet_soc, test)))
    reject_index = np.nonzero(test)[0]
    for i in reject_index:
        action[:, i] = np.zeros(number_of_pcs)
    return action
