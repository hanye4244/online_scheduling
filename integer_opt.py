# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-06 10:05:34
@LastEditTime: 2020-05-14 10:47:26
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import cvxpy as cv
import numpy as np
import pandas as pd


def integer_opt(number_of_pet, number_of_pcs, pet_power_demand, block_cdq, pet_state, pet_lat, pet_lon, number_of_region, pet_region, pet_soc, pet_pick_up_probability, block_plq, plq_arrival_rate, delay_aware_arrival_rate, block_delay_aware, utility_function, pet_remaining_power, V, per_service_fee, pev_arrival_rate, cdq_service_rate, pcs_cost):
    # Variable.
    x = cv.Variable((number_of_pcs, number_of_pet), boolean=True)
    # Objective function
    # Section: cdq
    cdq_arrival_rate = cv.sum(cv.multiply(pet_power_demand, x),
                              axis=1, keepdims=True) + pev_arrival_rate
    section_cdq_1 = cdq_arrival_rate - cdq_service_rate
    section_cdq = cv.sum(cv.multiply(section_cdq_1, block_cdq))
    # section_plq
    # pick up constraint
    pet = pd.DataFrame(pet_state, columns=['state'])
    pet['soc'] = pet_soc
    pet['state'] = pet_state
    pet['pick_up_probability'] = pet_pick_up_probability
    # pet_pick_up_ini = pet.apply(lambda x: np.random.choice([0, 1], p=[
    #     1-x['pick_up_probability'], x['pick_up_probability']]) if ((x['state'] == 0) & (x['soc'] > 1.5)) else 0, axis=1).values.reshape(1, number_of_pet)
    pet_region_matrix = np.zeros((number_of_region, number_of_pet))
    for i in range(number_of_pet):
        for j in range(number_of_region):
            if pet_region[i] == j:
                pet_region_matrix[j, i] = 1
            pass
        pass
    pass
    pet_recommended = cv.sum(x, axis=0, keepdims=True)
    pet_non_recommended = (np.ones((1, number_of_pet)) - pet_recommended)
    pet_available_ini = np.where(
        ((pet['state'] == 0) & (pet['soc'] > 1.5)), 1, 0).reshape(1, number_of_pet)
    pet_available = cv.multiply(pet_available_ini, pet_non_recommended)
    # pet_pick_up = cv.multiply(pet_non_recommended, pet_pick_up_ini)
    pet_available_region = pet_region_matrix @ pet_available.T
    pet_pick_up_region = cv.minimum(pet_available_region, block_plq)
    section_plq_2 = plq_arrival_rate - pet_pick_up_region
    section_plq = cv.sum(cv.multiply(block_plq, section_plq_2))
    # Section: Delay aware
    section_delay_aware = cv.sum(cv.multiply(
        block_delay_aware, (delay_aware_arrival_rate - pet_pick_up_region)))
    # section: profit
    section_profit = cv.sum(cv.multiply(
        cdq_arrival_rate, per_service_fee) - pcs_cost)
    objects = section_cdq - V * section_profit
    # objects = (section_plq + section_delay_aware +
    #            section_cdq) - V * section_profit
    constraints_2_right = np.full((number_of_pet, 1), 1)
    state_test = np.where((pet_state == 0), 1, 0)
    # SOC
    constraints_4_right = np.full((number_of_pcs, number_of_pet), 0)
    soc_test = np.where((pet_remaining_power < 0), 1, 0)
    # rem * x ==0
    # column sum
    constraints_5_right = np.full((1, number_of_pet), 1)
    constraints_6_right = np.full((number_of_pet, 1), 1)
    constraints_7_right = np.full((number_of_pet, 1), 1)
    soc_range_test = np.where((pet_soc > 1), 1, 0)
    soc_1 = np.where((pet_soc > 9), 1, 0)
    constraints = [state_test + pet_non_recommended.T >= constraints_2_right,
                   cv.multiply(soc_test, x) == constraints_4_right, pet_recommended <= constraints_5_right, soc_1 + pet_recommended.T <= constraints_6_right, soc_range_test + pet_recommended.T >= constraints_7_right]
    problem = cv.Problem(cv.Minimize(objects), constraints)
    problem.solve(solver=cv.CPLEX)
    return x.value, pet_pick_up_region.value, section_plq.value, section_delay_aware.value, section_cdq.value, section_profit.value, pet_available_region.value


if __name__ == '__main__':
    number_of_pet = 5
    number_of_pcs = 3
    pet_power_demand = np.random.randint(
        30, 60, size=[number_of_pcs, number_of_pet])
    block_cdq = np.random.randint(1, 4, size=[number_of_pet, 1])
    pet_state = np.array([0, 0, 0, 0, 0]).reshape(number_of_pet, 1)
    pet_lat = (40 - 39.9) * np.random.random((number_of_pet, 1)) + 39.9
    pet_lon = (116.4 - 116.3) * np.random.random((number_of_pet, 1)) + 116.3
    number_of_region = 3
    pet_region = np.random.randint(0, 4, size=[number_of_pet, 1])
    pet_soc = np.array([9, 10, 20, 7, 40]).reshape(number_of_pet, 1)
    pet_pick_up_probability = np.full((number_of_pet, 1), 1)
    block_plq = np.random.randint(0, 4, size=[number_of_region, 1])
    plq_arrival_rate = np.random.randint(0, 4, size=[number_of_region, 1])
    delay_aware_arrival_rate = np.full((number_of_region, 1), 2)
    block_delay_aware = np.random.randint(0, 4, size=[number_of_region, 1])
    utility_function = np.random.randint(
        400, 700, size=[number_of_pcs, number_of_pet])
    print('utility_function', utility_function)
    pet_remaining_power = np.array(
        [-10, 20, 20, 30, 23, 40, -30, 20, 20, 34, 34, 22, 34, 34, 23]).reshape(number_of_pcs, number_of_pet)
    print(pet_remaining_power)
    V = 0.1
    per_service_fee = 10
    integer_opt(number_of_pet, number_of_pcs, pet_power_demand, block_cdq, pet_state, pet_lat, pet_lon, number_of_region, pet_region, pet_soc,
                pet_pick_up_probability, block_plq, plq_arrival_rate, delay_aware_arrival_rate, block_delay_aware, utility_function, pet_remaining_power, V, per_service_fee, pev_arrival_rate, cdq_service_rate, pcs_cost)
