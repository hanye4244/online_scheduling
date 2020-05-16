# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-09 18:08:00
@LastEditTime: 2020-05-15 17:01:34
@LastEditors: Ye Han
@Description: The PETs will choose the nearest PCSs when they need to charge.
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd

import constraint_action_column
import constraint_soc
import constraint_state
import distance
import nearest_pcs_choose
import objective_function
import passenger_demand
import pcs_arrival
import pcs_profit
import pcs_service_fee
import pcs_waiting_time
import pet_location_time_slot
import pet_soc_time_slot
import pet_trigger_completed
import pet_trigger_pick_up
import pet_trigger_put_down
import pet_trigger_recommended
import pet_trigger_state
import pet_trigger_state_put_down
import pet_utility_function
import queue_cdq
import queue_delay_aware
import queue_plq
import region_id

# tag: System initialization.
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# The number of PCSs, regions and PETs.
number_of_pcs = 6
number_of_region = 4
number_of_pet = 15
# Initialize pcs.
pcs_lat = np.array([[39.915], [39.945], [39.975],
                    [39.915], [39.945], [39.975]])
pcs_lon = pet_choose([116.325], [116.375], [116.325],
                    [116.375], [116.325], [116.375]])
pcs_region= region_id.region_id(pcs_lat, pcs_lon)
# PCS service rate.
number_of_plug= 1
charging_rate_of_each= 15
cdq_service_rate = np.full(
    (number_of_pcs, 1), (number_of_plug * charging_rate_of_each))
# PET battery characters.
pet_battery_capacity=np.full((1, number_of_pet), 100)
shape_capacity=np.tile(pet_battery_capacity, (number_of_pcs, 1))
power_consumption=np.full((1, number_of_pet), 0.4)
shape_power_consumption=np.tile(power_consumption, (number_of_pcs, 1))
# The service fee.
per_service_fee=1
# The revenues of PETs during each time slot.
pet_average_revenue=25
# Kilometer per time slot.
average_speed=10
profit_mean_list=[]
block_cdq_mean_list=[]
block_plq_mean_list=[]
block_delay_aware_mean_list=[]
section_cdq_mean_list=[]
section_plq_mean_list=[]


