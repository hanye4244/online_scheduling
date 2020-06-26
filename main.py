# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-06 14:59:51
@LastEditTime: 2020-06-26 09:52:48
@LastEditors: Ye Han
@Description: The integer programming includes the acceptance rate of PETs.
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''


import numpy as np
import pandas as pd

import distance
import integer_opt
import passenger_demand
import pcs_arrival
import pcs_profit
import pcs_service_fee
import pcs_waiting_time
import pet_acceptance
import pet_location_time_slot
import pet_soc_time_slot
import pet_trigger_completed
import pet_trigger_pick_up
import pet_trigger_put_down
import pet_trigger_recommended
import pet_trigger_state
import pet_trigger_state_put_down
import pev_arrival
import queue_cdq
import queue_delay_aware
import queue_plq
import region_id
import region_revenue_gap

# tag: System initialization.
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# The number of PCSs, regions and PETs.
number_of_pcs = 9
number_of_region = 4
number_of_pet = 50
# tag: Initialize pcs.
pcs_lat = np.array([[39.92971299], [39.95035038], [39.98165317], [39.90016842], [
                   39.91376059], [39.96248785], [39.90577064], [39.99474787], [39.91769874]])
pcs_lon = np.array([[116.30829112], [116.39142449], [116.30966109], [116.35165101], [
                   116.31768771], [116.3934999], [116.36383875], [116.34447545], [116.30873046]])
pcs_region = region_id.region_id(pcs_lat, pcs_lon)
# PCS service rate.
number_of_plug = 5
charging_rate_of_each = 0.15
cdq_service_rate = np.full(
    (number_of_pcs, 1), (number_of_plug * charging_rate_of_each))
# PET battery characters.
pet_battery_capacity = np.full((1, number_of_pet), 1)
shape_capacity = np.tile(pet_battery_capacity, (number_of_pcs, 1))
power_consumption = np.full((1, number_of_pet), 0.004)
shape_power_consumption = np.tile(power_consumption, (number_of_pcs, 1))
# The service fee.
per_service_fee = 150
# The revenues of PETs during each time slot.
pet_average_revenue = 1
# Kilometer per time slot.
average_speed = 10
# Time slot electricity price.
electricity_price = [0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.38,  0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32,
                     1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 1.32, 0.83, 0.83, 0.83, 0.83, 0.83, 0.83]
