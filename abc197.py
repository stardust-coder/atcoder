# n = int(input())
# x0,y0 = map(int,input().split())
# xh,yh = map(int,input().split())
# centerx,centery = ((x0+xh)/2,(y0+yh)/2)

# import math
# import numpy as np
# c0 = (x0-centerx,y0-centery)

# def rotation_o(u, t, deg=False):
#     # 度数単位の角度をラジアンに変換
#     if deg == True:
#         t = np.deg2rad(t)
#     # 回転行列
#     R = np.array([[np.cos(t), -np.sin(t)],
#                   [np.sin(t),  np.cos(t)]])
#     return  np.dot(R, u)

# c1 = rotation_o(c0,np.pi*2/n)
# x1,y1 = c1[0]+centerx, c1[1]+centery
# print(x1,y1)

#C
n = int(input())
alist = list(map(int,input().split()))
kouho = [alist[0]]
# for i in range(n+1):
#     afirst = alist[:i]
#     alast = alist[i:]
#     res1 = 0
#     res2 = 0
#     for a in afirst:
#         res1 = res1 | a
#     for a in alast:
#         res2 = res2 | a
#     kouho.append(res1^res2)

# print(min(kouho))

for i in range(1,n):
    new = alist[i]
    newkouho = []
    for k in kouho:
        newkouho.append(k|new)
        newkouho.append(k^new)
    kouho = newkouho
    print(kouho)

print(min(kouho))  
        
