# coding=utf-8
'''
@Author: Ye Han
@Date: 2020-06-10 17:25:34
@LastEditTime: 2020-06-11 12:34:32
@LastEditors: Ye Han
@Description: 
@Copyright (c) 2020 - Ye Han
All rights reserved.
'''
import matplotlib.pyplot as plt

algorithm = [7, 11, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0, 0, 2, 3, 4, 4, 5, 6, 11, 15, 19, 18, 19, 25, 27, 31, 39, 42, 44, 45, 47, 49, 52, 55, 59, 63, 67, 70, 71, 70, 69, 65, 63, 59, 52, 47, 43, 34, 34, 35, 34, 32, 32, 29, 26, 19, 14, 12, 14, 11, 12, 14, 11, 10, 3, 3, 2, 2, 2, 1, 2, 2, 2, 1, 0, 1, 1, 3, 4, 4, 5, 2, 2, 2, 2, 3, 4, 4, 4, 8, 9, 9, 11, 11, 15, 19, 24, 28, 31, 35, 39, 41, 41, 45, 48, 52, 57, 60, 62, 60, 63, 66, 64, 64, 59, 52, 50, 49, 47, 43, 44, 43, 40, 39, 36, 32, 26, 23, 20, 20, 21, 22, 23, 26, 21, 20, 19, 19, 16, 11, 9, 7, 4, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 4, 5, 4, 4, 6, 7, 7, 8, 9, 11, 11, 11, 6, 5, 6, 5, 5, 5, 5, 6, 6, 4, 3, 4, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1,
             0, 0, 0, 1, 1, 2, 3, 3, 4, 4, 4, 3, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 5, 6, 5, 7, 7, 8, 11, 17, 20, 24, 29, 34, 33, 38, 41, 48, 51, 57, 65, 72, 77, 81, 81, 82, 84, 83, 82, 81, 80, 76, 72, 71, 70, 68, 67, 67, 67, 65, 67, 69, 70, 68, 70, 69, 70, 73, 76, 76, 72, 71, 68, 69, 60, 51, 49, 43, 43, 38, 34, 29, 25, 20, 13, 12, 12, 9, 10, 9, 9, 7, 8, 11, 10, 8, 9, 11, 11, 15, 12, 13, 21, 25, 30, 32, 35, 35, 39, 41, 43, 45, 48, 50, 56, 61, 62, 67, 71, 74, 74, 69, 68, 66, 63, 59, 58, 57, 56, 54, 52, 51, 48, 43, 43, 40, 38, 35, 36, 38, 40, 43, 45, 48, 49, 51, 53, 50, 48, 42, 40, 32, 26, 22, 11, 7, 3, 2, 2, 2, 2, 1, 1, 1, 3, 5, 9, 13, 14, 16, 22, 24, 28, 30, 28, 32, 39, 45, 47, 50, 51, 55, 58, 58, 58, 60, 64, 67, 68, 71, 77, 82, 81, 84, 82, 81, 82, 83, 80, 81, 82, 79, 78, 73, 71, 68, 64, 58, 54, 55, 52, 52, 50, 50, 50, 51, 53, 55, 54, 55, 58.]
