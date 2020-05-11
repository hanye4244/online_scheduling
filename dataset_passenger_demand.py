'''
@Author: Ye Han
@Date: 2019-11-15 10:25:01
@LastEditTime: 2020-05-11 12:22:29
@LastEditors: Ye Han
@Description:
@FilePath: \data_analysis\Spatio_temporal_load.py
@Copyright (c) 2019 - Ye Han
@All rights reserved.
'''

import os

import pandas as pd
# Import Data.
# path = 'C:\\Users\\hanye\\Documents\\20121101'
# files = os.listdir(path)
# num_1 = []
# num_2 = []
# num_3 = []
# num_4 = []
# for file in files:
#     taxi_data = pd.read_csv(
#         path + '\\' + file, names=['state', "lng", 'lat'], engine='python', usecols=[2, 4, 5])
#     # The region division. Get one region for our analysis.
#     taxi_data_3 = taxi_data[(taxi_data['lng'] > 116.35) & (taxi_data['lng'] < 116.4) & (
#         taxi_data['lat'] > 39.95) & (taxi_data['lat'] < 40)]
#     taxi_data_2 = taxi_data[(taxi_data['lng'] > 116.35) & (taxi_data['lng'] < 116.4) & (
#         taxi_data['lat'] < 39.95) & (taxi_data['lat'] > 39.9)]
#     taxi_data_1 = taxi_data[(taxi_data['lng'] < 116.35) & (taxi_data['lng'] > 116.3) & (
#         taxi_data['lat'] < 39.95) & (taxi_data['lat'] > 39.9)]
#     taxi_data_4 = taxi_data[(taxi_data['lng'] < 116.35) & (taxi_data['lng'] > 116.3) & (
#         taxi_data['lat'] > 39.95) & (taxi_data['lat'] < 40)]
#     # Get the passenger load of the chosen region.
#     taxi_data_1 = taxi_data_1[taxi_data_1['state'] == 0]
#     taxi_data_2 = taxi_data_2[taxi_data_2['state'] == 0]
#     taxi_data_3 = taxi_data_3[taxi_data_3['state'] == 0]
#     taxi_data_4 = taxi_data_4[taxi_data_4['state'] == 0]
#     num_1.append(taxi_data_1.shape[0])
#     num_2.append(taxi_data_2.shape[0])
#     num_3.append(taxi_data_3.shape[0])
#     num_4.append(taxi_data_4.shape[0])
#     pass
# print('num_1', num_1)
# print('num_2', num_2)
# print('num_3', num_3)
# print('num_4', num_4)
from more_itertools import chunked

