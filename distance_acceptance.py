# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-17 10:55:07
@LastEditTime: 2020-06-17 11:10:05
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np


def distance_acceptance(manhattan_pcs_pet):
    sort_distance = (np.argsort(-manhattan_pcs_pet, axis=1)+1) * 0.1
    print(sort_distance)
    return


if __name__ == "__main__":
    manhattan_pcs_pet = np.array([[22, 5, 4], [1, 6, 9]])
    distance_acceptance(manhattan_pcs_pet)
    pass