near = [3.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 4.0, 6.0, 7.0, 7.0, 5.0, 0.0, 2.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 7.0, 8.0, 12.0, 10.0, 13.0, 22.0, 34.0, 45.0, 54.0, 62.0, 69.0, 76.0, 81.0, 87.0, 92.0, 96.0, 98.0, 93.0, 97.0, 93.0, 92.0, 89.0, 83.0, 80.0, 77.0, 72.0, 72.0, 67.0, 60.0, 57.0, 59.0, 64.0, 69.0, 73.0, 77.0, 80.0, 81.0, 82.0, 79.0, 77.0, 72.0, 71.0, 66.0, 67.0, 64.0, 61.0, 59.0, 54.0, 45.0, 38.0, 30.0, 31.0, 28.0, 27.0, 25.0, 25.0, 26.0, 26.0, 27.0, 26.0, 26.0, 24.0, 21.0, 12.0, 5.0, 2.0, 3.0, 4.0, 5.0, 4.0, 5.0, 6.0, 7.0, 9.0, 14.0, 21.0, 31.0, 40.0, 50.0, 59.0, 64.0, 70.0, 75.0, 78.0, 80.0, 76.0, 73.0, 71.0, 68.0, 66.0, 67.0, 64.0, 60.0, 57.0, 50.0, 50.0, 46.0, 42.0, 43.0, 45.0, 49.0, 54.0, 59.0, 62.0, 66.0, 69.0, 67.0, 66.0, 63.0, 57.0, 55.0, 53.0, 48.0, 48.0, 47.0, 45.0, 38.0, 33.0, 31.0, 29.0, 26.0, 26.0, 26.0, 27.0, 28.0, 30.0, 29.0, 30.0, 28.0, 24.0, 12.0, 1.0, 2.0, 1.0, 1.0, 3.0, 3.0, 4.0, 4.0, 4.0, 5.0, 7.0, 10.0, 12.0, 16.0, 21.0, 24.0, 27.0, 30.0, 32.0, 33.0, 31.0, 28.0, 24.0, 26.0, 25.0, 20.0, 22.0, 18.0, 9.0, 7.0, 3.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0,
        1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 3.0, 3.0, 5.0, 5.0, 5.0, 8.0, 14.0, 22.0, 29.0, 36.0, 43.0, 51.0, 58.0, 63.0, 64.0, 63.0, 61.0, 62.0, 58.0, 57.0, 58.0, 57.0, 58.0, 59.0, 62.0, 64.0, 61.0, 59.0, 59.0, 61.0, 64.0, 67.0, 71.0, 75.0, 76.0, 76.0, 76.0, 74.0, 72.0, 63.0, 60.0, 50.0, 46.0, 40.0, 37.0, 35.0, 32.0, 30.0, 27.0, 25.0, 25.0, 28.0, 31.0, 34.0, 35.0, 36.0, 37.0, 36.0, 34.0, 29.0, 25.0, 16.0, 9.0, 1.0, 1.0, 3.0, 2.0, 2.0, 2.0, 1.0, 2.0, 1.0, 2.0, 3.0, 6.0, 10.0, 14.0, 19.0, 24.0, 30.0, 37.0, 40.0, 44.0, 45.0, 50.0, 54.0, 55.0, 56.0, 58.0, 60.0, 63.0, 64.0, 65.0, 63.0, 62.0, 66.0, 71.0, 76.0, 82.0, 86.0, 89.0, 91.0, 90.0, 89.0, 84.0, 80.0, 81.0, 79.0, 74.0, 70.0, 69.0, 66.0, 64.0, 59.0, 58.0, 57.0, 53.0, 52.0, 54.0, 58.0, 63.0, 68.0, 72.0, 74.0, 76.0, 75.0, 74.0, 71.0, 65.0, 61.0, 52.0, 45.0, 41.0, 34.0, 24.0, 14.0, 6.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 4.0, 6.0, 9.0, 14.0, 18.0, 21.0, 24.0, 25.0, 27.0, 28.0, 30.0, 33.0, 36.0, 43.0, 50.0, 54.0, 55.0, 57.0, 59.0, 61.0, 62.0, 68.0, 74.0, 81.0, 86.0, 90.0, 91.0, 94.0, 93.0, 90.0, 85.0, 84.0, 79.0, 79.0, 79.0, 75.0, 71.0, 71.0, 72.0, 71.0, 69.0, 67.0, 65.0, 68.0, 72.0, 75.0, 78.0, 80.0, 82.0, 85.0, 85.0, 82.0, 74.0, 71.0, 68.0, 66.0, 60.0, 59.0]
