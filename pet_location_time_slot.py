# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-19 11:58:49
@LastEditTime: 2020-04-28 16:22:38
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\pet_location_time_slot.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def charging_lat(action, lat, number_of_pet):
    charge_lat = np.sum(action * np.tile(lat, (1, number_of_pet)), axis=0)
    return charge_lat
    pass


def charging_lon(action, lon, number_of_pet):
    charge_lon = np.sum(action * np.tile(lon, (1, number_of_pet)), axis=0)
    return charge_lon
    pass


def pet_location_time_slot(pet_state, pet_lat, pet_lon, number_of_pet, action, pcs_lat, pcs_lon, pet_trigger_recommended):
    pet = pd.DataFrame(np.concatenate(
        [pet_state, pet_lat, pet_lon], axis=1), columns=['state', 'lat', 'lon'])
    pet['charge_lat'] = charging_lat(action, pcs_lat, number_of_pet)
    pet['charge_lon'] = charging_lon(action, pcs_lon, number_of_pet)
    pet['pet_trigger_recommended'] = pet_trigger_recommended
    pet['lat'] = pet.apply(lambda x: ((40 - 39.9) * np.random.random() + 39.9)
                           if (x['state'] != 2) else x['lat'], axis=1)
    pet['lon'] = pet.apply(lambda x: ((116.4 - 116.3) * np.random.random() + 116.3)
                           if (x['state'] != 2) else x['lon'], axis=1)
    pet['lat'] = pet.apply(lambda x: x['charge_lat'] if (
        x['pet_trigger_recommended'] == 1) else x['lat'], axis=1)
    pet['lon'] = pet.apply(lambda x: x['charge_lon'] if (
        x['pet_trigger_recommended'] == 1) else x['lon'], axis=1)
    return pet['lat'].values.reshape(number_of_pet, 1), pet['lon'].values.reshape(number_of_pet, 1)
    pass


if __name__ == '__main__':
    number_of_pet = 3
    number_of_pcs = 2
    action = np.array([[1, 0, 0], [0, 0, 0]])
    pcs_lat = (40 - 39.4) * np.random.random((number_of_pcs, 1)) + 39.4
    pcs_lon = (117 - 116) * np.random.random((number_of_pcs, 1)) + 116
    pet_lat = (40 - 39.4) * np.random.random((number_of_pet, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((number_of_pet, 1)) + 116
    pet_trigger_recommended = np.random.randint(0, 2, size=[number_of_pet, 1])
    print('pcs_lat', pcs_lat)
    print('pcs_lon', pcs_lon)
    pet_soc = np.random.randint(30, 100, size=[number_of_pet, 1])
    pet_state = np.array([2, 0, 1]).reshape(3, 1)
    pet_location_time_slot(pet_state, pet_lat, pet_lon,
                           number_of_pet, action, pcs_lat, pcs_lon, pet_trigger_recommended)
