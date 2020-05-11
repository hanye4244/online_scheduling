# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-08 12:06:08
@LastEditTime: 2020-05-11 10:50:34
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import matplotlib.pyplot as plt
import numpy as np

time_slot = range(18)
profit_online = [477.37696954041166, 119.88000000000001, 401.3795038639372, 119.88000000000001, 357.77475587035246, 119.88000000000001, 334.9146746478079, 119.88000000000001, 314.0973567643589, 119.88000000000001, 308.0402801959464, 119.88000000000001, 308.9778764241155, 119.88000000000001, 295.0430027320203, 119.88000000000001,
                 299.9050828739896, 119.88000000000001]
profit_random = [119.88000000000001, 185.88950986650022, 308.3856878961958, 238.0157048763942, 269.49054598259704, 303.3438502943749, 194.85793690861237, 189.61069776037468, 254.75107930706253,
                 272.3991257657485, 291.90671110503814, 248.72708678046655, 343.1845971061315, 190.4135309469057, 119.88000000000001, 191.07279817129034, 238.29795581344166, 266.231877415098]
sum_profit_online = [None] * 18
sum_profit_online[0] = profit_online[0]
for i in range(1, 18):
    sum_profit_online[i] = profit_online[i]+sum_profit_online[i - 1]
sum_profit_random = [None] * 18
sum_profit_random[0] = profit_random[0]
for i in range(1, 18):
    sum_profit_random[i] = profit_random[i]+sum_profit_random[i - 1]
plt.plot(time_slot, sum_profit_online,
         color='red', marker="^")
plt.plot(time_slot, sum_profit_random,
         color='blue', marker="+")
plt.show()
