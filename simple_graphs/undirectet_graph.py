# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:02:56 2022

@author: AvirFrog
"""

def connected(who, V, E):
    n = []
    for v1, v2 in E:
        if V[v1] == who:
            n.append(V[v2])
        elif V[v2] == who:
            n.append(V[v1])
            
    return n

V = [0, 1, 2, 3, 4]
E = [[0, 1],
     [0, 2],
     [0, 3],
     [0, 4],
     [1, 2],
     [1, 4],
     [2, 3],
     [2, 4],
     [3, 1],
     [3, 2],
     [4, 2],
     [4, 3]
     
     ]



    
    
print(connected(0, V, E))
