# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-08 12:06:08
@LastEditTime: 2020-05-27 11:57:28
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import matplotlib.pyplot as plt
import numpy as np

x = [1, 5, 9, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1141.7092489394863, 1144.735767345073, 1150.4671551899216, 1151.6502974600542, 1152.1223914642333,
     1152.4746279045767, 1152.7905080386126, 1152.0560128242473, 1151.9905131104501, 1151.9081498533794, 1151.69884045252]
# x = [0, 0.3, 0.5, 0.8, 1]
# y = [1131.3498600372452, 1216.0930057321825,
#      1284.087386387838, 1285.205471658799, 1285.613519967812]
# y_1 = [1130.9533497717987, 1164.9106732277503,
#        1166.5286607211372, 1172.4009615593473, 1174.0526020123998]
plt.plot(x, y, marker="*", color='#81D8D0')
# plt.plot(x, y_1, marker='s')
plt.show()
