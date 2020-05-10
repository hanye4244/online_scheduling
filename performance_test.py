# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-08 12:06:08
@LastEditTime: 2020-05-10 11:12:20
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import matplotlib.pyplot as plt
import numpy as np

x = range(18)

y_7 = [119.88000000000001, 185.88950986650022, 308.3856878961958, 238.0157048763942, 269.49054598259704, 303.3438502943749, 194.85793690861237, 189.61069776037468, 254.75107930706253, 272.3991257657485, 291.90671110503814, 248.72708678046655, 343.1845971061315, 190.4135309469057, 119.88000000000001, 191.07279817129034,
       238.29795581344166, 266.231877415098]
fig = plt.figure()
fig1 = fig.plot(x, y, color="r", linestyle="-",
                marker="^", linewidth=1.0)
# fig2 = fig1.twinx()
# fig2.plot(x, y_6, color="b", linestyle="-",


plt.show()
