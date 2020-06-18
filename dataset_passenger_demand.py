'''
@Author: Ye Han
@Date: 2019-11-15 10:25:01
@LastEditTime: 2020-06-06 16:42:12
@LastEditors: Ye Han
@Description:
@FilePath: \data_analysis\Spatio_temporal_load.py
@Copyright (c) 2019 - Ye Han
@All rights reserved.
'''

import csv
import os

import pandas as pd
from more_itertools import chunked

# # Import Data.
# for date in ["20121106"]:
#     path = 'D:\\Data\\Taxi\\' + date
#     files = os.listdir(path)
#    , = []
#    , = []
#    , = []
#    , = []
#     for file in files:
#         print(file)
#         taxi_data = pd.read_csv(
#             path + '\\' + file, header=None, na_values='-32768', names=['state', "lng", 'lat'], engine='c', usecols=[2, 4, 5], error_bad_lines=False, encoding='gb2312')
#     # The region division. Get one region for our analysis.
#         taxi_data_3 = taxi_data[(taxi_data['lng'] > 116.35) & (taxi_data['lng'] < 116.4) & (
#             taxi_data['lat'] > 39.95) & (taxi_data['lat'] < 40)]
#         taxi_data_2 = taxi_data[(taxi_data['lng'] > 116.35) & (taxi_data['lng'] < 116.4) & (
#             taxi_data['lat'] < 39.95) & (taxi_data['lat'] > 39.9)]
#         taxi_data_1 = taxi_data[(taxi_data['lng'] < 116.35) & (taxi_data['lng'] > 116.3) & (
#             taxi_data['lat'] < 39.95) & (taxi_data['lat'] > 39.9)]
#         taxi_data_4 = taxi_data[(taxi_data['lng'] < 116.35) & (taxi_data['lng'] > 116.3) & (
#             taxi_data['lat'] > 39.95) & (taxi_data['lat'] < 40)]
#     # Get the passenger load of the chosen region.
#         taxi_data_1 = taxi_data_1[taxi_data_1['state'] == 0]
#         taxi_data_2 = taxi_data_2[taxi_data_2['state'] == 0]
#         taxi_data_3 = taxi_data_3[taxi_data_3['state'] == 0]
#         taxi_data_4 = taxi_data_4[taxi_data_4['state'] == 0]
#        ,.append(taxi_data_1.shape[0])
#        ,.append(taxi_data_2.shape[0])
#        ,.append(taxi_data_3.shape[0])
#        ,.append(taxi_data_4.shape[0])
#         pass
#     print(date)
#     print(,',,)
#     print(,',,)
#     print(,',,)
#     print(,',,)
num =[[373, 344, 366, 360, 345, 347, 339, 378, 405, 413, 397, 416, 367, 385, 385, 366, 356, 392, 409, 390, 408, 408, 386, 357, 358, 321, 331, 326, 310, 332, 329, 343, 334, 382, 392, 403, 411, 385, 400, 384, 391, 402, 443, 426, 409, 387, 383, 371, 335, 318, 303, 334, 317, 299, 281, 282, 293, 289, 300, 290, 295, 324, 339, 331, 314, 296, 284, 293, 290, 304, 302, 332, 340, 333, 351, 343, 321, 319, 324, 327, 340, 315, 314, 292, 300, 281, 285, 262, 297, 271, 259, 270, 267, 274, 295, 277, 277, 294, 269, 286, 301, 289, 288, 293, 302, 296, 281, 274, 275, 274, 292, 302, 304, 301, 307, 258, 260, 274, 288, 266, 279, 279, 294, 328, 311, 314, 290, 301, 306, 301, 322, 312, 306, 296, 300, 270, 266, 260, 250, 263, 270, 274, 281, 269, 278, 297, 280, 276, 288, 283, 274, 268, 263, 273, 251, 258, 249, 247, 246, 245, 245, 244, 277, 268, 261, 254, 252, 245, 236, 226, 232, 224, 242, 259, 250, 241, 265, 253, 253, 278, 266, 275, 291, 297, 282, 293, 295, 254, 274, 273, 270, 277, 286, 265, 279, 262, 275, 284, 288, 272, 286, 265, 244, 252, 248, 254, 256, 228, 232, 250, 236, 241, 243, 240, 268, 254, 269, 266, 248, 255, 229, 240, 247, 256, 254, 266, 272, 259, 244, 249, 242, 222, 249, 262, 259, 274, 276, 273, 262, 270, 232, 261, 279, 280, 272, 265, 252, 255, 223, 214, 220, 243, 229, 234, 220, 218, 220, 209, 214, 200, 209, 186, 204, 176, 205, 223, 213, 193, 201, 177, 203, 190, 207, 211, 210, 220, 218, 211, 208, 192, 186, 220, 201, 186, 192, 201, 202, 200, 199, 193, 196, 214, 210, 206, 200, 216, 217, 229, 234, 235, 250, 236, 211, 207, 196, 202, 210, 195, 186, 201, 219, 248, 221, 218, 200, 232, 235, 255, 257, 247, 267, 276, 286, 272, 274, 257, 251, 267, 285, 271, 269, 275, 293, 280, 268, 261, 264, 272, 310, 305, 307, 316, 305, 328, 379, 343, 311, 307, 323, 291, 273, 303, 283, 281, 239, 232, 238, 253, 264, 268, 238, 241, 253, 276, 317, 302, 297, 312, 287, 249, 250, 239, 276, 244, 249, 279, 264, 244, 236, 259, 252, 251, 273, 291, 277, 269, 284, 308, 286, 310, 321, 302, 290, 283, 242, 257, 275, 253, 292, 291, 305, 325, 280, 286, 306, 299, 291, 282, 315, 294, 299, 268, 262, 268, 256, 295, 323, 313, 304, 285, 287, 285, 267, 271, 257, 251, 240, 224, 226, 231, 229, 228, 201, 205, 225, 205, 186, 228, 224, 213, 239, 235, 256, 262, 311, 287, 292, 258, 250, 248, 231, 228, 235, 217, 226, 249, 231, 269, 249, 261, 249, 254, 259, 244, 243, 276, 248, 242, 256, 253, 248, 249, 232, 229, 252, 254, 237, 226, 233, 263, 234, 244, 270, 239, 247, 269, 249, 246, 250, 280, 255, 285, 294, 291, 304, 289, 261, 271, 267, 218, 242, 222, 214, 230, 228, 232, 252, 261, 245, 281, 274, 268, 285, 309, 308, 335, 342, 344, 317, 330, 294, 303, 311, 310, 348, 377, 386, 390, 376, 368, 356, 347, 340, 363, 368, 367, 365, 352, 417, 433, 409, 415, 421, 363, 391, 391, 375, 321, 343, 378, 371, 381, 360, 331, 329, 307, 334, 322, 314, 324, 326, 324, 294, 351, 377, 390, 381, 391, 373, 426, 405, 452, 422, 408, 401, 403, 404, 377, 398, 382, 377, 366, 323, 339, 366, 370, 369, 385, 365, 336, 339, 345, 369, 366, 345, 371, 383, 385, 396, 414, 430, 431, 431, 400, 381, 411, 398, 393, 422, 402, 409, 406, 438, 467, 450, 494, 438, 446, 466, 492, 469, 452, 474, 446, 480, 445, 431, 414, 412, 383, 409, 416, 408, 410, 427, 456, 466, 485, 486, 528, 462, 435, 480, 467, 480, 497, 489, 512, 500, 510, 517, 529, 487, 499, 493, 481, 468, 486, 492, 548, 555, 529, 522, 500, 499, 533, 538, 487, 518, 510, 510, 512, 519, 492, 523, 525, 550, 512, 545, 543, 537, 571, 553, 548, 546, 555, 531, 547, 549, 572, 516, 522, 502, 583, 599, 581, 587, 597, 569, 587, 598, 581, 598, 531, 552, 544, 515, 528, 547, 575, 568, 584, 596, 604, 588, 598, 578, 601, 578, 591, 580, 573, 581, 586, 597, 624, 601, 610, 628, 589, 592, 596, 599, 576, 621, 628, 623, 657, 649, 659, 677, 704, 652, 653, 633, 654, 632, 622, 621, 606, 622, 636, 606, 624, 637, 666, 611, 641, 620, 600, 642, 597, 629, 665, 674, 649, 691, 697, 683, 699, 697, 670, 673, 650, 667, 670, 650, 645, 652, 641, 631, 621, 628, 654, 642, 614, 641, 613, 632, 665, 648, 636, 589, 630, 624, 616, 602, 620, 612, 585, 585, 568, 557, 559, 574, 548, 549, 572, 597, 603, 611, 599, 580, 556, 585, 569, 570, 523, 508, 491, 479, 493, 461, 460, 488, 480, 489, 483, 473, 464, 457, 486, 474, 473, 462, 437, 489, 503, 518, 540, 521, 523, 480, 455, 460, 492, 476, 474, 466, 449, 461, 471, 443, 459, 488, 506, 533, 488, 485, 495, 451, 492, 510, 537, 558, 526, 483, 485, 494, 500, 493, 481, 446, 459, 452, 450, 430, 421, 427, 423, 430, 445, 430, 433, 434, 400, 405, 444, 470, 484, 493, 489, 503, 473, 488, 479, 474, 475, 477, 468, 460, 467, 459, 448, 422, 391, 445, 467, 469, 467, 485, 480, 504, 514, 494, 469, 483, 472, 421, 420, 436, 421, 436, 443, 473, 490, 479, 465, 486, 490, 471, 450, 423, 447, 461, 458, 466, 443, 440, 416, 451, 487, 495, 514, 479, 455, 453, 428, 452, 449, 423, 467, 445, 406, 408, 417, 404, 398, 400, 385, 391, 445, 430, 390, 397, 417, 430, 427, 423, 401, 428, 485, 447, 452, 415, 454, 463, 490, 454, 483, 471, 492, 461, 482, 474, 480, 488, 483, 497, 480, 455, 431, 441, 413, 410, 429, 447, 447, 420, 412, 438, 428, 421, 416, 407, 378, 372, 396, 375, 386, 391, 403, 408, 377, 398, 396, 396, 412, 406, 429, 403, 350, 360, 359, 341, 346, 369, 382, 359, 373, 382, 410, 440, 408, 431, 442, 450, 426, 408, 370, 358, 357, 388, 378, 381, 371, 396, 423, 410, 393, 406, 399, 415, 426, 412, 394, 435, 416, 434, 416, 456, 453, 427, 396, 472, 483, 482, 450, 455, 446, 470, 442, 465, 458, 446, 456, 441, 411, 413, 366, 353, 416, 377, 384, 396, 402, 366, 374, 393, 363, 369, 365, 354, 342, 357, 345, 319, 336, 328, 327, 321, 321, 315, 346, 307, 311, 333, 319, 300, 326, 325, 351, 325, 336, 309, 319, 343, 279, 260, 242, 261, 245, 266, 289, 265, 263, 298, 265, 302, 289, 302, 298, 300, 285, 294, 292, 287, 302, 293, 292, 261, 241, 262, 258, 268, 272, 264, 248, 253, 246, 254, 245, 276, 268, 243, 229, 267, 223, 231, 221, 272, 269, 289, 295, 306, 272, 278, 280, 262, 281, 259, 289, 268, 287, 285, 288, 311, 290, 313, 305, 297, 293, 282, 285, 282, 281, 300, 304, 315, 327, 297, 299, 273, 315, 301, 291, 288, 323, 339, 330, 316, 338, 342, 366, 327, 304, 361, 365, 361, 316, 313, 304, 265, 304, 320, 357, 397, 368, 360, 325, 373, 394, 407, 413, 403, 374, 376, 394, 387, 355, 335, 320, 335, 351, 327, 334, 284, 322, 318, 338, 342, 387, 396, 404, 334, 326, 344, 374, 411, 399, 386, 402, 366, 389, 386, 376, 372, 346, 359, 348, 363, 375, 364, 369, 389, 400, 396, 383, 336, 324, 319, 313, 338, 385, 415, 398, 389, 419, 434, 422, 434, 420, 384, 386, 405, 400, 404, 394, 360, 416, 399, 421, 394, 381, 383, 422, 405, 383, 371, 385, 454, 447, 452, 441, 436, 466, 446, 400, 387, 404, 390, 361, 352, 370, 403, 378, 402, 415, 428, 410, 419, 430, 471, 482, 479, 460, 453, 467, 411, 422, 417, 432, 419, 413, 416, 405, 412, 448, 412, 429, 425, 395, 403, 411, 392, 425, 399, 362, 412, 410, 397, 416, 411, 428, 405, 401, 413, 411, 403, 402, 384, 407, 365, 376, 365, 363, 380, 397, 409, 407, 396, 389, 386, 393, 413, 374, 349, 316, 326, 360, 374, 348, 302, 321, 325, 295, 297, 319, 311, 295, 310, 279, 304, 303, 298, 332, 317, 309, 310, 282, 252, 257, 270, 273, 243, 252, 240, 269, 259, 249, 266, 263, 267, 294, 286, 293, 300, 273, 263, 278, 265, 262, 271, 277, 279, 241, 297, 269, 276, 258, 280, 312, 332, 327, 334, 331, 340, 280, 258, 265, 268, 257, 259, 304, 254, 250, 231, 246, 242, 254, 257, 256, 287, 251, 277, 250, 224, 243, 212, 231, 235, 225, 231, 239, 247, 273, 267, 277, 279, 300, 346, 328, 356, 388, 330, 358, 324, 352, 314, 276, 282, 296, 304, 287, 292, 312, 258, 237, 255, 277, 247, 267, 288, 314, 390, 377, 374, 366, 379, 372, 370, 353, 379, 360, 343, 375, 363, 356, 343, 331, 330, 325, 351, 361, 361, 336, 319, 338, 348, 334, 344, 339, 340, 342, 368, 338, 340, 343, 357, 365, 394, 398, 381, 365, 397, 399, 402, 441, 468, 452, 446, 463, 434, 449, 436, 424, 386, 398, 413, 406, 411, 373, 387, 344, 338, 356, 328, 345, 349, 373, 359, 368, 381, 391, 431, 402, 423, 444, 435, 422, 387, 376, 398, 390, 444, 405, 385, 379, 396, 406, 418, 441, 424, 400, 393, 366, 374, 356, 387, 373, 399, 388, 387, 381, 383, 360, 372, 405], [353, 348, 322, 314, 317, 294, 319, 307, 308, 291, 276, 282, 271, 252, 260, 263, 273, 273, 263, 281, 272, 273, 290, 298, 312, 318, 310, 310, 274, 274, 324, 325, 335, 305, 321, 339, 318, 297, 302, 317, 302, 264, 259, 258, 244, 273, 284, 305, 312, 308, 310, 312, 295, 296, 262, 265, 258, 230, 255, 260, 255, 259, 252, 257, 262, 260, 270, 268, 279, 284, 288, 277, 274, 277, 288, 296, 320, 321, 324, 268, 264, 266, 275, 284, 304, 314, 319, 291, 298, 301, 302, 293, 296, 290, 296, 271, 244, 261, 288, 293, 284, 266, 266, 264, 264, 254, 271, 284, 292, 285, 276, 274, 219, 215, 227, 238, 248, 232, 253, 255, 243, 233, 234, 223, 239, 256, 284, 290, 281, 271, 260, 253, 291, 290, 254, 247, 268, 273, 291, 305, 280, 282, 302, 312, 312, 294, 273, 281, 276, 275, 279, 276, 248, 229, 238, 238, 252, 249, 237, 246, 234, 244, 236, 222, 227, 225, 217, 222, 212, 202, 200, 211, 205, 216, 222, 235, 239, 261, 258, 236, 251, 234, 233, 229, 219, 217, 224, 236, 242, 253, 238, 252, 282, 262, 235, 239, 234, 238, 240, 238, 236, 230, 226, 228, 234, 229, 237, 231, 232, 228, 238, 256, 223, 256, 234, 228, 234, 243, 224, 250, 235, 249, 236, 246, 237, 262, 256, 248, 242, 243, 242, 242, 219, 235, 244, 236, 225, 221, 221, 228, 219, 213, 221, 215, 222, 222, 214, 247, 254, 224, 230, 239, 209, 214, 222, 218, 210, 219, 240, 219, 221, 228, 233, 202, 201, 199, 195, 199, 192, 186, 213, 216, 212, 210, 217, 213, 194, 187, 203, 219, 204, 209, 199, 208, 218, 223, 232, 261, 238, 227, 229, 216, 214, 190, 187, 197, 186, 192, 180, 194, 190, 197, 194, 196, 198, 191, 194, 214, 221, 219, 217, 200, 198, 199, 205, 191, 207, 196, 198, 217, 214, 216, 206, 196, 222, 211, 226, 211, 232, 222, 207, 196, 196, 201, 210, 239, 239, 225, 202, 214, 236, 241, 246, 228, 227, 198, 209, 226, 219, 219, 226, 213, 214, 206, 219, 216, 220, 222, 205, 205, 222, 207, 201, 201, 211, 239, 237, 235, 234, 233, 230, 240, 250, 250, 240, 242, 236, 235, 255, 233, 260, 264, 242, 267, 241, 245, 238, 237, 241, 226, 235, 236, 219, 224, 230, 236, 212, 215, 238, 242, 244, 229, 242, 237, 245, 218, 222, 234, 239, 245, 267, 248, 238, 286, 313, 274, 271, 276, 277, 260, 255, 251, 222, 202, 223, 236, 237, 245, 207, 222, 204, 226, 255, 247, 293, 280, 242, 248, 249, 275, 302, 269, 260, 243, 220, 240, 237, 236, 224, 229, 226, 244, 238, 221, 231, 222, 214, 225, 221, 218, 238, 230, 230, 232, 238, 234, 245, 243, 245, 261, 262, 246, 258, 250, 261, 254, 247, 259, 231, 247, 252, 243, 236, 278, 271, 280, 302, 288, 280, 290, 286, 276, 255, 284, 272, 265, 294, 246, 235, 245, 214, 234, 236, 225, 199, 222, 243, 236, 244, 237, 230, 256, 267, 247, 269, 255, 236, 252, 259, 255, 251, 241, 240, 239, 237, 201, 220, 227, 226, 231, 243, 254, 252, 273, 255, 254, 264, 287, 283, 313, 312, 297, 294, 335, 358, 338, 360, 341, 322, 334, 358, 343, 345, 337, 306, 314, 316, 336, 324, 345, 320, 327, 300, 318, 301, 324, 334, 332, 336, 318, 312, 343, 351, 344, 355, 355, 363, 382, 414, 396, 394, 409, 402, 370, 412, 403, 422, 385, 454, 693, 524, 495, 509, 588, 510, 370, 348, 370, 364, 358, 370, 357, 350, 342, 329, 359, 346, 352, 380, 437, 394, 458, 432, 408, 402, 379, 362, 392, 372, 360, 391, 365, 360, 393, 380, 352, 347, 347, 353, 382, 354, 345, 357, 336, 346, 329, 347, 360, 353, 391, 388, 371, 360, 338, 352, 351, 354, 352, 453, 447, 450, 392, 392, 393, 416, 394, 401, 387, 400, 370, 382, 352, 385, 346, 360, 382, 385, 358, 416, 425, 462, 420, 443, 419, 444, 445, 459, 470, 444, 428, 438, 447, 452, 450, 454, 421, 447, 444, 414, 397, 413, 427, 422, 435, 419, 430, 422, 438, 422, 416, 400, 434, 404, 400, 418, 426, 400, 401, 415, 424, 417, 440, 444, 435, 425, 449, 454, 453, 461, 433, 376, 394, 415, 396, 402, 387, 429, 455, 435, 403, 405, 456, 443, 463, 418, 397, 399, 414, 433, 418, 417, 409, 406, 427, 436, 406, 423, 425, 443, 436, 439, 432, 431, 427, 455, 450, 484, 476, 505, 504, 481, 508, 516, 509, 486, 458, 470, 449, 446, 426, 435, 434, 417, 449, 409, 394, 405, 378, 407, 405, 414, 370, 398, 391, 407, 438, 441, 421, 411, 429, 440, 468, 468, 455, 434, 414, 424, 424, 427, 419, 410, 430, 410, 449, 437, 438, 435, 418, 398, 390, 408, 390, 402, 432, 401, 391, 402, 372, 381, 362, 385, 374, 383, 382, 393, 364, 375, 386, 395, 397, 383, 381, 340, 335, 325, 310, 312, 314, 323, 309, 345, 349, 363, 378, 375, 365, 370, 338, 383, 404, 404, 397, 431, 465, 454, 431, 416, 391, 400, 390, 372, 349, 353, 325, 297, 289, 302, 300, 284, 283, 294, 308, 336, 369, 339, 340, 329, 336, 336, 339, 326, 311, 314, 314, 288, 299, 314, 309, 337, 322, 313, 352, 376, 355, 334, 349, 349, 352, 359, 378, 336, 341, 326, 362, 332, 361, 360, 340, 327, 326, 303, 320, 322, 315, 316, 329, 322, 337, 353, 352, 357, 404, 356, 351, 384, 357, 372, 357, 343, 325, 315, 285, 281, 297, 331, 378, 392, 375, 379, 362, 361, 386, 349, 338, 310, 333, 318, 347, 345, 367, 356, 339, 342, 363, 362, 363, 348, 355, 306, 326, 340, 358, 367, 360, 371, 370, 390, 373, 367, 396, 370, 351, 353, 367, 340, 355, 322, 325, 299, 314, 341, 353, 349, 344, 335, 346, 323, 317, 287, 296, 315, 324, 315, 297, 290, 299, 321, 321, 291, 311, 288, 294, 280, 266, 279, 303, 251, 253, 237, 280, 277, 252, 253, 264, 265, 251, 254, 246, 278, 266, 259, 249, 246, 237, 253, 258, 269, 263, 270, 272, 243, 261, 291, 293, 302, 289, 292, 292, 287, 285, 284, 282, 308, 311, 315, 314, 305, 287, 299, 299, 305, 289, 263, 289, 273, 284, 265, 275, 270, 265, 264, 292, 292, 289, 283, 273, 299, 283, 261, 270, 288, 266, 288, 298, 330, 325, 335, 306, 309, 337, 375, 378, 359, 366, 335, 314, 299, 316, 300, 306, 332, 310, 327, 317, 311, 286, 271, 319, 348, 339, 335, 351, 328, 328, 343, 349, 317, 327, 336, 327, 313, 301, 296, 321, 289, 298, 280, 307, 324, 297, 286, 262, 287, 279, 282, 297, 279, 280, 292, 317, 307, 294, 323, 317, 327, 279, 295, 324, 305, 311, 284, 280, 276, 283, 311, 306, 287, 276, 271, 286, 274, 255, 261, 263, 282, 278, 288, 261, 286, 276, 250, 255, 291, 269, 264, 253, 277, 268, 264, 283, 297, 291, 287, 292, 286, 272, 267, 275, 251, 281, 288, 273, 278, 300, 273, 294, 280, 258, 241, 273, 280, 288, 254, 253, 251, 265, 257, 230, 249, 247, 242, 238, 223, 243, 242, 265, 267, 249, 267, 248, 264, 233, 229, 242, 219, 231, 226, 228, 259, 242, 269, 241, 227, 233, 244, 254, 269, 239, 257, 248, 266, 263, 238, 224, 243, 254, 266, 272, 264, 255, 249, 239, 258, 207, 253, 244, 227, 244, 285, 279, 276, 282, 292, 281, 286, 294, 302, 292, 299, 303, 299, 288, 272, 279, 277, 266, 271, 278, 281, 259, 287, 274, 279, 305, 291, 285, 263, 285, 291, 303, 277, 311, 299, 317, 292, 256, 241, 227, 249, 238, 228, 235, 224, 266, 294, 324, 334, 309, 339, 324, 310, 316, 321, 310, 316, 283, 297, 305, 341, 358, 337, 345, 342, 310, 300, 293, 298, 285, 279, 265, 291, 297, 326, 362, 333, 324, 299, 315, 304, 273, 297, 289, 310, 283, 290, 288, 310, 282, 305, 322, 313, 304, 317, 313, 298, 301, 312, 322, 305, 340, 343, 326, 307, 298, 309, 341, 308, 308, 332, 341, 307, 292, 300, 297, 270, 231, 242, 264, 273, 303, 331, 349, 312, 319, 309, 308, 292, 282, 259, 254, 245, 270, 285, 255, 263, 277, 289, 248, 259, 237, 252, 264, 275, 269, 271, 259, 279, 250, 246, 234, 229, 215, 238, 243, 238, 243, 213, 240, 232, 244, 262, 257, 242, 237, 220, 212, 214, 222, 216, 213, 186, 200, 214, 178, 205, 223, 213, 204, 215, 240, 235, 230, 205, 183, 208, 188, 199, 211, 222, 196, 187, 192, 194, 212, 202, 201, 208, 220, 221, 205, 204, 190, 195, 230, 260, 217, 232, 253, 224, 233, 257, 261, 264, 272, 273, 278, 245, 228, 246, 268, 246, 237, 240, 253, 255, 278, 272, 280, 278, 283, 274, 307, 295, 270, 258, 254, 258, 299, 310, 283, 285, 294, 294, 317, 314, 294, 282, 261, 263, 294, 289, 295, 279, 278, 281, 313, 307, 286, 285, 301, 296, 288, 279, 261, 269, 313, 300, 288, 288, 263, 263, 248, 264, 254, 270, 288, 311, 324, 326, 314, 305, 280, 289, 270, 281, 271, 288, 310, 327, 327, 335, 304, 305, 319, 285, 322, 302, 330, 315, 317, 352, 346, 368, 394, 388, 360, 372, 376, 387, 375, 347, 327, 358, 371, 347, 318, 340, 324, 323, 344, 335, 323, 324, 316, 330, 292, 324, 316, 303, 282, 286, 289, 301, 304, 316, 313, 335, 334, 367, 355, 348, 359, 368, 371, 389, 367, 364, 345], [516, 502, 521, 499, 521, 553, 560, 572, 538, 535, 521, 506, 494, 496, 515, 524, 535, 528, 475, 495, 523, 525, 527, 499, 460, 486, 478, 459, 514, 497, 485, 458, 467, 470, 449, 427, 460, 449, 453, 486, 482, 521, 525, 538, 541, 538, 495, 491, 522, 496, 462, 467, 429, 462, 451, 463, 466, 479, 478, 480, 475, 481, 522, 516, 515, 497, 489, 487, 521, 536, 502, 519, 526, 493, 504, 494, 496, 485, 486, 479, 478, 478, 448, 443, 453, 443, 436, 439, 447, 441, 442, 439, 390, 421, 422, 450, 448, 466, 442, 425, 451, 469, 433, 499, 491, 476, 509, 500, 519, 503, 470, 485, 487, 505, 489, 481, 474, 478, 473, 488, 507, 522, 537, 538, 496, 490, 520, 497, 521, 522, 502, 503, 504, 506, 493, 527, 526, 534, 530, 528, 553, 527, 518, 554, 538, 518, 543, 524, 525, 511, 501, 516, 516, 505, 532, 510, 530, 492, 509, 523, 527, 507, 521, 517, 488, 517, 524, 534, 526, 524, 508, 518, 511, 507, 513, 502, 500, 490, 494, 489, 493, 502, 528, 493, 507, 530, 515, 545, 534, 542, 558, 510, 526, 538, 494, 505, 498, 510, 489, 491, 494, 518, 507, 488, 515, 508, 487, 488, 512, 517, 511, 500, 527, 509, 526, 480, 486, 500, 503, 501, 484, 493, 515, 522, 495, 500, 493, 487, 484, 476, 478, 464, 464, 458, 471, 445, 504, 490, 471, 507, 500, 482, 486, 479, 514, 502, 501, 514, 498, 486, 462, 504, 507, 485, 490, 459, 492, 468, 485, 487, 464, 460, 470, 495, 516, 490, 478, 479, 485, 484, 453, 445, 464, 447, 461, 442, 467, 449, 449, 458, 441, 442, 435, 430, 442, 437, 442, 458, 440, 418, 412, 397, 386, 400, 394, 393, 387, 382, 356, 378, 393, 386, 402, 400, 390, 398, 375, 381, 389, 350, 345, 341, 339, 345, 373, 374, 377, 377, 382, 370, 360, 376, 381, 376, 389, 377, 348, 370, 343, 299, 323, 322, 348, 360, 342, 338, 337, 338, 364, 335, 334, 324, 339, 327, 309, 332, 317, 334, 370, 338, 355, 363, 342, 347, 345, 327, 322, 314, 295, 300, 299, 279, 332, 336, 335, 326, 319, 320, 294, 321, 318, 304, 304, 297, 285, 282, 301, 278, 279, 310, 302, 290, 324, 332, 323, 345, 339, 333, 324, 324, 332, 332, 338, 340, 321, 304, 318, 316, 316, 308, 318, 320, 305, 308, 313, 332, 349, 341, 334, 350, 321, 336, 346, 333, 333, 311, 313, 312, 311, 308, 327, 303, 309, 313, 328, 303, 323, 310, 324, 345, 338, 357, 375, 364, 322, 327, 345, 356, 332, 331, 309, 353, 343, 356, 346, 355, 385, 382, 384, 369, 387, 369, 389, 376, 369, 370, 389, 374, 371, 373, 383, 394, 402, 407, 379, 357, 346, 350, 356, 367, 363, 373, 367, 352, 335, 366, 364, 382, 390, 388, 362, 342, 391, 368, 374, 378, 376, 376, 426, 390, 384, 366, 368, 371, 381, 354, 377, 391, 411, 389, 393, 403, 435, 450, 430, 434, 456, 467, 431, 447, 413, 440, 460, 491, 473, 490, 488, 472, 474, 499, 507, 492, 469, 439, 440, 436, 453, 426, 454, 447, 460, 442, 445, 406, 445, 409, 417, 422, 430, 397, 378, 401, 387, 388, 390, 392, 388, 437, 412, 393, 371, 421, 379, 378, 385, 394, 381, 374, 373, 358, 406, 389, 394, 393, 404, 368, 390, 366, 389, 378, 397, 432, 406, 412, 408, 397, 363, 364, 383, 401, 380, 389, 381, 423, 393, 400, 412, 386, 415, 412, 418, 426, 412, 394, 429, 426, 446, 445, 434, 423, 407, 429, 439, 415, 446, 463, 475, 488, 488, 508, 482, 479, 496, 476, 492, 488, 498, 516, 492, 483, 513, 528, 544, 552, 512, 598, 598, 574, 572, 589, 580, 577, 560, 559, 568, 581, 559, 588, 602, 584, 591, 600, 611, 591, 604, 568, 572, 571, 582, 570, 595, 585, 611, 602, 596, 600, 627, 642, 619, 651, 662, 655, 628, 640, 627, 614, 643, 638, 658, 681, 652, 651, 634, 662, 661, 676, 656, 679, 709, 677, 697, 665, 676, 678, 681, 678, 713, 696, 740, 727, 696, 709, 681, 662, 687, 683, 687, 638, 627, 628, 624, 553, 582, 575, 602, 675, 638, 696, 688, 734, 679, 712, 665, 662, 672, 678, 658, 653, 625, 610, 644, 680, 647, 639, 607, 592, 647, 645, 635, 606, 632, 645, 667, 637, 684, 620, 646, 649, 674, 648, 659, 655, 648, 646, 669, 671, 662, 653, 636, 650, 673, 680, 682, 677, 683, 652, 635, 668, 609, 653, 654, 605, 646, 636, 656, 640, 663, 668, 703, 678, 657, 632, 624, 655, 663, 670, 664, 677, 636, 656, 653, 629, 609, 639, 629, 642, 649, 634, 572, 603, 593, 593, 599, 624, 639, 650, 605, 577, 582, 589, 594, 550, 607, 568, 573, 559, 618, 612, 580, 551, 512, 535, 537, 545, 568, 593, 574, 585, 556, 577, 593, 585, 543, 563, 539, 507, 528, 517, 554, 559, 518, 552, 586, 601, 632, 661, 635, 587, 559, 545, 500, 554, 561, 547, 543, 522, 532, 563, 557, 529, 532, 533, 537, 545, 538, 556, 554, 540, 497, 523, 528, 524, 503, 500, 550, 548, 553, 530, 505, 513, 473, 488, 457, 471, 482, 475, 509, 525, 496, 471, 481, 496, 483, 503, 484, 487, 492, 517, 509, 468, 490, 483, 505, 511, 493, 514, 511, 548, 556, 561, 539, 534, 519, 549, 521, 573, 563, 619, 584, 589, 545, 531, 524, 498, 527, 527, 546, 518, 526, 531, 515, 522, 550, 501, 521, 504, 548, 525, 560, 501, 516, 522, 534, 490, 495, 523, 567, 585, 555, 564, 547, 526, 542, 533, 514, 511, 519, 481, 503, 442, 477, 494, 477, 491, 516, 531, 526, 512, 522, 508, 524, 520, 496, 527, 529, 525, 508, 553, 559, 560, 550, 536, 546, 529, 534, 540, 562, 544, 522, 536, 512, 542, 530, 502, 465, 496, 485, 508, 530, 523, 514, 546, 528, 571, 539, 564, 577, 578, 561, 562, 546, 537, 551, 522, 570, 551, 564, 551, 506, 499, 519, 499, 510, 504, 478, 508, 497, 491, 489, 464, 478, 479, 478, 454, 473, 478, 461, 454, 437, 469, 489, 470, 438, 441, 463, 453, 474, 467, 453, 451, 442, 441, 458, 427, 437, 396, 438, 406, 447, 456, 459, 435, 467, 426, 437, 440, 431, 425, 449, 424, 414, 413, 465, 437, 456, 426, 435, 448, 432, 416, 442, 452, 460, 457, 478, 459, 465, 493, 491, 465, 453, 451, 463, 467, 485, 480, 481, 453, 467, 456, 432, 438, 454, 458, 446, 459, 448, 457, 452, 425, 417, 426, 466, 430, 433, 460, 426, 408, 393, 421, 389, 383, 362, 357, 384, 370, 357, 363, 347, 378, 360, 396, 395, 407, 422, 433, 442, 435, 430, 429, 432, 415, 432, 435, 393, 428, 403, 421, 423, 409, 436, 440, 453, 484, 457, 435, 423, 402, 426, 424, 421, 411, 400, 408, 384, 412, 366, 399, 392, 371, 356, 397, 368, 361, 365, 358, 402, 381, 387, 374, 377, 359, 387, 391, 402, 389, 390, 388, 389, 371, 399, 377, 398, 353, 377, 366, 377, 425, 414, 419, 428, 417, 440, 428, 417, 414, 375, 384, 351, 384, 367, 383, 382, 393, 342, 366, 389, 403, 399, 359, 375, 418, 411, 404, 364, 377, 352, 419, 412, 399, 416, 404, 402, 401, 393, 419, 429, 414, 394, 395, 382, 407, 401, 405, 437, 469, 460, 444, 449, 460, 469, 463, 478, 451, 384, 434, 455, 469, 498, 507, 480, 508, 487, 508, 483, 548, 535, 520, 504, 526, 553, 553, 574, 544, 580, 558, 556, 586, 528, 560, 561, 596, 543, 556, 533, 523, 529, 534, 544, 525, 544, 526, 521, 579, 543, 522, 521, 493, 528, 528, 491, 493, 537, 474, 476, 463, 475, 495, 500, 511, 494, 452, 465, 474, 500, 478, 522, 491, 481, 486, 531, 466, 532, 528, 528, 492, 515, 528, 482, 499, 488, 501, 486, 513, 520, 491, 485, 477, 504, 506, 502, 544, 495, 484, 517, 485, 496, 485, 491, 446, 455, 439, 461, 478, 467, 436, 465, 438, 452, 426, 427, 439, 419, 438, 431, 430, 421, 420, 440, 401, 418, 387, 391, 367, 377, 405, 409, 400, 370, 391, 406, 380, 388, 333, 350, 374, 387, 390, 404, 412, 418, 450, 425, 402, 373, 380, 369, 372, 374, 389, 410, 392, 380, 399, 379, 406, 400, 356, 349, 360, 350, 350, 379, 361, 330, 296, 347, 328, 325, 306, 295, 277, 308, 339, 356, 366, 342, 354, 342, 352, 335, 367, 350, 371, 318, 344, 319, 333, 341, 367, 373, 345, 312, 348, 387, 414, 410, 376, 386, 379, 378, 359, 399, 379, 418, 408, 432, 423, 411, 415, 417, 401, 392, 426, 421, 399, 371, 338, 332, 331, 331, 336, 340, 329, 310, 332, 353, 329, 330, 320, 340, 314, 356, 329, 376, 345, 337, 336, 347, 356, 405, 389, 389, 378, 390, 420, 387, 375, 361, 394, 358, 362, 360, 331, 326, 338, 337, 365, 346, 368, 365, 313, 304, 345, 293, 329, 346, 363, 400, 403, 398, 436, 392, 437, 410, 398, 390, 382, 352, 394, 407, 387, 414, 379, 394, 410, 402, 375, 350, 397, 405, 413, 403, 376, 398, 377, 408, 409, 386, 360, 347, 325, 305, 355, 334, 371, 400, 339, 349, 356, 351, 357, 375, 360, 371, 378, 388, 407, 415, 394, 386, 432, 372, 382, 384, 374, 353, 337, 331, 341, 363, 361, 328, 346, 376, 394, 394, 376, 381, 389, 381, 382, 371, 367, 374, 360, 347, 360, 379, 378, 383, 396, 405, 392, 380, 433, 429, 438], [363, 356, 361, 362, 331, 300, 285, 306, 285, 323, 335, 353, 360, 283, 302, 319, 347, 332, 333, 329, 285, 273, 279, 293, 305, 322, 338, 377, 369, 369, 378, 357, 352, 310, 296, 280, 265, 283, 283, 276, 276, 280, 292, 294, 317, 308, 289, 293, 317, 289, 277, 275, 269, 251, 266, 227, 230, 251, 248, 245, 250, 251, 252, 257, 257, 261, 275, 268, 248, 237, 241, 227, 220, 230, 240, 263, 266, 252, 250, 240, 239, 238, 240, 246, 231, 240, 241, 269, 263, 287, 297, 293, 259, 278, 284, 268, 275, 277, 306, 320, 315, 315, 300, 303, 299, 298, 318, 292, 289, 280, 309, 293, 282, 293, 296, 301, 280, 248, 256, 248, 253, 265, 246, 232, 247, 270, 269, 253, 261, 258, 264, 262, 283, 286, 289, 283, 272, 268, 261, 260, 254, 234, 240, 226, 231, 233, 262, 259, 247, 248, 253, 249, 246, 254, 244, 265, 248, 252, 266, 272, 326, 327, 324, 321, 316, 320, 342, 333, 312, 330, 324, 318, 314, 304, 293, 275, 287, 292, 286, 282, 282, 274, 274, 257, 261, 261, 272, 265, 283, 257, 274, 281, 271, 291, 299, 308, 305, 308, 281, 282, 287, 297, 284, 274, 287, 261, 279, 292, 296, 288, 277, 275, 274, 289, 292, 290, 279, 267, 251, 261, 258, 260, 267, 256, 253, 265, 258, 264, 258, 276, 279, 298, 293, 290, 314, 278, 291, 286, 290, 293, 302, 312, 323, 303, 284, 279, 287, 268, 291, 295, 268, 286, 285, 286, 273, 291, 279, 275, 269, 252, 253, 252, 256, 248, 243, 277, 264, 280, 283, 272, 259, 279, 263, 260, 261, 255, 266, 246, 257, 263, 251, 243, 252, 256, 275, 268, 259, 249, 242, 239, 263, 277, 291, 308, 306, 269, 253, 244, 231, 227, 229, 218, 227, 244, 235, 259, 275, 279, 248, 219, 214, 198, 175, 172, 181, 157, 172, 171, 181, 182, 188, 156, 160, 154, 151, 144, 141, 154, 143, 138, 142, 137, 133, 139, 151, 145, 165, 159, 131, 126, 160, 140, 152, 150, 138, 140, 137, 143, 132, 135, 148, 140, 157, 167, 175, 180, 179, 172, 190, 193, 180, 176, 189, 204, 197, 188, 179, 171, 185, 196, 191, 184, 196, 195, 219, 200, 200, 207, 237, 190, 189, 185, 190, 185, 164, 183, 179, 198, 204, 214, 209, 205, 191, 211, 195, 196, 211, 176, 173, 166, 182, 189, 184, 196, 182, 181, 186, 205, 176, 188, 178, 177, 174, 185, 193, 180, 189, 188, 180, 163, 184, 195, 160, 175, 176, 174, 165, 176, 168, 168, 152, 171, 171, 188, 210, 211, 207, 202, 183, 216, 239, 218, 203, 185, 197, 187, 174, 189, 195, 221, 204, 203, 203, 230, 234, 216, 198, 237, 242, 232, 259, 249, 251, 235, 249, 245, 251, 243, 243, 208, 206, 195, 202, 193, 202, 178, 175, 203, 210, 208, 213, 239, 232, 207, 220, 233, 224, 230, 243, 264, 271, 292, 279, 269, 281, 277, 274, 281, 299, 343, 282, 330, 309, 288, 289, 277, 307, 322, 283, 294, 272, 284, 270, 276, 268, 275, 270, 254, 266, 291, 273, 309, 304, 340, 323, 289, 294, 303, 316, 313, 312, 312, 306, 300, 281, 269, 294, 274, 270, 294, 303, 297, 283, 279, 293, 372, 327, 300, 332, 333, 322, 308, 347, 336, 358, 336, 334, 388, 385, 359, 371, 404, 463, 460, 459, 449, 427, 443, 434, 466, 434, 433, 443, 441, 443, 445, 448, 479, 448, 439, 489, 451, 427, 424, 395, 404, 451, 467, 491, 489, 488, 503, 496, 514, 482, 488, 468, 493, 495, 476, 504, 511, 510, 499, 480, 484, 492, 541, 546, 478, 503, 492, 503, 499, 493, 532, 558, 533, 559, 540, 562, 586, 554, 587, 558, 536, 539, 523, 540, 546, 574, 598, 578, 630, 637, 608, 672, 669, 663, 634, 663, 641, 649, 616, 596, 605, 606, 589, 621, 618, 655, 671, 639, 614, 616, 610, 639, 571, 580, 580, 562, 614, 674, 613, 590, 601, 626, 614, 561, 555, 563, 567, 608, 650, 661, 640, 620, 597, 613, 625, 680, 640, 614, 617, 616, 584, 588, 586, 572, 593, 566, 561, 573, 573, 564, 582, 610, 596, 588, 601, 598, 609, 639, 607, 539, 517, 503, 556, 529, 558, 534, 567, 546, 581, 550, 608, 618, 639, 589, 597, 621, 631, 604, 595, 568, 564, 568, 558, 568, 583, 573, 574, 549, 558, 523, 556, 561, 577, 561, 557, 550, 513, 540, 590, 582, 595, 608, 599, 601, 627, 613, 657, 640, 636, 639, 646, 692, 696, 688, 705, 715, 674, 682, 643, 627, 607, 615, 609, 610, 628, 606, 606, 621, 619, 601, 605, 586, 619, 632, 630, 605, 628, 640, 628, 605, 623, 641, 628, 612, 552, 568, 532, 590, 622, 598, 638, 667, 648, 642, 601, 617, 611, 569, 546, 570, 590, 577, 548, 555, 554, 518, 545, 544, 544, 531, 569, 550, 588, 596, 593, 594, 569, 502, 499, 470, 447, 464, 436, 464, 499, 533, 527, 508, 491, 461, 491, 497, 480, 470, 456, 407, 417, 415, 433, 410, 444, 438, 409, 427, 432, 477, 477, 456, 463, 471, 474, 434, 444, 445, 453, 448, 427, 427, 451, 460, 497, 465, 465, 473, 483, 468, 489, 470, 432, 428, 430, 414, 433, 458, 480, 471, 465, 461, 476, 457, 445, 453, 462, 472, 483, 448, 454, 454, 502, 451, 464, 417, 394, 406, 426, 434, 393, 420, 397, 382, 390, 407, 389, 396, 439, 442, 474, 465, 463, 475, 484, 467, 475, 500, 536, 583, 539, 558, 561, 533, 552, 545, 553, 566, 545, 548, 524, 538, 542, 553, 535, 516, 521, 529, 532, 555, 578, 556, 547, 552, 533, 587, 573, 564, 581, 545, 511, 532, 510, 525, 501, 493, 505, 556, 556, 556, 498, 515, 487, 510, 499, 497, 525, 522, 533, 521, 517, 503, 538, 527, 496, 502, 492, 492, 484, 455, 461, 477, 443, 457, 447, 419, 445, 408, 425, 430, 402, 436, 429, 436, 451, 416, 405, 458, 436, 416, 498, 498, 524, 501, 513, 516, 474, 523, 523, 493, 504, 509, 481, 471, 491, 488, 502, 491, 497, 534, 482, 537, 528, 539, 509, 552, 556, 540, 546, 558, 517, 496, 505, 488, 490, 441, 426, 436, 419, 444, 406, 402, 396, 392, 396, 429, 419, 442, 409, 373, 370, 375, 378, 414, 399, 449, 459, 467, 480, 452, 436, 423, 459, 435, 470, 416, 435, 409, 427, 429, 420, 385, 418, 440, 422, 399, 373, 398, 403, 403, 406, 396, 420, 406, 389, 385, 388, 373, 368, 391, 382, 374, 377, 381, 368, 373, 421, 397, 409, 364, 339, 353, 367, 381, 373, 366, 377, 344, 346, 356, 376, 338, 344, 336, 347, 325, 325, 311, 330, 339, 313, 342, 324, 349, 328, 352, 363, 354, 358, 385, 381, 366, 350, 352, 360, 320, 313, 313, 313, 313, 293, 308, 313, 309, 311, 312, 356, 350, 351, 330, 328, 364, 358, 343, 361, 348, 359, 323, 303, 332, 332, 351, 360, 387, 358, 342, 339, 398, 354, 342, 340, 348, 350, 369, 368, 335, 345, 355, 341, 377, 392, 371, 375, 372, 387, 411, 395, 391, 363, 378, 369, 366, 374, 379, 355, 389, 385, 402, 417, 408, 394, 377, 379, 392, 361, 375, 402, 399, 372, 418, 411, 431, 393, 383, 368, 425, 382, 401, 409, 403, 429, 378, 377, 407, 388, 385, 375, 389, 406, 391, 394, 392, 384, 376, 409, 411, 416, 416, 417, 439, 406, 406, 448, 376, 391, 366, 361, 402, 410, 448, 446, 438, 453, 430, 472, 464, 506, 481, 490, 496, 529, 503, 504, 479, 492, 452, 438, 445, 455, 494, 474, 452, 446, 462, 449, 472, 459, 483, 486, 470, 470, 442, 469, 475, 469, 434, 455, 463, 509, 530, 490, 445, 451, 475, 471, 499, 481, 493, 496, 505, 504, 492, 480, 472, 466, 455, 474, 471, 457, 479, 470, 467, 459, 435, 435, 426, 443, 422, 426, 423, 455, 421, 470, 438, 460, 456, 476, 459, 478, 460, 456, 463, 453, 431, 441, 409, 372, 369, 346, 360, 351, 373, 426, 383, 389, 390, 393, 370, 383, 369, 367, 408, 392, 387, 391, 379, 364, 316, 360, 387, 377, 382, 377, 440, 396, 399, 344, 369, 408, 407, 383, 382, 379, 378, 357, 373, 363, 347, 325, 304, 310, 295, 293, 297, 319, 336, 333, 308, 292, 306, 272, 260, 246, 275, 272, 273, 254, 261, 223, 227, 246, 245, 279, 315, 325, 318, 308, 318, 298, 260, 297, 283, 319, 262, 255, 250, 240, 260, 236, 247, 222, 241, 235, 282, 274, 269, 259, 288, 278, 285, 245, 257, 267, 242, 232, 227, 220, 223, 241, 239, 279, 299, 309, 295, 340, 337, 330, 315, 345, 325, 314, 299, 267, 271, 287, 277, 263, 275, 266, 269, 279, 283, 276, 297, 292, 293, 250, 274, 259, 277, 257, 246, 261, 259, 243, 272, 292, 300, 334, 323, 327, 317, 298, 335, 306, 337, 356, 335, 304, 319, 322, 312, 327, 364, 382, 354, 374, 376, 345, 339, 357, 364, 347, 326, 323, 357, 349, 375, 390, 347, 352, 339, 345, 361, 388, 397, 386, 392, 393, 389, 366, 355, 382, 404, 409, 425, 454, 433, 414, 389, 394, 374, 389, 361, 377, 396, 391, 392, 411, 411, 458, 465, 413, 395, 393, 414, 383, 358, 376, 358, 370, 329, 374, 406, 386, 399, 398, 414, 420, 420, 449, 409, 470, 432, 441, 445, 477, 472, 483, 514, 471, 457, 473, 446, 432, 421, 446, 441, 446, 414, 398, 372, 376, 385, 401, 380, 358, 328, 344, 342, 328, 329, 358, 342, 348, 382, 405]]

for i in range(4):
    print(len(num[i]))
    print([sum(x) for x in chunked(num[i][:1584], 22)])
