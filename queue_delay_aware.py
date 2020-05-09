# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-21 16:55:49
@LastEditTime: 2020-04-30 12:19:21
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import pandas as pd


def queue_delay_aware(block_delay_aware, worst_case_delay_guarantee, delay_aware_service_rate, number_of_region, block_plq):

    delay_aware = pd.DataFrame(
        block_delay_aware, columns=['block_delay_aware'])
    delay_aware['block_plq'] = block_plq
    delay_aware['queue_service'] = delay_aware_service_rate
    delay_aware['queue_arrival'] = delay_aware.apply(
        lambda x: 0 if (x['block_plq'] == 0) else worst_case_delay_guarantee, axis=1)
    delay_aware['test'] = delay_aware.apply(lambda x: 0 if (
        x['queue_service'] > x['block_delay_aware']) else (x['block_delay_aware'] - x['queue_service']), axis=1)
    block_delay_aware = delay_aware['test'].values.reshape(
        number_of_region, 1) + delay_aware['queue_arrival'].values.reshape(number_of_region, 1)
    return block_delay_aware
