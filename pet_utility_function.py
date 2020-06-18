# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-20 08:41:11
@LastEditTime: 2020-06-02 15:31:20
@LastEditors: Ye Han
@Description: The cost of PET
@FilePath: \Online_Scheduling\pet_utility_function.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np

import region_revenue_gap


def pet_utility_function(number_of_region, number_of_pet, number_of_pcs, pet_average_revenue, pcs_region, pet_region, pet_pick_up_probability, pick_up_probability, pet_power_demand, electricity_price, shape_waiting_time, charging_time, block_plq):
    # Distance power consumption-->price.
    pet_charging_cost = pet_power_demand * electricity_price
    # Waiting time revenue.Charging time revenue.
    pet_average_revenue_cost = (
        shape_waiting_time + charging_time)
    # The revenues gap.
    revenue_gap, shape_pcs_region_passenger = region_revenue_gap.region_revenue_gap(
        number_of_region, number_of_pet, number_of_pcs, pet_average_revenue, pcs_region, pet_region, pet_pick_up_probability, pick_up_probability, block_plq)
    utility = pet_charging_cost + pet_average_revenue_cost + revenue_gap
    return utility, pet_charging_cost, pet_average_revenue_cost, revenue_gap, shape_pcs_region_passenger


if __name__ == '__main__':
    pet_lat = (40 - 39.4) * np.random.random((10, 1)) + 39.4
    pet_lon = (117 - 116) * np.random.random((10, 1)) + 116
    pcs_lat = (40 - 39.4) * np.random.random((6, 1)) + 39.4
    pcs_lon = (117 - 116) * np.random.random((6, 1)) + 116
    action = np.random.randint(0, 2, size=[6, 10])
    pet_battery_capacity = np.full((1, 10), 100)
    power_consumption = np.full((1, 6), 0.5)
    manhattan_pcs_pet = np.random.randint(10, 20, size=[6, 10])
    pet_soc = np.random.randint(30, 90, size=[1, 10])
    number_of_pcs = 6

    block_pcs = 40
    queue_service = 8
    number_of_pet = 10
    number_of_region = 4
    pet_average_revenue = 25
    pcs_region = np.random.randint(0, 4, size=[1, 6])
    pet_region = np.random.randint(0, 4, size=[1, 10])
    pick_up_probability = np.random.random(number_of_region)
    average_speed = 0.0001
    pet_utility_function(block_pcs, action, pet_battery_capacity, power_consumption, manhattan_pcs_pet, pet_soc,
                         number_of_pcs, queue_service, number_of_region, number_of_pet, pet_average_revenue, pcs_region, pet_region, pick_up_probability)
