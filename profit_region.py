# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-09 10:50:30
@LastEditTime: 2020-06-09 10:59:14
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np
import pandas as pd


def profit_region(pcs_region, profit):
    pcs = pd.DataFrame(pcs_region, columns=["region"])
    pcs["profit"] = profit
    avr_profit_region = pcs.groupby("region")["profit"].mean()
    return avr_profit_region


if __name__ == '__main__':
    pcs_region = [1, 2, 3, 1]
    profit = [11, 22, 33, 44]
    avr_profit_region = profit_region(pcs_region, profit)
    print(avr_profit_region)
