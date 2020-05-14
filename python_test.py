# , coding=utf-8
'''
@Author:, Ye, Han
@Date:, 2020-04-15, 11:52:03
@LastEditTime: 2020-05-14 10:42:49
@LastEditors: Ye Han
@Description:
@FilePath:, \Online_Scheduling\python_tast.py
@Copyright, (c), 2020, -, Ye, Han
All, rights, reserved.
'''

import numpy as np

number_of_pcs = 9
number_pev_arrival = np.random.randint(0, 5, size=[number_of_pcs, 72])
print(number_pev_arrival)