num_2 = [399, 385, 386, 386, 393, 394, 381, 354, 361, 351, 358, 326, 337, 369, 390, 385, 394, 405, 415, 394, 361, 367, 347, 355, 344, 336, 363, 364, 348, 360, 354, 384, 366, 338, 297, 325, 354, 397, 370, 365, 343, 369, 383, 372, 366, 357, 335, 333, 322, 338, 347, 357, 333, 354, 395, 348, 337, 328, 330, 337, 346, 332, 328, 335, 350, 326, 316, 344, 343, 362, 328, 352, 322, 340, 336, 332, 338, 319, 312, 295, 305, 318, 327, 333, 338, 342, 361, 336, 347, 323, 309, 318, 317, 343, 357, 352, 379, 379, 372, 344, 341, 316, 311, 330, 357, 358, 354, 353, 338, 339, 332, 324, 340, 303, 303, 313, 299, 296, 289, 296, 287, 311, 303, 292, 287, 271, 278, 306, 310, 315, 335, 350, 335, 304, 299, 305, 308, 295, 313, 340, 330, 308, 311, 318, 285, 255, 260, 249, 260, 276, 280, 276, 273, 259, 265, 290, 297, 257, 284, 284, 290, 272, 290, 322, 308, 292, 283, 299, 314, 318, 314, 309, 315, 299, 303, 301, 311, 306, 306, 299, 308, 293, 289, 292, 287, 308, 285, 307, 314, 294, 292, 311, 326, 333, 325, 337, 313, 306, 308, 318, 292, 323, 309, 316, 296, 296, 310, 290, 296, 299, 275, 272, 296, 305, 306, 287, 291, 323, 334, 337, 298, 309, 300, 308, 297, 275, 278, 287, 297, 303, 297, 311, 320, 308, 318, 327, 332, 326, 344, 356, 339, 321, 335, 297, 285, 279, 284, 272, 282, 282, 297, 298, 306, 292, 287, 298, 281, 282, 279, 266, 290, 256, 267, 282, 279, 260, 280, 276, 280, 290, 285, 282, 278, 269, 265, 278, 276, 302, 289, 314, 307, 294, 285, 301, 297, 287, 276, 289, 284, 301, 309, 311, 312, 315, 320, 308, 301, 316, 295, 281, 302, 295, 287, 290, 279, 269, 266, 254, 259, 262, 250, 237, 239, 225, 224, 225, 229, 229, 241, 222, 248, 226, 249, 257, 242, 257, 257, 251, 243, 225, 204, 206, 197, 202, 187, 191, 193, 188, 184, 191, 190, 164, 143, 152, 166, 157, 166, 170, 208, 197, 220, 216, 205, 193, 196, 192, 173, 138, 143, 151, 144, 151, 161, 155, 150, 147, 147, 156, 151, 148, 166, 185, 188, 182, 150, 142, 152, 175, 186, 197, 190, 176, 191, 210, 192, 174, 182, 168, 163, 175, 184, 207, 213, 199, 196, 201, 190, 195, 194, 184, 188, 189, 177, 196, 188, 180, 189, 205, 209, 245, 218, 226, 220, 204, 222, 197, 201, 184, 199, 191, 188, 198, 181, 192, 175, 179, 165, 192, 207, 212, 214, 206, 205, 195, 217, 221, 213, 216, 175, 211, 186, 177, 174, 166, 183, 191, 205, 197, 204, 182, 197, 199, 201, 204, 234, 227, 254, 240, 247, 251, 253, 249, 224, 218, 225, 217, 207, 227, 237, 226, 201, 198, 205, 208, 243, 212, 217, 231, 226, 197, 190, 229, 237, 238, 242, 233, 258, 251, 246, 277, 264, 248, 244, 213, 190, 185, 237, 223, 231, 231, 274, 272, 295, 291, 288, 280, 286, 286, 303, 303, 316, 338, 347, 337, 306, 335, 314, 327, 324, 317, 297, 315, 305, 293, 329, 350, 349, 341, 371, 327, 323, 304, 302, 279, 271, 260, 293, 316, 279, 305, 262, 245, 260, 274, 302, 287, 308, 309, 355, 303, 317, 332, 356, 353, 376, 401, 404, 386, 398, 364, 369, 376, 333, 363, 375, 375, 348, 348, 375, 392, 385, 401, 399, 387, 407, 411, 431, 419, 414, 453, 476, 491, 475, 494, 497, 472, 499, 506, 486, 487, 495, 457, 451, 491, 507, 502, 508, 517, 502, 561, 517, 505, 504, 526, 509, 458, 466, 512, 499, 499, 479, 453, 456, 453, 429, 459, 453, 494, 478, 525, 490, 477, 487, 525, 545, 516, 531, 529, 520, 486, 514, 501, 518, 508, 530, 572, 590, 571, 584, 535, 537, 500, 522, 511, 546, 553, 604, 589, 585, 603, 662, 599, 614, 661, 662, 710, 697, 703, 687, 676, 659, 646, 672, 644, 638, 636, 626, 595, 609, 615, 665, 607, 637, 648, 657, 712, 744, 699, 680, 697, 665, 665, 693, 699, 657, 632, 628, 642, 647, 649, 641, 628, 644, 672, 674, 664, 642, 660, 655, 663, 687, 653, 660, 622, 641, 630, 677, 650, 683, 675, 659, 701, 718, 695, 689, 696, 651, 664, 692, 676, 629, 648, 674, 688, 705, 700, 647, 615, 630, 630, 574, 572, 618, 621, 616, 669, 665, 693, 679, 698, 703, 694, 709, 676, 679, 715, 697, 743, 729, 756, 724, 706, 720, 736, 748, 756, 779, 778, 759, 788, 764, 751, 753, 776, 810, 803, 812, 830, 830, 779, 788, 742, 781, 794, 793, 798, 774, 736, 703, 699, 743, 740, 751, 720, 700, 702, 689, 682, 722, 710, 714, 721, 735, 780, 771, 768, 748, 695, 713, 720, 767, 734, 745, 718, 718, 716, 689, 689, 712, 687, 660, 641, 649, 651, 699, 671, 701, 688, 678, 667, 688, 673, 685, 680, 656, 630, 600, 637, 634, 645, 656, 665, 696, 678, 677, 646, 622, 604, 590, 612, 590, 566, 582, 580, 557, 552, 571, 579, 561, 544, 525, 509, 524, 525, 515, 573, 570, 567, 569, 572, 571, 575, 566, 539, 541, 517, 504, 475, 483, 478, 475, 487, 497, 480, 508, 511, 474, 498, 495, 462, 437, 450, 423, 420, 442, 487, 456, 451, 475, 469, 492, 519, 543, 518, 503, 502, 489, 520, 509, 504, 507, 506, 539, 535, 516, 479, 471, 469, 437, 439, 452, 443, 446, 477, 465, 498, 505, 500, 486, 467, 488, 481, 476, 474, 441, 450, 464, 445, 488, 493, 476, 448, 478, 476, 510, 510, 513, 488, 495, 478, 474, 490, 428, 447, 422, 431, 428, 438, 437, 445, 427, 412, 443, 446, 475, 508, 496, 528, 543, 568, 572, 529, 500, 521, 526, 500, 450, 490, 531, 495, 450, 432, 468, 442, 470, 444, 472, 491, 492, 491, 521, 489, 496, 552, 534, 545, 523, 502, 478, 489, 484, 473, 497, 517, 474, 481, 470, 483, 499, 494, 485, 515, 535, 489, 501, 474, 485, 504, 514, 489, 481, 474, 468, 500, 526, 487, 495, 494, 486, 503, 476, 426, 458, 456, 466, 415, 437, 457, 455, 421, 467, 502, 515, 512, 513, 484, 488, 502, 500, 505, 487, 498, 507, 493, 492, 505, 476, 471, 483, 460, 426, 415, 409, 440, 440, 443, 514, 424, 424, 418, 393, 362, 370, 360, 355, 352, 379, 347, 345, 357, 336, 348, 339, 337, 345, 351, 355, 365, 352, 364, 360, 358, 416, 405, 436, 419, 400, 403, 415, 408, 409, 389, 404, 422, 385, 373, 379, 362, 383, 373, 360, 362, 377, 364, 377, 351, 344, 334, 340, 327, 367, 355, 388, 383, 415, 396, 348, 346, 356, 320, 337, 326, 317, 340, 338, 357, 330, 356, 364, 350, 369, 351, 354, 377, 375, 370, 365, 365, 346, 368, 340, 350, 349, 357, 360, 357, 353, 334, 342, 335, 377, 374, 361, 362, 341, 354, 366, 350, 341, 329, 323, 347, 328, 322, 295, 286, 271, 296, 321, 342, 324, 329, 293, 306, 331, 332, 332, 341, 347, 333, 348, 348, 340, 349, 339, 373, 343, 328, 321, 329, 312, 290, 306, 289, 306, 315, 322, 321, 327, 286, 282, 323, 321, 315, 323, 344, 345, 317, 325, 274, 332, 311, 312, 334, 329, 314, 316, 290, 281, 296, 283, 302, 298, 315, 303, 292, 274, 306, 326, 330, 306, 297, 323, 308, 318, 300, 300, 320, 305, 335, 364, 335, 344, 358, 351, 337, 319, 330, 331, 362, 334, 346, 342, 389, 405, 387, 379, 347, 355, 333, 388, 358, 365, 363, 363, 365, 375, 357, 408, 381, 373, 383, 400, 392, 402, 427, 418, 403, 404, 405, 399, 388, 369, 391, 417, 394, 425, 414, 403, 434, 435, 445, 467, 490, 465, 450, 442, 463, 417, 423, 490, 478, 504, 469, 447, 455, 462, 458, 495, 489, 477, 501, 546, 552, 543, 498, 472, 477, 446, 475, 418, 418, 446, 438, 453, 452, 458, 445, 471, 480, 491, 472, 475, 493, 550, 472, 428, 409, 398, 378, 365, 364, 387, 415, 414, 377, 404, 423, 378, 392, 371, 407, 407, 385, 389, 400, 407, 394, 395, 387, 403, 398, 399, 396, 397, 392, 396, 374, 369, 357, 376, 358, 350, 371, 344, 356, 331, 389, 398, 410, 427, 375, 379, 423, 452, 436, 398, 399, 421, 418, 392, 376, 380, 341, 374, 364, 366, 357, 306, 306, 300, 303, 347, 330, 358, 340, 356, 360, 340, 393, 373, 342, 345, 343, 355, 346, 331, 332, 345, 328, 328, 318, 303, 311, 291, 285, 270, 254, 239, 248, 252, 252, 299, 288, 283, 272, 252, 267, 227, 230, 219, 231, 249, 270, 270, 247, 255, 264, 286, 266, 282, 293, 313, 307, 297, 305, 291, 269, 243, 290, 249, 239, 268, 304, 322, 305, 290, 336, 348, 359, 356, 298, 321, 280, 278, 302, 307, 305, 279, 308, 271, 268, 282, 293, 299, 307, 326, 318, 333, 303, 321, 309, 306, 306, 299, 276, 290, 274, 258, 296, 262, 264, 264, 282, 288, 353, 367, 358, 306, 307, 340, 350, 358, 362, 372, 354, 369, 325, 337, 314, 301, 307, 312, 327, 306, 303, 294, 312, 320, 305, 327, 303, 302, 331, 316, 340, 368, 395, 417, 413, 362, 357, 348, 325, 326, 328, 368, 357, 347, 364, 383, 369, 397, 399, 388, 372, 348, 343, 318, 318, 347, 358, 373, 366, 341, 370, 347, 361, 359, 311, 307, 325, 365, 366, 387, 409, 412, 431, 450, 478, 503, 468, 509, 463, 471, 425, 456, 446, 479, 486, 495, 473, 460, 473, 431, 413, 406, 411, 427, 459, 441, 444, 398, 393, 394, 359, 379, 314, 330, 336, 368, 364, 391, 375, 400, 390, 364, 352, 370, 374, 375, 370, 387, 367, 343, 343, 346, 354, 372]
# print(len(num_1))
print([sum(x) for x in chunked(num_2[:1584], 22)])
