__author__ = 'Jiaxiao Zheng'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def z(x,y,M):
    cnt = np.zeros((M,M))
    for a in range(0,M-1):
        for b in range(0,M-1):
            cnt[(a * x + b) % M, (a * y + b) % M] += 1

    print(cnt)
    plt.imshow(cnt, interpolation = 'none')
    return cnt

z(x = 1, y = 5, M = 8)
wait = input("PRESS ENTER TO CONTINUE.")
z(x = 1, y = 4, M = 8)
wait = input("PRESS ENTER TO CONTINUE.")
