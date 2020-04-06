import math
import datetime
from datetime import datetime, timedelta

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

def corona_log(c1, c2):
    return 3/(math.log2(c2) - math.log2(c1))

def daterange(_start, _end):
    for n in range((_end - _start).days):
        yield _start + timedelta(n)

start = datetime.strptime('2020/3/8', '%Y/%m/%d').date()
end   = datetime.strptime('2020/4/6', '%Y/%m/%d').date()
c_Osaka = [55, 55, 73, 80, 89, 92, 102, 106, 108, 112, 117, 119, 123, 125, 131, 134, 142, 149, 156, 176, 191, 208, 216, 244, 278, 311, 346, 387, 408]
c_Tokyo = [64, 64, 67, 73, 75, 77, 87, 90, 90, 102, 111, 118, 129, 136, 138, 154, 171, 212, 259, 299, 362, 430, 443, 521, 587, 684, 773, 890, 1033]
c_NY    = [106, 142, 173, 217, 326, 421, 610, 732, 950, 1374, 2382, 4152, 7102, 10356, 15168, 20875, 25665, 33066, 38987, 44635, 53363, 59568, 67174, 75832, 83889, 92770, 102870, 114966, None]

day = []
for i in daterange(start, end):
    day.append(i)

y_Osaka = [None for _ in range(3)]
y_Tokyo = [None for _ in range(3)]
y_NY    = [None for _ in range(3)]
for i in range(len(day)-3):
    y_Osaka.append(corona_log(c_Osaka[i], c_Osaka[i + 3]))
    y_Tokyo.append(corona_log(c_Tokyo[i], c_Tokyo[i + 3]))
    if i < len(day)-4:
        y_NY.append(corona_log(c_NY[i], c_NY[i + 3]))
    else:
        y_NY.append(None)

plt.figure(figsize=(8, 4.2))
plt.plot(day, y_Osaka, color='green', label='Osaka')
plt.plot(day, y_Tokyo, color='red',   label='Tokyo')
plt.plot(day, y_NY,    color='blue',  label='NY')
plt.grid(axis='y', color='gray', lw=0.5)
plt.xticks(day, rotation = 90)
plt.yticks(np.arange(5, 21, 5))
plt.ylim(0, 21)
plt.ylabel('累計感染者数が2倍になるのにかかる日数(日)')
plt.title('累計感染者数が2倍になるのに何日かかるペースか？')
plt.legend()
plt.show()
