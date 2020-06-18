# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-19 16:02:17
@LastEditTime: 2020-06-09 09:54:35
@LastEditors: Ye Han
@Description:
@FilePath: \Online_Scheduling\passenger_demand.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import numpy as np

# def fun(x):
#     a = round(x/1000)
#     return a
#     pass


# region1 = [8940, 8104, 6911, 8316, 7065, 5723, 5658, 5706, 5544, 5280, 5391, 5990, 5166, 5207, 5345, 5779, 6430, 5741, 5914, 4935, 5036, 5360, 6557, 7204, 9012, 9811, 9843, 11052, 11906, 11668, 12435, 11926, 12132, 14228, 15794, 16313, 14902, 11664, 10805, 11310, 10461, 9281, 9769, 10005,
#            10702, 9673, 9239, 8436, 9880, 10422, 8344, 8040, 7267, 6320, 6524, 7907, 7410, 9061, 9386, 11168, 11094, 9072, 10307, 9001, 8230, 7605, 7370, 7493, 7334, 8067, 8327, 8101]
# region2 = [7590, 8107, 7462, 6915, 6803, 6792, 5876, 5781, 5762, 5263, 5421, 5467, 4999, 5002, 4907, 5451, 5766, 5821, 5937, 5704, 6403, 7059, 8025, 7938, 9159, 8874, 10280, 10665, 10715, 10206, 9734, 9366, 10297, 10117, 9164, 8925, 8722, 7953, 7662, 7383, 7035, 6468, 6842, 6929, 7307, 6692, 6391, 6013, 6246, 5600, 5649, 6062, 5829, 5560, 5329, 5512, 6545, 6513, 5698, 5744, 6773, 6287, 6805,
#            6218, 5368, 4631, 4586, 4556, 5001, 5289, 5976, 6926]
# region3 = [9327, 12041, 11579, 12092, 12010,
#            11667, 12199, 12548, 11956, 11838,
#            12013, 11916, 11097, 10249, 9404, 7769, 6376, 6459, 7031, 7014, 8337,
#            8742, 9924, 9691, 9555, 10623, 10491, 10451, 12368, 14000, 14234, 14910, 14027, 14168, 14388, 14823, 14116, 13345, 12347, 11851, 11666, 11070, 12694, 12826, 12085, 12092, 12767, 12185, 10693, 9585, 9367, 7802,
#            7577, 7970, 7626, 8724, 9326, 9581, 11176, 11725, 11358, 10776, 10040, 9445, 8119, 7969, 6965, 6683, 7000, 7835, 7327, 7694]
# region4 = [8330, 8901, 8516, 9107, 9115, 8906, 8386, 7969, 8611, 8538, 7414, 7329, 7615, 6179, 5617, 3837, 4445, 5072, 4671, 5226, 5222, 6073, 5920, 7702, 8855, 9705, 10752, 11783, 14762, 14387, 16470, 15800, 16142, 17207, 17468, 15331, 14765, 13777, 12943, 11082, 11557, 11871, 12098, 11957, 12661, 12605, 11705, 12275, 12233, 10802, 10371, 8899, 7439, 7202,
#            7673, 7381, 9149, 10216, 11073, 11785, 12648, 12131, 9782, 8897, 8075, 6842, 6064, 7251, 7002, 7828, 8463, 8589]
# passenger_demand_1 = list(map(lambda x: fun(x), region1))
# passenger_demand_2 = list(map(lambda x: fun(x), region2))
# passenger_demand_3 = list(map(lambda x: fun(x), region3))
# passenger_demand_4 = list(map(lambda x: fun(x), region4))