for V in [2]:
    # Initialize pet.
    profit_list=[]
    block_cdq_list=[]
    block_plq_list=[]
    block_delay_aware_list=[]
    section_cdq_list=[]
    section_plq_list=[]
    passenger_demand_list=[]
    pet_lat=np.array([[39.95699865],
                        [39.90546982],
                        [39.9683827],
                        [39.94013469],
                        [39.92567399],
                        [39.93289525],
                        [39.95132112],
                        [39.95105727],
                        [39.96777505],
                        [39.99871827],
                        [39.99175799],
                        [39.92021242],
                        [39.99900578],
                        [39.99060987],
                        [39.95592922]])
    pet_lon=np.array([[116.39512796],
                        [116.36945924],
                        [116.38476896],
                        [116.39305604],
                        [116.38683138],
                        [116.30387258],
                        [116.3030354],
                        [116.36599219],
                        [116.39197718],
                        [116.37723497],
                        [116.30692452],
                        [116.35764129],
                        [116.30713447],
                        [116.32663698],
                        [116.319976]])
    pet_soc=np.arange(75, 90, 1).reshape(number_of_pet, 1)
    pet_state=np.zeros((number_of_pet, 1))
    pet_pick_up=np.zeros((number_of_pet, 1))
    pet_put_down=np.zeros((number_of_pet, 1))
    pet_completed=np.zeros((number_of_pet, 1))
    pet_recommended=np.zeros((number_of_pet, 1))
    # Initialize blocks of queues.
    block_cdq=np.full((number_of_pcs, 1), 30)
    block_plq=np.full((number_of_region, 1), 4)
    block_delay_aware=np.full((number_of_region, 1), 0)
    # tag: Variable parameter.
    worst_case_delay_guarantee=3
    pet_cost_max=600
    # tag: Time slot iteration.
    for t in range(18):
        electricity_price=np.random.choice(
            [0.2, 0.2, 0.2, 0.2], p = np.array([0.25, 0.25, 0.25, 0.25]))
        pcs_cost=np.full((number_of_pcs, 1), electricity_price * 0.1)
        pet_region=region_id.region_id(pet_lat, pet_lon)
        manhattan_pcs_pet=distance.distance_between_pcs_pet(
            pet_lat, pet_lon, pcs_lat, pcs_lon, number_of_pcs, number_of_pet)
        pick_up_probability=np.full(number_of_region, 1)
        pet_pick_up_probability=np.array(list(map(
            lambda x: pick_up_probability[x], pet_region))).reshape(number_of_pet, 1)
        waiting_time = pcs_waiting_time.pcs_waiting_time(
            cdq_service_rate, block_cdq)
        shape_waiting_time=np.tile(waiting_time, (1, number_of_pet))
        shape_soc=np.tile(pet_soc.reshape(
            1, number_of_pet), (number_of_pcs, 1))
        pet_power_consumption=shape_power_consumption*manhattan_pcs_pet
        pet_remaining_power=shape_soc - pet_power_consumption
        pet_power_demand=shape_capacity - pet_remaining_power
        charging_time=pet_power_demand / 15
        number_pev_arrival=np.random.randint(1, 2, size = [number_of_pcs, 1])
        pev_arrival_rate=number_pev_arrival * 20
        utility_function=pet_utility_function.pet_utility_function(number_of_region, number_of_pet, number_of_pcs, pet_average_revenue, pcs_region,
                                                                     pet_region, pet_pick_up_probability, pick_up_probability, pet_power_demand, electricity_price, shape_waiting_time, charging_time)
        pet_put_down=pet_trigger_put_down.pet_trigger_put_down(
            pet_state, number_of_pet, pet_soc)
        pet_state=pet_trigger_state_put_down.pet_trigger_state_put_down(
            pet_state, pet_put_down, number_of_pet)
        pet_completed=pet_trigger_completed.pet_trigger_completed(
            pet_soc, pet_state, number_of_pet)
        plq_arrival_rate=passenger_demand.passenger_demand(
            number_of_region, t)
        delay_aware_arrival_rate=np.full(
            (number_of_region, 1), worst_case_delay_guarantee)
        # tag:
        action=np.zeros((number_of_pcs, number_of_pet))
        action, pet_recommended=nearest_pcs_choose.nearest_pcs_choose(
            pet_soc, manhattan_pcs_pet, number_of_pet, action)
        optimization=objective_function.objective_function(action, block_cdq, block_plq, block_delay_aware, V, pet_state, number_of_pcs, number_of_pet, pet_lat, pet_lon, pet_region, pet_soc,
                                                             number_of_region, per_service_fee, cdq_service_rate, plq_arrival_rate, delay_aware_arrival_rate, pet_pick_up_probability, shape_capacity, pet_power_demand, pev_arrival_rate, pcs_cost)
        pet_recommended=pet_trigger_recommended.pet_trigger_recommended(
            number_of_pet, action)
        pet_pick_up=pet_trigger_pick_up.pet_trigger_pick_up(
            pet_state, pet_lat, pet_lon, pet_recommended, number_of_region, number_of_pet, pet_region, pet_soc, pet_pick_up_probability)
        pet_region_matrix=np.zeros((number_of_region, number_of_pet))
        for i in range(number_of_pet):
            for j in range(number_of_region):
                if pet_region[i] == j:
                    pet_region_matrix[j, i]=1
                pass
            pass
        pass
        pet_pick_up_region=np.dot(pet_region_matrix, pet_pick_up)
        cdq_arrival_rate=pcs_arrival.pcs_arrival(
            action, pet_power_demand, number_of_pcs, number_of_pet, pev_arrival_rate)
        plq_service_rate=pet_pick_up_region
        delay_aware_service_rate=plq_service_rate
        service_fee=pcs_service_fee.pcs_service_fee(
            cdq_arrival_rate, per_service_fee)
        profit=pcs_profit.pcs_profit(
            service_fee, pcs_cost)
    # tag: Update.
        pet_state=pet_trigger_state.pet_trigger_state(
            pet_state, pet_recommended, pet_pick_up, pet_completed, number_of_pet)
        pet_soc=pet_soc_time_slot.pet_soc_time_slot(
            pet_state, pet_soc, number_of_pet, block_cdq, action)
        pet_lat, pet_lon=pet_location_time_slot.pet_location_time_slot(
            pet_state, pet_lat, pet_lon, number_of_pet, action, pcs_lat, pcs_lon, pet_recommended)
        block_cdq=queue_cdq.queue_cdq(
            block_cdq, cdq_arrival_rate, number_of_pcs, cdq_service_rate)
        block_plq=queue_plq.queue_plq(
            block_plq, plq_arrival_rate, plq_service_rate, number_of_region)
        block_delay_aware=queue_delay_aware.queue_delay_aware(
            block_delay_aware, worst_case_delay_guarantee, delay_aware_service_rate, number_of_region, block_plq)
        # tag: time slot print.
        # print('action', action)
        # print('SOC', pet_soc)
        # section_cdq_list.append(section_cdq)
        # section_plq_list.append(section_plq)
        # block_cdq_list.append(block_cdq)
        # block_plq_list.append(block_plq)
        # passenger_demand_list.append(plq_arrival_rate.sum())
        profit_list.append(profit.sum())
        # print('t =', t)
        # print('utility function', utility_function * action)
        # print('num_pet_recommended', pet_recommended.sum())
        # print('pet_pick_up_probability', pet_pick_up_probability)
        # print('section_plq', section_plq)
        # print('section_delay_aware', section_delay_aware)
        # print('section_profit', section_profit)
        # print('plq_arrival_rate', plq_arrival_rate)
        # print('plq_service_rate', plq_service_rate)
        # print('block_plq', block_plq)
        # print('block_delay_aware', block_delay_aware)
        # print('pet_pick_up_region', pet_pick_up_region)
        # print('pet_region', pet_region)
    pass
    # tag: Parameter print.
    # profit_mean_list.append(np.mean(profit_list))
    # block_cdq_mean_list.append(np.mean(block_cdq_list))
    # block_plq_mean_list.append(np.mean(block_plq_list))
    # section_cdq_mean_list.append(np.mean(section_cdq_list))
    # section_plq_mean_list.append(np.mean(section_plq_list))
    # print('worst_case_delay_guarantee =', worst_case_delay_guarantee)
# tag: Result print.
print(profit_list)
# print(passenger_demand_list)
