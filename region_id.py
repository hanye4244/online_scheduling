# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-04-14 15:58:50
@LastEditTime: 2020-05-26 17:14:35
@LastEditors: Ye Han
@Description: This function returns the region IDs of the given locations.
@FilePath: \Online_Scheduling\region_id.py
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''

import numpy as np
import pandas as pd


def calculate_region_id(lon_cut, lat_cut):
    test = [i*100+j for i in range(1, 3) for j in range(1, 3)]
    region_id = lat_cut*100 + lon_cut
    return test.index(region_id)


def region_id(lat, lon):
    # note: change with number_of_region
    region_location = pd.DataFrame(lat, columns=['lat'])
    region_location['lon'] = lon
    bins_lat = [39.9, 39.95, 40]
    bins_lon = [116.3, 116.35, 116.4]
    # Cut the latitudes.
    lat_label = [1, 2]
    region_location['lat_cut'] = pd.cut(
        region_location['lat'], bins=bins_lat, labels=lat_label, include_lowest=True)
    # Cut the longitude.
    lon_label = [1, 2]
    region_location['lon_cut'] = pd.cut(
        region_location['lon'], bins=bins_lon, labels=lon_label, include_lowest=True)
    region_location['id'] = region_location.apply(
        lambda x: calculate_region_id(x['lon_cut'], x['lat_cut']), axis=1)
    region_location['id'] = region_location['id']
    return region_location['id'].values
    pass


if __name__ == '__main__':
    number_of_pcs = 10
    pcs_lat = (40 - 39.9) * np.random.random((number_of_pcs, 1)) + 39.9
    pcs_lon = (116.4 - 116.3) * np.random.random((number_of_pcs, 1)) + 116.3
    print(pcs_lat)
    print(pcs_lon)
    print(region_id(pcs_lat, pcs_lon))
