# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-05-08 12:06:08
@LastEditTime: 2020-05-27 15:27:22
@LastEditors: Ye Han
@Description:
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import matplotlib.pyplot as plt
import numpy as np

x = range(13, 19)
y = [1219.6098184519365, 1211.3724923227371, 1194.5444822997642,
     1181.1737099032782, 1171.2023753402946, 1166.752532611471]
# x = [0, 0.3, 0.5, 0.8, 1]
# y = [1131.3498600372452, 1216.0930057321825,
#      1284.087386387838, 1285.205471658799, 1285.613519967812]
# y_1 = [1130.9533497717987, 1164.9106732277503,
#        1166.5286607211372, 1172.4009615593473, 1174.0526020123998]
plt.plot(x, y, marker="*", color='#81D8D0')
# plt.plot(x, y_1, marker='s')
plt.show()