# for i in passenger_demand_1:
#     print(i, end=',')
# print('111')
# for i in passenger_demand_2:
#     print(i, end=',')
# print('111')
# for i in passenger_demand_3:
#     print(i, end=',')
# print('111')
# for i in passenger_demand_4:
#     print(i, end=',')
def passenger_demand(number_of_region, t, passenger_demand_max):
    passenger_demand = np.array([[7,  8,  7,  7,  7,  7,  7,  7,  7,  6,  6,  5,  5,  5,  5,  5,  6,  6,  5,  5,  4,  4,  6,  7,
                                  8,  8,  9,  9, 10, 11, 12, 12, 14, 13, 14, 16, 16, 14, 12, 11, 11, 10, 10, 10, 10,  9, 10,  9,
                                  9,  7,  8,  7,  7,  6,  6,  6,  7,  7,  7,  9,  9,  9,  8,  8,  7,  7,  6,  6,  6,  6,  7,  8, 8, 8, 7, 7, 6, 6, 6, 5, 6, 6, 6, 5, 4, 5, 5, 7, 6, 6, 6, 5, 6, 5, 6, 7, 8, 8, 8, 9, 10, 11, 12, 12, 13, 14, 14, 14, 13, 11, 11, 10, 10, 10, 10, 9, 10, 9, 9, 9, 10, 8, 7, 6, 6, 6, 7, 8, 8, 8, 9, 9, 10, 9, 8, 6, 6, 6, 6, 7, 8, 8, 9, 9, 7, 6, 7, 7, 7, 6, 6, 6, 5, 5, 6, 5, 5, 5, 5, 5, 5, 6, 5, 5, 7, 7, 8, 8, 8, 9, 11, 12, 10, 10, 9, 7, 7, 7, 7, 6, 6, 7, 7, 8, 8, 8, 7, 8, 7, 7, 7, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 5, 5, 5, 4, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 5, 5, 6, 5, 6, 6, 5, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 7, 7, 9, 9, 9, 11, 11, 12, 11, 11, 12, 13, 12, 11, 10, 11, 11, 11, 10, 11, 12, 12, 11, 11, 10, 9, 8, 8, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 8, 7, 7, 7, 6, 6, 6, 7, 7, 8, 7, 7, 8, 8, 7, 7, 6, 6, 6, 5, 6, 6, 6, 5, 4, 5, 5, 7, 6, 6, 6, 5, 6, 5, 6, 7, 8, 8, 8, 9, 10, 11, 12, 12, 13, 14, 14, 14, 13, 11, 11, 10, 10, 10, 10, 9, 10, 9, 9, 9, 10, 8, 7, 6, 6, 6, 7, 8, 8, 8, 9, 9, 10, 9, 8, 6, 6, 6, 6, 7, 8, 8, 9, 9, 9, 8, 7, 8, 7, 6, 6, 6, 6, 5, 5, 6, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 7, 7, 9, 10, 10, 11, 12, 12, 12, 12, 12, 14, 16, 16, 15, 12, 11, 11, 10, 9, 10, 10, 11, 10, 9, 8, 10, 10, 8, 8, 7, 6, 7, 8, 7, 9, 9, 11, 11, 9, 10, 9, 8, 8, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                                 [7,  7,  6,  6,  6,  6,  6,  5,  6,  5,  5,  5,  5,  5,  4,  4,  5,  5,  5,  5,  5,  6,  7,  7,
                                  8,  9, 8, 9,  9,  9,  9,  9, 11, 10, 10, 10, 10, 10,  8,  8,  7,  7,  6,  7,  7,  7,  7,  6, 6,  6,  6,  6,  5,  6,  6,  6,  7,  7,  6,  6,  6,  6,  6,  6,  5,  5,  5,  4,  5,  5,  6,  6, 6, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 6, 7, 9, 8, 8, 9, 9, 9, 9, 9, 10, 9, 9, 8, 8, 7, 7, 7, 8, 8, 7, 6, 6, 6, 6, 7, 7, 7, 6, 6, 6, 5, 6, 6, 6, 7, 7, 7, 6, 5, 5, 5, 5, 6, 6, 6, 8, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 7, 6, 7, 6, 6, 6, 6, 7, 7, 7, 7, 6, 6, 6, 5, 5, 6, 6, 5, 5, 5, 6, 5, 5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 5, 5, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 5, 5, 4, 4, 5, 5, 5, 6, 8, 8, 7, 7, 7, 7, 7, 8, 9, 9, 8, 8, 8, 8, 8, 7, 7, 7, 8, 7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 4, 6, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 5, 6, 7, 9, 8, 8, 9, 9, 9, 9, 9, 10, 9, 9, 8, 8, 7, 7, 7, 8, 8, 7, 6, 6, 6, 6, 7, 7, 7, 6, 6, 6, 5, 6, 6, 6, 7, 7, 7, 6, 5, 5, 5, 5, 6, 6, 6, 8, 7, 8, 8, 7, 7, 7, 7, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 8, 8, 9, 9, 10, 11, 11, 10, 10, 9, 10, 10, 9, 9, 9, 8, 8, 7, 7, 6, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 7, 7, 6, 6, 7, 6, 7, 6, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7],
                                 [10, 12, 14, 13, 14, 14, 14, 15, 15, 15, 14, 14, 13, 13, 10,  9,  7,  5,  6,  7,  8,  9, 10, 10,
                                  11, 12, 11, 11, 10, 12, 12, 13, 13, 15, 15, 15, 15, 14, 12, 11, 11, 11, 12, 12, 12, 12, 12, 13,
                                  13, 11, 10, 10, 10,  9, 10,  9,  9, 10, 11, 11, 11, 11, 11, 10,  9,  8,  8,  8,  8,  8,  8,  8, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11, 11, 11, 10, 9, 8, 7, 7, 7, 7, 7, 8, 8, 9, 10, 9, 9, 9, 10, 12, 13, 14, 15, 14, 14, 14, 14, 13, 12, 12, 11, 11, 12, 12, 11, 12, 12, 10, 10, 10, 10, 9, 9, 9, 8, 9, 9, 10, 12, 11, 11, 11, 9, 9, 8, 7, 9, 8, 8, 8, 9, 8, 8, 8, 9, 10, 11, 11, 12, 13, 13, 14, 14, 14, 14, 14, 13, 13, 12, 10, 9, 10, 9, 9, 9, 10, 9, 10, 12, 14, 14, 13, 12, 11, 9, 9, 7, 8, 8, 7, 8, 8, 9, 9, 9, 9, 9, 8, 8, 7, 8, 9, 9, 8, 8, 7, 8, 8, 7, 7, 8, 9, 8, 9, 8, 9, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 10, 10, 10, 9, 10, 10, 10, 10, 9, 9, 9, 9, 9, 8, 8, 9, 8, 8, 8, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 10, 10, 9, 9, 9, 10, 9, 9, 9, 9, 9, 9, 9, 7, 10, 11, 10, 11, 11, 11, 11, 11, 11, 11, 10, 10, 9, 8, 8, 7, 7, 7, 7, 7, 7, 8, 9, 9, 9, 9, 10, 11, 14, 15, 17, 15, 15, 15, 15, 15, 14, 14, 14, 13, 13, 13, 13, 12, 12, 12, 13, 12, 11, 10, 9, 10, 9, 9, 9, 9, 10, 12, 12, 12, 12, 10, 10, 9, 9, 10, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 10, 11, 11, 11, 11, 11, 11, 11, 10, 9, 8, 7, 7, 7, 7, 7, 8, 8, 9, 10, 9, 9, 9, 10, 12, 13, 14, 15, 14, 14, 14, 14, 13, 12, 12, 11, 11, 12, 12, 11, 12, 12, 10, 10, 10, 10, 9, 9, 9, 8, 9, 9, 10, 12, 11, 11, 11, 9, 9, 8, 7, 9, 8, 8, 8, 9, 8, 8, 9, 12, 12, 12, 12, 12, 12, 13, 12, 12, 12, 12, 11, 10, 9, 8, 6, 6, 7, 7, 8, 9, 10, 10, 10, 11, 10, 10, 12, 14, 14, 15, 14, 14, 14, 15, 14, 13, 12, 12, 12, 11, 13, 13, 12, 12, 13, 12, 11, 10, 9, 8, 8, 8, 8, 9, 9, 10, 11, 12, 11, 11, 10, 9, 8, 8, 7, 7, 7, 8, 7, 8, 8, 8, 8, 8, 8, 8, 8],
                                 [8,  8,  8,  7,  8,  7,  6,  7,  7,  7,  7,  6,  6,  6,  5,  4,  4,  4,  4,  4,  5,  5,  5,  7,
                                  7,  8, 10, 11, 11, 13, 14, 14, 15, 15, 17, 16, 16, 15, 12, 11, 11, 11, 10, 11, 11, 11, 10, 10,
                                  8,  9,  8,  8,  8,  7,  7,  7,  7,  8,  9, 11, 10,  9,  8,  8,  7,  6,  7,  7,  7,  7,  8,  9, 7, 7, 6, 5, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 7, 9, 10, 11, 13, 14, 13, 13, 13, 12, 14, 13, 13, 11, 10, 10, 10, 10, 12, 12, 11, 10, 11, 9, 10, 9, 8, 7, 8, 8, 8, 9, 9, 10, 10, 10, 9, 8, 8, 6, 6, 6, 6, 7, 8, 9, 9, 10, 8, 8, 6, 6, 7, 7, 8, 7, 7, 8, 8, 7, 7, 6, 6, 5, 4, 5, 4, 6, 6, 7, 8, 9, 11, 14, 14, 13, 11, 10, 9, 8, 9, 7, 7, 7, 7, 7, 7, 8, 9, 10, 9, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 5, 6, 6, 6, 5, 5, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 8, 10, 11, 13, 15, 15, 14, 14, 14, 12, 13, 14, 13, 10, 9, 10, 11, 11, 11, 11, 11, 11, 10, 10, 9, 9, 8, 7, 7, 7, 7, 7, 7, 7, 8, 9, 10, 8, 7, 7, 6, 6, 6, 6, 6, 7, 7, 6, 7, 7, 7, 6, 5, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 7, 9, 10, 11, 13, 14, 13, 13, 13, 12, 14, 13, 13, 11, 10, 10, 10, 10, 12, 12, 11, 10, 11, 9, 10, 9, 8, 7, 8, 8, 8, 9, 9, 10, 10, 10, 9, 8, 8, 6, 6, 6, 6, 7, 8, 9, 9, 10, 8, 9, 9, 9, 9, 9, 8, 8, 9, 9, 7, 7, 8, 6, 6, 4, 4, 5, 5, 5, 5, 6, 6, 8, 9, 10, 11, 12, 15, 14, 16, 16, 16, 17, 17, 15, 15, 14, 13, 11, 12, 12, 12, 12, 13, 13, 12, 12, 12, 11, 10, 9, 7, 7, 8, 7, 9, 10, 11, 12, 13, 12, 10, 9, 8, 7, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9]]) - passenger_demand_max
    passenger_demand_slot = passenger_demand[:, t]
    return passenger_demand_slot.reshape(number_of_region, 1)


    # return passenger_demand_slot.reshape(number_of_region, 1)
if __name__ == '__main__':
    number_of_region = 4
    passenger_demand(number_of_region, 1, 1)