profit_mean_list = []
block_cdq_mean_list = []
block_plq_mean_list = []
block_delay_aware_mean_list = []
# Tag: Variable parameters.
max_soc = 0.99
# max_soc_list = [0.15, 0.3, 0.45, 0.6, 0.75, 0.9]
passenger_demand_max = 4
# passenger_demand_max_list = [4, 3, 2, 1, 0, -1, -2]
# passenger_demand_max_list = [4]
V = 1
# V_list = [1]
# V_list = [10, 20, 30, 40, 50, 80, 100, 200, 300, 400]
# worst_case_delay_guarantee_list = [
#     1, 5, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000]
worst_case_delay_guarantee_list = [1]
# worst_case_delay_guarantee = 3
# print('worst_case_delay_guarantee', worst_case_delay_guarantee)
# for V in V_list:
for worst_case_delay_guarantee in worst_case_delay_guarantee_list:
    # Initialize pet.
    profit_list = []
    block_cdq_list = []
    block_plq_list = []
    block_delay_aware_list = []
    pet_lat = np.array([[39.96253373], [39.91457459], [39.92588301], [39.94986468], [39.9264644], [39.92094834], [39.90860704], [39.90056609], [39.98933747], [39.95777496], [39.93228032], [39.94989055], [39.99973724], [39.90173232], [39.92445588], [39.9616257], [39.94763049], [39.97825631], [39.99229355], [39.91681799], [39.92534945], [39.93672401], [39.92826405], [39.97009977], [39.94988704], [
        39.91694974], [39.93304921], [39.99114325], [39.94262374], [39.99083236], [39.90737595], [39.90142823], [39.91180923], [39.92800281], [39.99798076], [39.93303175], [39.92250838], [39.98032591], [39.99064253], [39.91587499], [39.9575109], [39.97697965], [39.96476319], [39.90019632], [39.91797975], [39.94547393], [39.96540044], [39.97884827], [39.90734119], [39.95631456]])
    pet_lon = np.array([[116.36472475], [116.3882789], [116.32234297], [116.38212617], [116.31774475], [116.30214439], [116.35531708], [116.37685496], [116.39610188], [116.30930473], [116.30828321], [116.39485067], [116.37321686], [116.37615293], [116.35095054], [116.3919535], [116.39262153], [116.30616914], [116.36412417], [116.39627141], [116.34724162], [116.35656495], [116.34527461], [116.3708312], [
        116.35659439], [116.3600659], [116.30292666], [116.35701078], [116.32588347], [116.31544209], [116.39851909], [116.32593198], [116.36915791], [116.33335334], [116.3583916], [116.37845508], [116.37318405], [116.34356882], [116.33087179], [116.3663933], [116.38774454], [116.38550602], [116.38443759], [116.3698688], [116.34138473], [116.37817646], [116.38369842], [116.38800506], [116.31696235], [116.3323365]])
    pet_soc = np.array([[0.82], [0.75], [0.78], [0.74], [0.72], [0.85], [0.80], [0.74], [0.88], [0.71], [0.77], [0.73], [0.86], [0.73], [0.83], [0.84], [0.85], [0.79], [0.85], [0.81], [0.85], [0.73], [0.84], [0.82], [
                       0.82], [0.71], [0.80], [0.82], [0.71], [0.76], [0.85], [0.74], [0.85], [0.87], [0.75], [0.87], [0.75], [0.78], [0.74], [0.88], [0.73], [0.84], [0.86], [0.85], [0.76], [0.81], [0.83], [0.82], [0.76], [0.88]])
    pet_state = np.zeros((number_of_pet, 1))
    pet_pick_up = np.zeros((number_of_pet, 1))
    pet_put_down = np.zeros((number_of_pet, 1))
    pet_completed = np.zeros((number_of_pet, 1))
    pet_recommended = np.zeros((number_of_pet, 1))
    # Initialize blocks of queues.
    block_cdq = np.full((number_of_pcs, 1), 3)
    block_plq = np.full((number_of_region, 1), 4)
    block_delay_aware = np.full((number_of_region, 1), 0)
    # Time slot iteration.
    for t in range(504):
        pet_pick_up = np.zeros((number_of_pet, 1))
        pet_put_down = np.zeros((number_of_pet, 1))
        pet_completed = np.zeros((number_of_pet, 1))
        pet_recommended = np.zeros((number_of_pet, 1))
        electricity_price_slot = electricity_price[t]
        pcs_cost = np.full((number_of_pcs, 1),
                           electricity_price_slot * 0.1 * 1000)
        pet_region = region_id.region_id(pet_lat, pet_lon)
        manhattan_pcs_pet = distance.distance_between_pcs_pet(
            pet_lat, pet_lon, pcs_lat, pcs_lon, number_of_pcs, number_of_pet)
        pick_up_probability = np.full(number_of_region, 0.8)
        pet_pick_up_probability = np.array(list(map(
            lambda x: pick_up_probability[x], pet_region))).reshape(number_of_pet, 1)
        waiting_time = pcs_waiting_time.pcs_waiting_time(
            cdq_service_rate, block_cdq)
        shape_waiting_time = np.tile(waiting_time, (1, number_of_pet))
        shape_soc = np.tile(pet_soc.reshape(
            1, number_of_pet), (number_of_pcs, 1))
        pet_power_consumption = shape_power_consumption*manhattan_pcs_pet
        pet_remaining_power = shape_soc - pet_power_consumption
        pet_power_demand = shape_capacity - pet_remaining_power
        charging_time = pet_power_demand / 0.15
        pev_arrival_rate, pev_arrival_num = pev_arrival.pev_arrival(
            t, number_of_pcs)
        pet_put_down = pet_trigger_put_down.pet_trigger_put_down(
            pet_state, number_of_pet, pet_soc)
        pet_state = pet_trigger_state_put_down.pet_trigger_state_put_down(
            pet_state, pet_put_down, number_of_pet)
        pet_completed = pet_trigger_completed.pet_trigger_completed(
            pet_soc, pet_state, number_of_pet)
        plq_arrival_rate = passenger_demand.passenger_demand(
            number_of_region, t, passenger_demand_max)
        delay_aware_arrival_rate = np.full(
            (number_of_region, 1), worst_case_delay_guarantee)
        # 统计需要参与充电过程的车辆的个数
        # recommended_num = np.where(
        #     (pet_soc < max_soc) & (pet_state == 0), 1, 0).sum()
        # Tag: PET utility functions analysis.
        # 计算区域之间的收入差距
        revenue_gap = region_revenue_gap.region_revenue_gap(
            number_of_region, number_of_pet, number_of_pcs, pet_average_revenue, pcs_region, pet_region, pet_pick_up_probability, pick_up_probability, block_plq)
        action, pet_pick_up_region = integer_opt.integer_opt(
            number_of_pet, number_of_pcs, pet_power_demand, block_cdq, pet_state, pet_lat, pet_lon, number_of_region, pet_region, pet_soc, pet_pick_up_probability, block_plq, plq_arrival_rate, delay_aware_arrival_rate, block_delay_aware, pet_remaining_power, V, per_service_fee, pev_arrival_rate, cdq_service_rate, pcs_cost, max_soc)
        acceptance = pet_acceptance.pet_acceptance(
            t, manhattan_pcs_pet, pet_soc, revenue_gap, number_of_pcs, shape_waiting_time, number_of_pet)
        action = action * acceptance
        pet_recommended = pet_trigger_recommended.pet_trigger_recommended(
            number_of_pet, action)
        pet_pick_up = pet_trigger_pick_up.pet_trigger_pick_up(
            pet_state, pet_recommended, number_of_region, pet_region, pet_soc, pet_pick_up_region, pet_pick_up)
        cdq_arrival_rate = pcs_arrival.pcs_arrival(
            action, pet_power_demand, number_of_pcs, number_of_pet, pev_arrival_rate)
        plq_service_rate = pet_pick_up_region
        delay_aware_service_rate = plq_service_rate
        service_fee = pcs_service_fee.pcs_service_fee(
            cdq_arrival_rate, per_service_fee)
        profit = pcs_profit.pcs_profit(
            service_fee, pcs_cost)
    # Tag: Update.
        pet_state = pet_trigger_state.pet_trigger_state(
            pet_state, pet_recommended, pet_pick_up, pet_completed, number_of_pet)
        pet_soc = pet_soc_time_slot.pet_soc_time_slot(
            pet_state, pet_soc, number_of_pet, block_cdq, action)
        pet_lat, pet_lon = pet_location_time_slot.pet_location_time_slot(
            pet_state, pet_lat, pet_lon, number_of_pet, action, pcs_lat, pcs_lon, pet_recommended, pet_completed)
        block_cdq = queue_cdq.queue_cdq(
            block_cdq, cdq_arrival_rate, number_of_pcs, cdq_service_rate)
        block_plq = queue_plq.queue_plq(
            block_plq, plq_arrival_rate, plq_service_rate, number_of_region)
        block_delay_aware = queue_delay_aware.queue_delay_aware(
            block_delay_aware, worst_case_delay_guarantee, delay_aware_service_rate, number_of_region, block_plq)
        # tag: time slot append.
        profit_list.append(profit.sum())
        block_cdq_list.append(block_cdq.sum())
        block_plq_list.append(block_plq.sum())
        # block_delay_aware_list.append(block_delay_aware.sum())
    pass
    # tag: Parameter print.
    print('V =', V)
    print("worst_case_delay_guarantee = ", worst_case_delay_guarantee)
    # print('profit_list =', profit_list)
    profit_mean_list.append(np.mean(profit_list))
    block_cdq_mean_list.append(np.mean(block_cdq_list))
    block_plq_mean_list.append(np.mean(block_plq_list))
    # block_delay_aware_mean_list.append(np.mean(block_delay_aware_list))
    # print(block_plq_list, 'block_plq_list')
# Tag: Result print.
print('profit_mean_list', profit_mean_list)
# print('block_cdq_mean_list', block_cdq_mean_list)
print('block_plq_mean_list', block_plq_mean_list)
print('-'*100)
