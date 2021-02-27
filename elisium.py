import numpy as np
import copy
import itertools
from collections import deque#O(1)でpopできる

n = int(input())
coordinates = []#点一覧
xsum = 0
ysum = 0
for i in range(n):
    x,y = map(int,input().split())
    index = i
    xsum += x
    ysum += y
    coordinates.append([x,y,index])
ave = [xsum/n,ysum/n] 
sortdist = lambda val:(val[0]-ave[0])**2+(val[1]-ave[0])**2
#coordinates_index = [j[2] for j in sorted(coordinates,key=sortdist)]#内側からみていくことで多角形の内側に新規点が登場するのを回避
coordinates_index = [j[2] for j in coordinates]
coordinates_index.reverse()

print("co_ind",coordinates_index)#確認用


def judgement(order):
    order_d = copy.deepcopy(order)
    order_d.append(order[0])
    order_d.append(order[1])
    res = True
    for i in range(len(order)):
        p1 = coordinates[order_d[i]][:2]
        p2 = coordinates[order_d[i+1]][:2]
        p3 = coordinates[order_d[i+2]][:2]
        v1 = np.array(p2)-np.array(p1)
        v2 = np.array(p3)-np.array(p2)
        if np.cross(v1,v2) < 0:
            res = False
            break
    return res

def p_judgement(order,i,new):
    order_d = copy.deepcopy(order)
    order_d.append(order[0])
    order_d.append(order[1])
    p0 = coordinates[order[i-1]][:2]
    p1 = coordinates[order[i]][:2]
    p2 = coordinates[new][:2]
    p3 = coordinates[order_d[i+1]][:2]
    p4 = coordinates[order_d[i+2]][:2]
    v1 = np.array(p1)-np.array(p0)
    v2 = np.array(p2)-np.array(p1)
    v3 = np.array(p3)-np.array(p2)
    v4 = np.array(p4)-np.array(p3)
    if np.cross(v1,v2) > 0 and np.cross(v2,v3) > 0 and np.cross(v3,v4) > 0:
        return True
    else:
        return False 

def intersection(p1,p2,p3,p4):#線分p1p2とp3p4が交差しているか否か
    t1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    t2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    t3 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    t4 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return t1*t2<0 and t3*t4<0

def judgement_intersection(order):
    edgelist = [[order[i-1],order[i]] for i in range(len(order))]
    res = False
    for u in itertools.combinations(edgelist, 2):
        p1 = coordinates[u[0][0]]
        p2 = coordinates[u[0][1]]
        p3 = coordinates[u[1][0]]
        p4 = coordinates[u[1][1]]
        if intersection(p1,p2,p3,p4) == True:
            res = True
            break
    return res

#まず５点の時の左折閉路を星状でゲットする（前問により存在が保証されているので全探索すればよい）
G = coordinates_index[0:5]#5点
for v in itertools.permutations(G):
    if judgement(list(v)) == True:
        start = list(v)

#t点の左折閉路をt+1点にする
def add(star, new):
    for i in range(len(star)):
        if p_judgement(star,i,new) == True:
            star.insert(i+1,new)
            return star,None
    return star, new

import random
co = coordinates_index[5:]
random.shuffle(co)
result = copy.deepcopy(start)
while co:
    print("co",co)
    new = co[0]
    co.pop(0)
    result, remainder = add(result,new)
    print("r",result,remainder)
    if remainder != None:
        print("hogehoge")
        co = random.sample(coordinates_index[5:],n-5)
        result = copy.deepcopy(start)
    print(result)

print("final",judgement(result),result)

