# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-14 15:04:01
@LastEditTime: 2020-04-28 16:11:42
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\distance.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd
from pyproj import Proj, transform
from scipy.spatial.distance import cdist


def distance_between_pcs_pet(pet_lat, pet_lon, pcs_lat, pcs_lon, number_of_pcs, number_of_pet):
    p1 = Proj("epsg:4326")
    p2 = Proj("epsg:3857")
    pet_x, pet_y = p1(pet_lon, pet_lat)
    pcs_x, pcs_y = p1(pcs_lon, pcs_lat)
    pet_lon_meter, pet_lat_meter = transform(
        p1, p2, pet_x, pet_y, radians=False, always_xy=True)
    pcs_lon_meter, pcs_lat_meter = transform(
        p1, p2, pcs_x, pcs_y, radians=False, always_xy=True)
    pet_location = np.concatenate(
        (pet_lat_meter.reshape(number_of_pet, 1), pet_lon_meter.reshape(number_of_pet, 1)), axis=1)
    pcs_location = np.concatenate(
        (pcs_lat_meter.reshape(number_of_pcs, 1), pcs_lon_meter.reshape(number_of_pcs, 1)), axis=1)
    manhattan_pcs_pet = cdist(
        pcs_location, pet_location, metric='cityblock')
    return manhattan_pcs_pet/1000
    pass


if __name__ == '__main__':
    number_of_pcs = 10
    number_of_pet = 20
    pet_lat = (40 - 39.9) * np.random.random((number_of_pet, 1)) + 39.9
    pet_lon = (116.4 - 116.3) * np.random.random((number_of_pet, 1)) + 116.3
    pcs_lat = (40 - 39.9) * np.random.random((number_of_pcs, 1)) + 39.9
    pcs_lon = (116.4 - 116.3) * np.random.random((number_of_pcs, 1)) + 116.3
    distance_between_pcs_pet(pet_lat, pet_lon, pcs_lat,
                             pcs_lon, number_of_pcs, number_of_pet)
