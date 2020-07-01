# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-02 12:28:50
@LastEditTime: 2020-06-30 23:54:21
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np

import region_revenue_gap
import request_soc


def pet_acceptance(t, manhattan_pcs_pet, pet_soc, revenue_gap, number_of_pcs, shape_waiting_time, number_of_pet):
    # 1. soc
    soc_rate = request_soc.request_soc(t, pet_soc)
    soc_rate = np.tile(soc_rate, (number_of_pcs, 1))
    # 2. distance: sort the distance matrix by row. The acceptance rates are calculated by the positions. If the distance is the third largest one, the rate will be 30%.
    sort_distance = (np.argsort(-manhattan_pcs_pet, axis=0)+1) * 0.1
    # 3. passenger: sort the passenger matrix by row.
    sort_revenue_gap = (np.argsort(revenue_gap, axis=0)+1) * 0.1
    # 4. queue
    sort_waiting_time = (np.argsort(-shape_waiting_time, axis=0)+1) * 0.1
    # The acceptance rates are the average of the four percentages.
    acceptance = (soc_rate + sort_distance +
                  sort_revenue_gap + sort_waiting_time)/4
    #   soc < 0.15
    soc_low = np.where(pet_soc <= 0.2, 1, 0)
    accepted_soc_low = np.nonzero(soc_low)[0]
    for i in accepted_soc_low:
        acceptance[:, i] = np.ones(number_of_pcs)
    acceptance = np.array(list(map(lambda x: fun(x), acceptance.ravel()))
                          ).reshape(number_of_pcs, number_of_pet)
    return acceptance


def fun(x):
    p = np.array([x, 1-x])
    a = np.random.choice([1, 0], p=p.ravel())
    return a


if __name__ == "__main__":
    t = 7
    manhattan_pcs_pet = np.array([[1, 4, 7], [3, 20, 8]])
    pet_soc = np.array([[0.12], [0.4], [0.9]])
    revenue_gap = np.array([[2, 3, 4], [-1, 3, 0]])
    number_of_pcs = 2
    shape_waiting_time = np.array([[32, 55, 89], [45, 65, 88]])
    pet_acceptance(t, manhattan_pcs_pet, pet_soc, revenue_gap,
                   number_of_pcs, shape_waiting_time, 3)
    pass