request = [3.0, 4.0, 3.0, 3.0, 3.0, 3.0, 3.0, 4.0, 5.0, 6.0, 7.0, 6.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 0.0, 0.0, 2.0, 3.0, 4.0, 4.0, 5.0, 7.0, 11.0, 14.0, 19.0, 20.0, 29.0, 35.0, 39.0, 47.0, 50.0, 58.0, 59.0, 65.0, 70.0, 75.0, 80.0, 85.0, 86.0, 89.0, 87.0, 89.0, 86.0, 83.0, 81.0, 79.0, 77.0, 73.0, 70.0, 65.0, 66.0, 65.0, 65.0, 64.0, 67.0, 66.0, 68.0, 66.0, 62.0, 60.0, 59.0, 55.0, 55.0, 51.0, 50.0, 46.0, 49.0, 44.0, 43.0, 42.0, 41.0, 39.0, 38.0, 37.0, 37.0, 39.0, 39.0, 35.0, 30.0, 25.0, 18.0, 13.0, 12.0, 10.0, 9.0, 8.0, 3.0, 1.0, 2.0, 3.0, 4.0, 4.0, 4.0, 5.0, 9.0, 11.0, 15.0, 20.0, 25.0, 31.0, 38.0, 42.0, 46.0, 51.0, 53.0, 56.0, 60.0, 65.0, 64.0, 65.0, 63.0, 60.0, 61.0, 60.0, 60.0, 62.0, 62.0, 60.0, 60.0, 59.0, 55.0, 54.0, 55.0, 51.0, 51.0, 50.0, 52.0, 54.0, 56.0, 55.0, 57.0, 54.0, 55.0, 53.0, 51.0, 48.0, 48.0, 48.0, 44.0, 39.0, 38.0, 37.0, 38.0, 31.0, 30.0, 29.0, 27.0, 27.0, 27.0, 25.0, 24.0, 22.0, 16.0, 10.0, 6.0, 3.0, 1.0, 1.0, 3.0, 4.0, 4.0, 4.0, 4.0, 5.0, 7.0, 10.0, 13.0, 18.0, 18.0, 16.0, 14.0, 11.0, 8.0, 5.0, 5.0, 4.0, 6.0, 4.0, 4.0, 5.0, 5.0, 4.0, 6.0, 8.0, 8.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0,
           0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 2.0, 1.0, 2.0, 2.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 3.0, 3.0, 5.0, 5.0, 5.0, 7.0, 8.0, 13.0, 16.0, 19.0, 17.0, 21.0, 22.0, 21.0, 24.0, 28.0, 33.0, 36.0, 40.0, 42.0, 48.0, 54.0, 60.0, 65.0, 68.0, 70.0, 72.0, 72.0, 70.0, 68.0, 68.0, 65.0, 65.0, 65.0, 64.0, 61.0, 63.0, 67.0, 68.0, 69.0, 66.0, 65.0, 65.0, 62.0, 62.0, 59.0, 56.0, 54.0, 55.0, 52.0, 55.0, 56.0, 58.0, 56.0, 54.0, 52.0, 49.0, 47.0, 44.0, 39.0, 35.0, 28.0, 24.0, 18.0, 13.0, 12.0, 9.0, 5.0, 2.0, 1.0, 2.0, 1.0, 2.0, 3.0, 5.0, 4.0, 6.0, 6.0, 7.0, 10.0, 13.0, 14.0, 19.0, 27.0, 33.0, 40.0, 44.0, 48.0, 54.0, 59.0, 63.0, 62.0, 66.0, 66.0, 68.0, 71.0, 71.0, 72.0, 74.0, 72.0, 68.0, 65.0, 60.0, 58.0, 59.0, 58.0, 57.0, 56.0, 58.0, 59.0, 58.0, 56.0, 56.0, 53.0, 48.0, 48.0, 39.0, 36.0, 36.0, 36.0, 40.0, 43.0, 42.0, 42.0, 38.0, 37.0, 37.0, 34.0, 34.0, 30.0, 28.0, 29.0, 26.0, 23.0, 18.0, 16.0, 9.0, 6.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 3.0, 3.0, 5.0, 7.0, 10.0, 12.0, 17.0, 21.0, 26.0, 28.0, 35.0, 42.0, 51.0, 61.0, 71.0, 73.0, 79.0, 83.0, 82.0, 84.0, 85.0, 86.0, 89.0, 93.0, 97.0, 98.0, 100.0, 100.0, 98.0, 100.0, 97.0, 92.0, 89.0, 89.0, 86.0, 84.0, 86.0, 86.0, 93.0, 94.0, 97.0, 97.0, 95.0, 97.0, 94.0, 92.0, 88.0, 88.0, 88.0, 86.0, 85.0, 86.0, 85.0, 83.0, 85.0, 88.0, 87.0]
t = range(504)
plt.plot(t, request, color='red', linestyle='-')
plt.plot(t, near, color='blue', linestyle=':')
plt.plot(t, algorithm, color='green', linestyle='-.')
plt.show()
