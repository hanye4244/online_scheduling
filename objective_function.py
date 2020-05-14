# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-21 16:34:32
@LastEditTime: 2020-05-06 16:11:34
@LastEditors: Ye Han
@Description: Calculate the objective function for each action.
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''


import pcs_arrival
import pcs_profit
import pcs_service_fee
import pet_number_pick_up
import pet_trigger_pick_up
import pet_trigger_recommended


def objective_function(action, block_cdq, block_plq, block_delay_aware, V, pet_state, number_of_pcs, number_of_pet, pet_lat, pet_lon, pet_region, pet_soc, number_of_region, per_service_fee, cdq_service_rate, plq_arrival_rate, delay_aware_arrival_rate, pet_pick_up_probability, shape_capacity, pet_power_demand, pev_arrival_rate, pcs_cost):
    # print('action =', action)
    pet_recommended = pet_trigger_recommended.pet_trigger_recommended(
        number_of_pet, action)
    pet_pick_up = pet_trigger_pick_up.pet_trigger_pick_up(
        pet_state, pet_lat, pet_lon, pet_recommended, number_of_region, number_of_pet, pet_region, pet_soc, pet_pick_up_probability)
    cdq_arrival_rate = pcs_arrival.pcs_arrival(
        action, pet_power_demand, number_of_pcs, number_of_pet, pev_arrival_rate)
    # print('cdq_arrival_rate=', cdq_arrival_rate)
    plq_pet_choosete = pet_number_pick_up.pet_number_pick_up(
        pet_pick_up, number_of_region, pet_region)
    # print('plq_service_rate=', plq_service_rate)
    delay_aware_service_rate = plq_service_rate
    service_fee = pcs_service_fee.pcs_service_fee(
        cdq_arrival_rate, per_service_fee)
    profit = pcs_profit.pcs_profit(
        service_fee, pcs_cost)
    # Calculate the objective function.
    section_cdq = block_cdq*(cdq_arrival_rate - cdq_service_rate)
    section_cdq_sum = section_cdq.sum()
    # print('section_cdq =', section_cdq_sum)
    section_plq = block_plq*(plq_arrival_rate - plq_service_rate)
    section_plq_sum = section_plq.sum()
    # print('section_plq_sum =', section_plq_sum)
    section_delay_aware = block_delay_aware * \
        (delay_aware_arrival_rate - delay_aware_service_rate)
    section_delay_aware_sum = section_delay_aware.sum()
    # print('section_delay_aware_sum =', section_delay_aware_sum)
    section_objective_function = 0 - V * profit
    # print('profit =', profit)
    section_objective_function_sum = section_objective_function.sum()
    objective = section_cdq_sum + section_plq_sum + \
        section_delay_aware_sum + section_objective_function_sum
    # print('objective =', objective)
    return objective
