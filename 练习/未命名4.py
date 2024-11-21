# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:09:35 2024

@author: 25051
"""

#求初值问题，区间在[0,1]之间，取步长为0.1
#用显式欧拉求解

import numpy as np
yn = 1
sequence = np.arange(0, 1.1, 0.1)
for i in sequence:
    print(f"当xn={i+0.1}时，yn={1.1*yn-0.2*i/yn}")
    
    
    
    

