# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-19 15:37:44
@LastEditTime: 2020-06-14 15:54:57
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\region_revenue_gap.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def region_revenue_gap(number_of_region, number_of_pet, number_of_pcs, pet_average_revenue, pcs_region, pet_region, pet_pick_up_probability, pick_up_probability, block_plq):
    pet_region_passenger = list(map(lambda x: block_plq[x - 1], pet_region))
    pcs_region_passenger = list(map(lambda x: block_plq[x - 1], pcs_region))
    pet_region_passenger = np.array(
        pet_region_passenger).reshape(number_of_pet, 1)
    pcs_region_passenger = np.array(
        pcs_region_passenger).reshape(number_of_pcs, 1)
    shape_pet_region_passenger = np.tile(
        pet_region_passenger, (1, number_of_pcs)).T
    shape_pcs_region_passenger = np.tile(
        pcs_region_passenger, (1, number_of_pet))
    gap = (shape_pcs_region_passenger - shape_pet_region_passenger)
    gap_revenue = gap * pet_average_revenue
    return gap_revenue


if __name__ == '__main__':
    pet_region = np.random.randint(0, 5, size=[1, 10])
    number_of_region = 4
    pet_average_revenue = 25
    pcs_region = np.array([0, 1, 2, 2, 3, 1])
    region_revenue_gap(number_of_region, 10, 6,
                       pet_average_revenue, pcs_region, pet_region)
