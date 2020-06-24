# , coding=utf-8
'''
@Author:, Ye, Han
@Date:, 2020-04-15, 11:52:03
@LastEditTime: 2020-06-24 11:33:29
@LastEditors: Ye Han
@Description:
@FilePath:, \Online_Scheduling\python_tast.py
@Copyright, (c), 2020, -, Ye, Han
All, rights, reserved.
'''

import matplotlib.pyplot as plt
import numpy as np

a = np.array([913.873269519843, 401.1608824117176, 1072.393010393371, 981.1420283007803, 881.8821888209794, 1448.3607470101554, 1068.2992163468566, 1064.147074298607, 1094.363554997985, 1112.1643348902126, 1076.2067308184614, 1356.5899089645566, 1255.9869011745961, 1390.5707047814337, 1819.5966700090012, 1648.1822913547746, 863.1758217200037, 1018.1154105882749, 1318.1490795445616, 1118.4292347931873, 1086.8318910447192, 1303.8653692536461, 756.8187965631474, 1268.4421536389534, 870.4999108599911, 1088.102088062655, 823.9629896492809, 870.3665202347152, 673.854959932031, 867.1610625611361, 1209.6230747484992, 1151.0735854780628, 1198.4009340795626, 1273.2652045257146, 1360.8855926697515, 1052.7295459276615, 1195.4942304382982, 1791.756773652423, 1363.4846406607755, 919.723035855782, 1286.1737377629843, 815.5922339332542, 715.8029381237102, 1245.3248969713252, 1517.9252650202252, 948.6211203221872, 977.9690107158367, 1163.0217276941933, 1034.8701728198673, 1276.534304073308, 1167.0279782365333, 863.1667714568607, 1300.4971509548664, 841.8464656913458, 1095.5468720315719, 939.1195632675814, 1010.3717997248797, 838.8863354605235, 1157.0267243900023, 1241.8913937335428, 795.1742470458714, 875.5478048963341, 1540.4992455201561, 1434.181576094682, 1359.032242333529, 847.6002944029198, 1269.0077399717522, 1130.3800282014272, 959.7105157425972, 1281.5292285489616, 1378.6895360990238, 684.9964594938474, 1195.561202129545, 849.6579999999999, 987.3162213887408, 639.6643089222536, 897.9723511510874, 1147.7312850191474, 1102.5774826965235, 1298.0869234196507, 1289.4241793460026, 1492.4430452614345, 1150.1377110201065, 962.0740203775058, 317.82703670815016, 1207.56016781432, 1489.5019023573846, 1249.658, 1288.7795893673938, 828.7172023016199, 1283.5978126612142, 1088.344570544317, 1044.7282994395875, 149.65800000000002, 1015.4220398064526, 1014.4064624849115, 1028.3141944757726, 849.253, 1011.425954897532, 1049.253, 964.2877894555749, 1155.2814014442356, 991.752700782419, 921.447045871361, 1547.51693071778, 1245.0683965184967, 1280.3677040227133, 954.6323627808608, 1212.61898111278, 1111.9900055655628, 1427.8802631470858, 1405.0740558783505, 919.033251092847, 1145.4539882473928, 798.812, 1427.6980574413612, 736.1486144901417, 1529.6899879440293, 1159.6594121105534, 1159.54783018392, 1222.5820608549473, 904.9065749075108, 1225.311408218918, 760.9092338824586, 799.253, 1026.7474707186805, 1324.1521054533455, 877.3714158587148, 1222.8694515439568, 852.8800962097757, 893.0469066782865, 1067.7140827599305, 882.8372497229052, 1378.5564969880652, 974.9466803073703, 687.8775590573575, 894.2159492918917, 1549.3143024136416, 1033.6246029293468, 890.0342267461797, 1224.916645818576, 1061.4772187228878, 896.4512679490452, 1164.7965875411674, 902.0142726313054, 1371.0597954154964, 875.7451728700573, 1452.0707006123002, 835.8732961387202, 1133.092691955119, 1603.575274058572, 1431.8751745739366, 1022.6104457023889, 1069.8946411727331, 1289.3668358381867, 1184.394274272272, 1056.6570370757431, 1140.300770178893, 1167.4600156991082, 699.6579999999999, 993.0533778458664, 1166.0496108291627, 1022.1185252063017, 1502.9048911361192, 1263.3761797802463, 934.546872331343, 792.8321321881785, 1216.883617867313, 474.1745896211261, 1188.8873872576082, 1305.9943760261372, 1029.5107507546466, 1283.2632044469606, 1201.9656082956008, 1216.4735788756946, 995.9210434644027, 1233.0116834880878, 1319.4040292296206, 1066.6371567823794, 897.3234670280815, 1204.1032492148784, 1033.3384010942605, 663.1772683983493, 1168.7843140112968, 1257.7882756309696, 1060.7711403098385, 762.0142994850331, 1258.2467369212025, 1022.8455584783301, 923.1798993937028, 984.2310334520253, 858.9402423676564, 1050.6093757157657, 1289.1560117263462, 1578.6120525794793, 900.3310192283881, 760.7827077618944, 938.7860978800479, 1226.3739524662892, 1323.1096874185973, 1062.3423947318386, 1576.2427709932535, 987.4907047869469, 1065.280145931389, 845.253898673823, 1581.9492212718023, 752.8698755061841, 1487.3476700921542, 1182.106525225091, 1069.4491757474589, 1052.2765640684393, 1075.5123526726834, 770.3467941662097, 1193.623042054187, 1178.3829497774557, 1019.4695790330326, 1101.3961969087568, 1179.5880766036607, 1393.1992334943218, 749.6579999999999, 1126.1485366979484, 495.2804319851092, 1198.6289165972862, 1430.323793950625, 1334.1568525189446, 1442.5778639962282, 1293.216158048103, 1019.8764805022428, 1270.8715333590344, 605.1901163764592, 1274.3779963221941, 1140.6246047421082, 1013.9046157286273, 1379.6625632864452, 869.7719407627046, 801.6881156993189, 947.9039891957243, 1153.7425273674169, 1070.1164915382956, 1124.723753931184, 999.253, 899.4585221396742, 915.9488016055902, 1268.7027028322786, 1214.0733007368433, 1140.8274442355332, 1098.4793465063233, 956.9521699108221, 1261.600939604973, 1052.7980534196647, 806.7244343738474, 752.0961157169403,
              1392.6910977742987, 1540.903516673795, 1288.3512827600455, 1344.6371948158906, 1445.034192911081, 937.2315562856606, 1365.42329969542, 1188.5758957004919, 1101.5459593662108, 698.8119999999999, 1033.7699323098384, 1027.5649249748153, 898.3209059175525, 1067.9553373828785, 1055.088002398681, 955.3887723153256, 958.5510208182942, 1181.9462294899945, 1335.603704805918, 1187.1487904445853, 1310.5390927702008, 1125.8990719911699, 1219.2640625509148, 990.1396959767519, 1130.2334115367912, 993.3778035068958, 1473.7992971605984, 924.4487997872585, 918.1792623238609, 634.3007922592533, 1183.528933219505, 1040.5925857601135, 1008.3651298783744, 771.0791366518667, 809.3243840794795, 1319.1656821927281, 1237.79337945618, 1474.4078370433847, 1026.0008825911602, 899.6579999999999, 1069.6980901865054, 649.6579999999999, 1069.5721852880042, 801.3412481363285, 1252.1522405560727, 984.219075225938, 699.276556705934, 1336.7581175641062, 1241.8188404491086, 1538.871418420569, 1080.6171236318735, 1027.5904412924158, 778.5961032781536, 849.7511728252055, 1419.649293522839, 1161.6088571743126, 799.6579999999999, 1200.8985912845706, 1366.0513568550673, 1385.4526489846385, 1437.3485340376756, 1519.1844300562798, 1105.5377685022872, 944.0681558485463, 1029.3254411857602, 1220.8532047037068, 854.016750191538, 1069.9594227170628, 1649.838843345097, 1376.9385578494212, 753.9764221640922, 1199.9297515532144, 1241.9627353797239, 1157.878763001284, 738.8985329089741, 1358.6753077463254, 964.1146608871746, 948.8119999999999, 1419.1502440830927, 1010.098713013622, 1246.0217617085311, 896.7070776015754, 1087.412960814883, 792.8959837721735, 975.846295673257, 1486.7247430812329, 838.2041947556689, 1154.537734573505, 1065.8079499978644, 1086.5471372111292, 1081.4465856694264, 920.1406018944355, 1173.1915749984164, 1088.073601431442, 861.3912301784803, 1551.1360636372187, 1127.812243121055, 1374.9864476728555, 1430.0129703499656, 1292.7323109117751, 748.6527728658772, 1347.0068407645676, 674.2347415983887, 1123.1663616690976, 1033.513531575462, 929.2050251788504, 459.02069089765826, 999.2410959129459, 1274.2286394555927, 1008.2697505059593, 1351.5077528791182, 971.685979619984, 1362.5345028031365, 1291.1063287332645, 965.3215201268109, 1074.9264081402475, 1314.865548648213, 1163.3876140028724, 1709.5592962889712, 1230.4093349437987, 1244.7896727013904, 1109.1911020780467, 1089.435565335397, 868.9590820468962, 1329.933532717847, 888.259816207458, 969.694735864746, 1031.549819559633, 1400.6769941707018, 1272.314563059165, 1246.4382211050186, 835.6333531464254, 900.4329163843415, 1358.7264721242327, 1215.3383201590243, 1033.1517043176943, 865.9119511156999, 759.0859079451128, 1021.1065334882516, 1021.0032534612875, 1008.2924097335816, 1096.0614398837483, 1342.0647909371698, 1285.3826429752758, 886.5753618623626, 1145.2113972043257, 1229.2692861668374, 1538.9404096574247, 983.3034815325661, 1002.7408593574933, 1310.2083956400822, 953.7329912455637, 1259.1425419496854, 698.812, 1251.4414483168073, 1043.077916741648, 815.3463241085201, 1091.869269969237, 1400.3746916809378, 1275.351138975366, 1299.69908079002, 972.2122036718944, 642.4034364715513, 1124.1867944667729, 992.1760462622501, 839.209399983589, 1089.2075151343458, 974.0288377256634, 1147.6395962012643, 1009.8762950272633, 1115.345709068033, 842.536901469799, 895.1377541745571, 1168.8944570844565, 943.5092301546464, 704.1484625969548, 1604.9490169627195, 1054.373701215895, 1058.7312775882262, 772.958564482821, 1509.5248777889758, 1359.816754829399, 1074.0288323515394, 949.6579999999999, 1146.2087248509251, 886.1132763510066, 889.8608117465169, 808.5733683444845, 1125.738094851219, 1223.2735770267245, 1020.427430793873, 785.8027911140156, 1524.409673290696, 1382.2332343189314, 1270.5260281928968, 972.937955355811, 985.8928615299806, 1266.7303009243117, 887.4730593666175, 736.7537646431715, 1066.5491804871438, 804.9263797124282, 1107.6513506191136, 537.8295519514104, 975.9553776950021, 799.253, 805.2580131657643, 1126.0477584706398, 1209.1215627015342, 1296.0430491489274, 928.5539303779798, 1158.2737528846653, 1318.0106758776878, 1392.7833562047822, 1684.971948379823, 938.5020375337446, 1484.3846966080248, 953.3435802402203, 808.6510513414405, 1354.1320745889825, 1254.30812510316, 1298.812, 1210.0282074398383, 774.3376314978171, 879.7806131165592, 856.6694756248246, 1207.6531861250821, 1387.1508779874712, 832.1619952276694, 829.8402105713182, 1300.4815814065892, 1184.3260927328454, 1086.9879802211476, 990.835242336184, 868.1738597898749, 1035.8964585710721, 1266.4037551611896, 917.8333230773356, 1222.0554058851994, 514.161743602615, 849.2580183261323, 791.1216277436895, 1628.6634528340971, 870.7151156141749, 1150.2057042586478, 1124.6661469037358, 936.4310591816462, 1216.1753234050163, 1432.5777565578646, 791.6644170962265, 1169.9727197098994, 1018.7404497409784])
m = []
for j in range(1, 505):
    m.append(a[0: j].sum()/j)
print(m)
