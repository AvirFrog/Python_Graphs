# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:03:19 2022

@author: AvirFrog
"""

V = [0, 1, 2, 3, 4]
E = [(0,1),
     (1,2),
     (2,3),
     (3,4),
     (4,1),
     (0,2),
     (2,4),
     (4,1),
     (1,3),
     (3,0)
     ]

v_start = 0

for x,y in E:
    if x == v_start:
        print(y)
        
print([y for (x,y) in E if x == v_start])

